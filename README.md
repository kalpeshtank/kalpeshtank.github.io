# Kalpesh Tank Portfolio

Static GitHub Pages portfolio for international frontend engineering roles.

## What is included

- Region selector: Global, UK, Germany, USA, India
- Language selector: English and German
- Dynamic region summary, SEO metadata, JSON-LD schema, and primary resume CTA
- Region-specific resume download links in `assets/resumes/`
- Responsive dark/light UI with accessible form controls
- GitHub Actions deployment workflow for GitHub Pages

## Local setup

This is a dependency-free static site. Run it with any local static server:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

Opening `index.html` directly may block translation JSON loading in some browsers because of local file security rules.

## Content structure

```text
src/
  app.js
  data/
    profile.js
    regions.js
  i18n/
    en.json
    de.json
  utils/
    geoLocation.js
    seo.js
assets/
  resumes/
    kalpesh-tank-uk-cv.pdf
    kalpesh-tank-germany-cv.pdf
    kalpesh-tank-usa-resume.pdf
    kalpesh-tank-india-resume.pdf
```

## Deployment

The workflow at `.github/workflows/deploy.yml` deploys this static site to GitHub Pages on pushes to `main` or `master`.

1. In GitHub, go to repository Settings > Pages.
2. Set Source to GitHub Actions.
3. Push changes to `main` or `master`.
4. The workflow uploads the repository root as the static site artifact.

## Environment variables

No environment variables are required.

## Testing checklist

- Region dropdown updates the hero label, summary, SEO title, and primary resume CTA.
- Language dropdown updates navigation, sections, stats, labels, and form text.
- Region and language choices persist after reload via `localStorage`.
- All four resume buttons download a PDF from `assets/resumes/`.
- Browser geolocation/IP fallback does not block the page if permission is denied or unavailable.
- Layout works on mobile, tablet, and desktop.
- Dark/light mode persists after reload.
