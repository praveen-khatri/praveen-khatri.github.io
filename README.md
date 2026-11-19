# Praveen Khatri · Academic Research Website

An original, responsive, multi-page academic website built for GitHub Pages. No paid theme, account keys, external scripts, analytics, frameworks, or build tool required.

## Pages and features

- `index.html` — editorial homepage, research highlights, featured *Molecular Plant* discovery, awards and professional service.
- `research.html` — four research programs and methodological toolkit.
- `publications.html` — 16 selected research outputs, filter by type, live search and copyable citations.
- `about.html` — research story, academic timeline, awards and service.
- `cv.html` — online academic CV with a downloadable three-page public-facing PDF.
- `contact.html` — email, ORCID, Google Scholar and LinkedIn links.
- `404.html` — custom missing-page screen.
- `assets/images/*.svg` — original botanical/molecular illustrations.
- `assets/images/favicon.png` — browser tab icon (PNG).
- `assets/images/apple-touch-icon.png` — Apple home-screen icon.
- Mobile navigation, keyboard-accessible controls, skip link, descriptive image text, reduced-motion support and responsive layouts.

## Publish on GitHub Pages (no command line needed)

1. Unzip the archive you received.
2. Sign in to GitHub and create a **public** repository. Choose either:
   - `YOUR-USERNAME.github.io` for `https://YOUR-USERNAME.github.io/`; or
   - a project name such as `research-website` for `https://YOUR-USERNAME.github.io/research-website/`.
3. Upload **the contents** of `praveen-khatri-website`, so `index.html` is in the repository root. Do not upload just the ZIP or add an extra enclosing folder. Preserve `assets/` and `.nojekyll` (the latter is optional but recommended).
4. Commit to the `main` branch.
5. Open **Settings → Pages → Build and deployment**. For **Source**, choose **Deploy from a branch**. Set **Branch: `main`**, **Folder: `/(root)`**, then save.
6. Open your GitHub Pages URL after GitHub reports a successful deployment in **Settings → Pages**.

GitHub documentation: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

### Alternative: Git / GitHub Desktop

Commit the unzipped project to your chosen repository. Then follow the same Pages settings above. All local links use relative paths, so the site works on a user root domain **or** under a project repository path.

### Test locally

Opening `index.html` directly in a browser works because the site uses plain HTML, CSS, JavaScript and SVGs.

For a local web server, from this folder:

```bash
python -m http.server 8000
```

Open `http://localhost:8000`.

## Editing the site

- **Text, publications, projects and academic details:** edit the content near the top of `build_site.py` and the page functions further down. Run `python build_site.py` to regenerate all HTML pages. Alternatively, edit the HTML files directly (but future regeneration will overwrite direct edits).
- **Colors and layout:** `assets/css/style.css` has all styles. Variables are declared in `:root`.
- **Menus, publication filters and copy actions:** `assets/js/main.js`.
- **Images:** replace the original SVG files in `assets/images/` with your own artwork, keeping filenames. Run `python create_art.py` only if you want to reset the illustrations to their included originals.
- **Public CV PDF:** edit `make_public_cv.py` and run `python make_public_cv.py` (requires `reportlab`, and uses DejaVu fonts when installed). You can alternatively replace `assets/docs/Praveen_Khatri_Public_CV_2026.pdf` with an updated PDF of the same name.
- **Profile photo:** not included, because an approved photo was not available. The design intentionally uses custom scientific illustrations rather than a placeholder or an invented portrait. You can add a real headshot to the About page later.
- **Custom domain:** add your domain in GitHub Pages settings after publishing. If doing so, consider adding canonical URLs and a sitemap based on the final domain.

## Important editorial / privacy checks before publishing

Content was compiled from your September 2026 full CV, a November 16, 2026 abbreviated CV and verified article pages. It was prepared on **November 18, 2026**. Confirm all statements before making the repository public.

- The *Phytochemistry Reviews* glyceollin article is marked **accepted, not yet published**. Update when a formal paper/DOI is issued.
- The 2026 GmIFH article is marked **bioRxiv preprint, not peer reviewed**. Update only after formal acceptance/publication.
- Ongoing salvinorin and time-course work is described generally without identifying unpublished candidate enzymes or disclosing confidential data.
- The public CV intentionally excludes personal phone number, identity numbers, date of birth, private addresses and referee contact details.
- Publication listings are **selected**, not a claim to include every contribution. Five *Plant Physiology* News & Views items appear here; a later commentary listed in the September CV was omitted because its article number and DOI appeared inconsistent and need confirmation.
- The Google Scholar link currently uses the URL listed in the CV (`https://bit.ly/3sAjuCn`). You may replace it with the direct Scholar profile URL.
- This is a **public-facing academic research website**, not a substitute for your longer 10-page CV used in academic job applications.

## Structure

```text
praveen-khatri-website/
├── index.html
├── research.html
├── publications.html
├── about.html
├── cv.html
├── contact.html
├── 404.html
├── .nojekyll
├── build_site.py
├── create_art.py
├── make_public_cv.py
└── assets/
    ├── css/style.css
    ├── js/main.js
    ├── images/*.svg
    └── docs/Praveen_Khatri_Public_CV_2026.pdf
```

Copyright © 2026 Praveen Khatri. All rights reserved. No third-party theme code is used. Article titles and metadata are credited to their original publishers and authors.

### Favicon

The site uses `assets/images/favicon.png` on every page (and an Apple touch icon). Replace these PNG files with your own square artwork when updating the icon. If you regenerate HTML using `build_site.py`, ensure it retains the PNG favicon references.
