from __future__ import annotations

import html
import json
import re
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MEDIA_API = "https://www.uanl.mx/wp-json/wp/v2/media?search={query}&per_page=40"
STOPWORDS = {
    "de",
    "del",
    "la",
    "las",
    "los",
    "el",
    "y",
    "e",
    "para",
    "por",
    "con",
    "area",
    "curricular",
    "formacion",
    "profesional",
}

COURSES = [
    "Cultura de paz y derechos humanos",
    "Igualdad de genero, diversidad sexual e inclusion",
    "Calculo diferencial",
    "Algebra para ingenieria",
    "Geometria analitica",
    "Quimica general",
    "Laboratorio de quimica general",
    "Mecanica clasica",
    "Laboratorio de mecanica clasica",
    "Liderazgo, emprendimiento e innovacion",
    "Responsabilidad social y desarrollo sustentable",
    "Etica, transparencia y cultura de la legalidad",
    "Calculo integral",
    "Ciencia de los materiales",
    "Probabilidad y estadistica",
    "Ondas y calor",
    "Laboratorio de ondas y calor",
    "Dibujo para ingenieria",
    "Ecuaciones diferenciales",
    "Programacion basica",
    "Mecanica vectorial",
    "Electricidad y magnetismo",
    "Laboratorio de electricidad y magnetismo",
    "Procesos de manufactura",
    "Laboratorio de procesos de manufactura",
    "Termodinamica basica",
    "Laboratorio de termodinamica basica",
    "Introduccion a la mecatronica",
    "Algebra lineal",
    "Series de Fourier y transformadas de Laplace",
    "Fisica moderna",
    "Laboratorio de fisica moderna",
    "Mecanica de materiales",
    "Laboratorio de mecanica de materiales",
    "Mecanica y potencia de fluidos",
    "Laboratorio de mecanica y potencia de fluidos",
    "Circuitos electricos",
    "Laboratorio de circuitos electricos",
    "Electronica digital",
    "Laboratorio de electronica digital",
    "Modelado y simulacion de sistemas mecatronicos",
    "Diseno de maquinas",
    "Laboratorio de diseno de maquinas",
    "Maquinas electricas",
    "Laboratorio de maquinas electricas",
    "Analisis de sistemas dinamicos",
    "Laboratorio de analisis de sistemas dinamicos",
    "Electronica analogica",
    "Laboratorio de electronica analogica",
    "Diseno e ingenieria por computadora",
    "Laboratorio de diseno e ingenieria por computadora",
    "Sensores y actuadores",
    "Laboratorio de sensores y actuadores",
    "Introduccion a la ciencia de datos",
    "Amplificadores operacionales",
    "Laboratorio de amplificadores operacionales",
    "Control de sistemas lineales",
    "Laboratorio de control de sistemas lineales",
    "Microcontroladores",
    "Laboratorio de microcontroladores",
    "Sistemas de control logico",
    "Laboratorio de sistemas de control logico",
    "Optativa I area curricular de formacion profesional fundamental",
    "Diseno de mecanismos de precision",
    "Laboratorio de diseno de mecanismos de precision",
    "Inteligencia artificial y redes neuronales",
    "Adquisicion de datos con sistemas embebidos",
    "Arquitectura de robots",
    "Laboratorio de arquitectura de robots",
    "Prototipados rapidos",
    "Laboratorio de prototipados rapidos",
    "Optativa II area curricular de formacion profesional fundamental",
    "Optativa III area curricular de formacion profesional fundamental",
    "Optativa IV area curricular de formacion profesional fundamental",
    "Optativa V area curricular de formacion profesional fundamental",
    "Diseno de sistemas mecatronicos",
    "Laboratorio de diseno de sistemas mecatronicos",
    "Robotica industrial",
    "Laboratorio de robotica industrial",
    "Servicio social",
    "Optativa I area curricular de formacion profesional integradora",
    "Optativa II area curricular de formacion profesional integradora",
    "Proyecto integrador de ingenieria mecatronica",
    "Practicas profesionales",
    "Optativa III area curricular de formacion profesional integradora",
    "Seminario para el desempeno profesional",
    "Optativa IV area curricular de formacion profesional integradora",
]

MANUAL_SLUGS = {
    "Igualdad de genero, diversidad sexual e inclusion": "igualdad-genero-div-sexual-incl-imtc",
    "Etica, transparencia y cultura de la legalidad": "etica-transp-cultura-legalidad-imtc",
    "Responsabilidad social y desarrollo sustentable": "resp-social-desarrollo-sust-imtc",
    "Modelado y simulacion de sistemas mecatronicos": "modelado-sim-sist-mecatronicos-imtc",
    "Proyecto integrador de ingenieria mecatronica": "proyecto-integrador-mecatronica-imtc",
    "Optativa I area curricular de formacion profesional fundamental": "optativa-i-fundamental-imtc",
    "Optativa II area curricular de formacion profesional fundamental": "optativa-ii-fundamental-imtc",
    "Optativa III area curricular de formacion profesional fundamental": "optativa-iii-fundamental-imtc",
    "Optativa IV area curricular de formacion profesional fundamental": "optativa-iv-fundamental-imtc",
    "Optativa V area curricular de formacion profesional fundamental": "optativa-v-fundamental-imtc",
    "Optativa I area curricular de formacion profesional integradora": "optativa-i-integradora-imtc",
    "Optativa II area curricular de formacion profesional integradora": "optativa-ii-integradora-imtc",
    "Optativa III area curricular de formacion profesional integradora": "optativa-iii-integradora-imtc",
    "Optativa IV area curricular de formacion profesional integradora": "optativa-iv-integradora-imtc",
}

ALIASES = {
    "Algebra para ingenieria": ["Algebra"],
    "Programacion basica": ["Metodologia de la programacion"],
    "Dibujo para ingenieria": ["Dibujo tecnico", "Dibujo"],
    "Introduccion a la mecatronica": ["Mecatronica"],
    "Series de Fourier y transformadas de Laplace": ["Series de Fourier", "Transformadas de Laplace"],
    "Adquisicion de datos con sistemas embebidos": ["Adquisicion de datos"],
    "Inteligencia artificial y redes neuronales": ["Inteligencia artificial", "Redes neuronales"],
}

ENGINEERING_FOUNDATION = {
    "Calculo diferencial",
    "Calculo integral",
    "Geometria analitica",
    "Algebra para ingenieria",
}

cache: dict[str, list[dict]] = {}


def normalize(text: str) -> str:
    value = html.unescape(text or "")
    value = unicodedata.normalize("NFD", value)
    value = "".join(ch for ch in value if unicodedata.category(ch) != "Mn")
    value = value.lower()
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def slug_for_course(course: str) -> str:
    if course in MANUAL_SLUGS:
        return MANUAL_SLUGS[course]

    slug = normalize(course).replace(" ", "-")
    if len(slug) <= 40:
        return f"{slug}-imtc"

    replacements = {
        "laboratorio": "lab",
        "simulacion": "sim",
        "sistemas": "sist",
        "ingenieria": "ing",
        "analisis": "anal",
        "mecatronicos": "mecatron",
        "mecatronica": "mecatron",
        "electricos": "elec",
        "operacionales": "operac",
        "adquisicion": "adq",
        "mecanismos": "mecan",
        "precision": "prec",
        "potencia": "pot",
    }
    for source, target in replacements.items():
        slug = slug.replace(source, target)

    tokens = [token for token in slug.split("-") if token and token not in STOPWORDS]
    slug = "-".join(tokens)[:40].strip("-")
    return f"{slug}-imtc"


def aliases_for_course(course: str) -> list[str]:
    return [course, *ALIASES.get(course, [])]


def significant_tokens(name: str) -> list[str]:
    return [token for token in normalize(name).split() if len(token) >= 4 and token not in STOPWORDS]


def build_queries(course: str) -> list[str]:
    queries: list[str] = []
    seen: set[str] = set()
    for alias in aliases_for_course(course):
        norm_alias = normalize(alias)
        if not norm_alias:
            continue

        candidates = [norm_alias, re.sub(r"^laboratorio de ", "", norm_alias)]
        tokens = significant_tokens(alias)
        if len(tokens) >= 2:
            candidates.append(" ".join(tokens[:2]))
        candidates.extend(tokens[:3])

        for candidate in candidates:
            candidate = candidate.strip()
            if candidate and candidate not in seen:
                seen.add(candidate)
                queries.append(candidate)

    return queries


def fetch_media(query: str) -> list[dict]:
    norm_query = normalize(query)
    if norm_query in cache:
        return cache[norm_query]

    url = MEDIA_API.format(query=urllib.parse.quote(norm_query))
    with urllib.request.urlopen(url, timeout=45) as response:
        data = json.load(response)
    cache[norm_query] = list(data)
    return cache[norm_query]


def score_candidate(course: str, item: dict) -> int:
    blob = normalize(" ".join([
        item.get("title", {}).get("rendered", ""),
        item.get("description", {}).get("rendered", ""),
        item.get("caption", {}).get("rendered", ""),
        item.get("source_url", ""),
    ]))
    title = normalize(item.get("title", {}).get("rendered", ""))
    source_url = item.get("source_url", "")
    source_norm = normalize(source_url)

    course_is_lab = course.startswith("Laboratorio de ")
    score = 0
    alias_scores: list[int] = []

    for alias in aliases_for_course(course):
        norm_alias = normalize(alias)
        if not norm_alias:
            continue
        tokens = significant_tokens(alias)
        matches = sum(1 for token in tokens if token in blob)
        alias_score = 0
        if norm_alias in title:
            alias_score += 120
        if norm_alias in source_norm:
            alias_score += 100
        if norm_alias in blob:
            alias_score += 90
        alias_score += matches * 18
        if tokens:
            last_token = tokens[-1]
            alias_score += 20 if last_token in blob else -20
            if len(tokens) >= 3 and matches < 2:
                alias_score -= 90
            if len(tokens) == 2 and matches == 0:
                alias_score -= 90
            if matches == len(tokens):
                alias_score += 35
        alias_scores.append(alias_score)

    if alias_scores:
        score += max(alias_scores)

    if "programa analitico modalidad escolarizada" in blob:
        score += 120
    elif "programa analitico" in blob:
        score += 60
    elif "plan analitico" in blob:
        score += 25
    elif "plan sintetico y plan analitico" in blob:
        score += 10

    if re.search(r"(^|[_/\-])pa([_/\-]|$)", source_url, re.IGNORECASE):
        score += 80
    if re.search(r"(^|[_/\-])ps([_/\-]|$)", source_url, re.IGNORECASE):
        score -= 15
    if re.search(r"(^|[_/\-])me([_/\-]|$)", source_url, re.IGNORECASE) and re.search(r"(^|[_/\-])pa([_/\-]|$)", source_url, re.IGNORECASE):
        score += 20
    if course in ENGINEERING_FOUNDATION and " ing " in source_norm:
        score += 20

    if course_is_lab and "laboratorio" not in blob and not title.startswith("lab "):
        score -= 120
    if not course_is_lab and "laboratorio de" in blob:
        score -= 30

    if course == "Algebra para ingenieria" and "topicos" in title:
        score -= 25
    if course == "Introduccion a la ciencia de datos" and "datos" not in blob:
        score -= 120

    return score


def resolve_program(course: str) -> tuple[str | None, int, list[tuple[int, str]]]:
    if course.startswith("Optativa ") or course in {"Servicio social", "Practicas profesionales"}:
        return None, -1, []

    candidates: dict[int, dict] = {}
    for query in build_queries(course):
        try:
            for item in fetch_media(query):
                if item.get("mime_type") != "application/pdf":
                    continue
                candidates[item["id"]] = item
        except Exception:
            continue

    scored: list[tuple[int, str]] = []
    best_url = None
    best_score = -10**9
    for item in candidates.values():
        score = score_candidate(course, item)
        url = item.get("source_url", "")
        scored.append((score, url))
        if score > best_score:
            best_score = score
            best_url = url

    scored.sort(key=lambda pair: pair[0], reverse=True)
    if not best_url or best_score < 120:
        return None, best_score, scored[:5]
    return best_url, best_score, scored[:5]


def target_pdf(course: str) -> Path:
    slug = slug_for_course(course)
    planning = ROOT / slug / f"planeaciones-{slug}"
    planning.mkdir(parents=True, exist_ok=True)
    return planning / f"p-analitico-{slug}.pdf"


def download(url: str, target: Path) -> None:
    parts = urllib.parse.urlsplit(url)
    normalized_url = urllib.parse.urlunsplit(
        (
            parts.scheme,
            parts.netloc,
            urllib.parse.quote(parts.path, safe="/%"),
            parts.query,
            parts.fragment,
        )
    )
    request = urllib.request.Request(normalized_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=90) as response:
        data = response.read()
    target.write_bytes(data)


def main() -> int:
    downloaded = 0
    skipped_existing = 0
    missing: list[str] = []
    failed: list[str] = []
    report_lines = ["course,score,status,url"]

    for course in COURSES:
        target = target_pdf(course)
        if target.exists():
            skipped_existing += 1
            report_lines.append(f'"{course}",,existing,"{target.as_posix()}"')
            continue

        url, score, top_candidates = resolve_program(course)
        if not url:
            missing.append(course)
            report_lines.append(f'"{course}","{score}",missing,""')
            continue

        try:
            download(url, target)
            downloaded += 1
            report_lines.append(f'"{course}","{score}",downloaded,"{url}"')
        except Exception:
            failed.append(f"{course} => {url}")
            report_lines.append(f'"{course}","{score}",failed,"{url}"')

    report_path = ROOT / "reporte-descarga-programas-imtc.csv"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")

    print(f"Materias evaluadas: {len(COURSES)}")
    print(f"PDFs descargados: {downloaded}")
    print(f"PDFs ya existentes: {skipped_existing}")
    print(f"Sin coincidencia fiable: {len(missing)}")
    print(f"Errores de descarga: {len(failed)}")
    if missing:
        print("Primeras materias sin coincidencia fiable:")
        for course in missing[:20]:
            print(course)
    if failed:
        print("Primeros errores de descarga:")
        for entry in failed[:20]:
            print(entry)
    print(f"Reporte: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())