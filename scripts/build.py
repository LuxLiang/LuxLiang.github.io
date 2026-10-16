"""Generate GitHub Pages HTML and sitemap with the Python standard library."""

from datetime import date
from html import escape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://luxliang.github.io/"
PAGES = {
    "home": ("index.html", "Luxu Liang | Personal Homepage | Tsinghua University",
             "Luxu Liang is a Ph.D. student in Finance at Tsinghua University researching optimization, uncertainty quantification, reliable AI, and LLM-generated text detection."),
    "research": ("research.html", "Research | Luxu Liang | Tsinghua University",
                 "Research and publications by Luxu Liang on LLM-generated text detection, discrete sampling, stochastic optimization, and uncertainty quantification."),
    "cv": ("cv.html", "CV | Luxu Liang | Tsinghua University",
           "Academic CV of Luxu Liang: education at Tsinghua, Renmin, and Jilin universities, research experience, academic service, scholarships, and awards."),
    "contact": ("contact.html", "Contact | Luxu Liang | Tsinghua University",
                "Contact Luxu Liang, a Finance Ph.D. student at Tsinghua University, about research and collaboration in reliable AI and decision-making under uncertainty."),
}


def build():
    template = (ROOT / "_site_source/site.html").read_text()
    section_pattern = re.compile(r'    <section\b[^>]*data-page="([^"]+)".*?</section>', re.S)
    assert set(section_pattern.findall(template)) == set(PAGES)
    person = {
        "@type": "Person", "@id": BASE + "#person", "name": "Luxu Liang",
        "url": BASE, "image": BASE + "assets/lux-liang-portrait.webp",
        "description": PAGES["home"][2],
        "affiliation": {"@type": "CollegeOrUniversity", "name": "Tsinghua University"},
        "sameAs": ["https://scholar.google.com/citations?user=VHr-Lf4AAAAJ"],
    }
    urls = []
    for name, (filename, title, description) in PAGES.items():
        url = BASE if name == "home" else BASE + filename
        urls.append(url)
        page = section_pattern.sub(
            lambda match: match[0].replace(" hidden>", ">") if match[1] == name else "", template)
        page = page.replace(f'data-page-link="{name}"', f'data-page-link="{name}" aria-current="page"')
        if name != "home":
            page = page.replace(f'<h2 id="{name}-title">', f'<h1 id="{name}-title">').replace("</h2>", "</h1>")
        schema = {
            "@context": "https://schema.org",
            "@graph": [person, {
                "@type": "WebPage", "@id": url + "#webpage", "url": url,
                "name": title, "description": description, "about": {"@id": BASE + "#person"},
            }],
        }
        values = {
            "title": escape(title, quote=True), "description": escape(description, quote=True),
            "url": url, "year": str(date.today().year),
            "structured_data": json.dumps(schema, ensure_ascii=False, indent=4),
        }
        for key, value in values.items():
            page = page.replace("{{" + key + "}}", value)
        assert "{{" not in page
        (ROOT / filename).write_text(page)
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "".join(f"  <url><loc>{url}</loc></url>\n" for url in urls)
    (ROOT / "sitemap.xml").write_text(sitemap + "</urlset>\n")
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: " + BASE + "sitemap.xml\n")


if __name__ == "__main__":
    build()
