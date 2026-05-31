from __future__ import annotations

from .tfhub_search import DEFAULT_TFHUB_MODEL


def main() -> None:
    try:
        import tensorflow_hub as hub  # type: ignore
    except ImportError as exc:
        raise SystemExit("Falta tensorflow-hub. Ejecuta: pip install -r requirements-tfhub.txt") from exc
    print("Cargando modelo TensorFlow Hub. La primera vez puede tardar por descarga...")
    model = hub.load(DEFAULT_TFHUB_MODEL)
    vectors = model(["evaluación formativa", "planeación didáctica"]).numpy()
    print("TensorFlow Hub funciona correctamente.")
    print(f"Modelo: {DEFAULT_TFHUB_MODEL}")
    print(f"Forma de embeddings: {vectors.shape}")


if __name__ == "__main__":
    main()
