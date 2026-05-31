from __future__ import annotations

from dataclasses import dataclass
from typing import Any
import numpy as np

from .preprocessing import Fragment, clip_text
from .search import SearchHit


DEFAULT_TFHUB_MODEL = "https://tfhub.dev/google/universal-sentence-encoder-multilingual/3"


@dataclass
class TfHubSearchEngine:
    """Motor opcional: TensorFlow Hub + Universal Sentence Encoder multilingüe.

    Requiere requirements-tfhub.txt. La primera ejecución descarga el modelo y después queda en caché.
    También acepta una ruta local en TFHUB_MODEL.
    """

    fragments: list[Fragment]
    model_url_or_path: str = DEFAULT_TFHUB_MODEL

    def __post_init__(self) -> None:
        try:
            import tensorflow_hub as hub  # type: ignore
        except ImportError as exc:
            raise RuntimeError("Falta tensorflow-hub. Ejecuta: pip install -r requirements-tfhub.txt") from exc

        self._hub: Any = hub
        self._model = hub.load(self.model_url_or_path)
        self._texts = [f.text for f in self.fragments]
        self._embeddings = self._embed(self._texts)

    def _embed(self, texts: list[str]) -> np.ndarray:
        if not texts:
            return np.empty((0, 0))
        vectors = self._model(texts).numpy()
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return vectors / norms

    def search(self, concept: str, top_k: int = 8, threshold: float = 0.20, max_quote_chars: int = 700) -> list[SearchHit]:
        if not self.fragments:
            return []
        q = self._embed([concept])[0]
        sims = self._embeddings @ q
        order = np.argsort(sims)[::-1]
        hits: list[SearchHit] = []
        seen = set()
        for idx in order:
            score = float(sims[int(idx)])
            if score < threshold:
                continue
            frag = self.fragments[int(idx)]
            quote = clip_text(frag.text, max_chars=max_quote_chars)
            dedupe_key = (frag.source_id, frag.page, quote[:180].lower())
            if dedupe_key in seen:
                continue
            seen.add(dedupe_key)
            hits.append(
                SearchHit(
                    concept=concept,
                    fragment_id=frag.fragment_id,
                    page=frag.page,
                    score=score,
                    quote=quote,
                    source_id=frag.source_id,
                    source_name=frag.source_name,
                    source_path=frag.source_path,
                    source_type=frag.source_type,
                    location_label=frag.location_label,
                )
            )
            if len(hits) >= top_k:
                break
        return hits
