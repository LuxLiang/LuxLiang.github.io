# Luxu Liang — Academic Website

Academic website published with GitHub Pages at <https://luxliang.github.io>.

## Edit in VS Code

Open this folder in VS Code:

```bash
code /home/yangzheyuan/lux_work_space/LuxLiang.github.io
```

Edit `_site_source/site.html` for shared layout and page content. Then regenerate
the public HTML pages and sitemap using Python (no extra dependencies):

```bash
python scripts/build.py
```

Page titles and descriptions are defined in `scripts/build.py`. The generated
`index.html`, `research.html`, `cv.html`, and `contact.html` each contain their
content without requiring JavaScript. Edit the template rather than generated
HTML so future builds preserve your changes.

Install the recommended **Live Server** extension, then right-click `index.html`
and choose **Open with Live Server** to preview changes. Existing `/#cv`,
`/#research`, and `/#contact` links redirect to their corresponding HTML pages.

## Publish

```bash
python scripts/build.py
git add index.html research.html cv.html contact.html sitemap.xml robots.txt _site_source scripts style.css script.js assets README.md
git commit -m "Describe your update"
git push
```

Every push to `main` is published automatically by GitHub Pages after the Pages
source is set to **Deploy from a branch → main → /(root)** in repository settings.

## Google Search

The public pages include unique titles/descriptions, canonical URLs, and Person
and WebPage structured data. `robots.txt` allows crawling and points to
`https://luxliang.github.io/sitemap.xml`.

To check Google's actual indexing status, verify the URL-prefix property
`https://luxliang.github.io/` in Google Search Console. Submit `sitemap.xml`, then
inspect the homepage URL and request indexing. Verification requires the site
owner's Google account; if Google provides an HTML verification file, put that
exact file at the repository root and publish it before completing verification.
Indexing and search ranking are controlled by Google and are not immediate.
