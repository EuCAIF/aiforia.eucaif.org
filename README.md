# aiforia.eucaif.org

Website of AIFORIA, COST Action CA25172 (Artificial Intelligence for Fundamental Physics:
Open Roadmapping and Inclusive Actions), served at `https://aiforia.eucaif.org` through
GitHub Pages and built with [Astro](https://astro.build).

The look (fonts, colours) mirrors the main site, [eucaif.org](https://eucaif.org)
([repository](https://github.com/EuCAIF/eucaif.org)).

## Editing

The whole page is `src/pages/index.astro`; the Action's facts and links (number, dates,
COST URLs, working groups) are at the top of that file. Styles are in `src/styles/global.css`.

The logo files in `public/images/` are generated: edit `design/make-logo.py` and run
`python3 design/make-logo.py`.

```bash
npm ci          # install once
npm run dev     # local dev server with live reload
npm run build   # production build into dist/
```

## Deployment

`.github/workflows/deploy.yml` builds on every push to `main` and deploys once
GitHub Pages is enabled for the repository (source: GitHub Actions) with the
custom domain `aiforia.eucaif.org`. The domain needs a DNS record
`aiforia CNAME eucaif.github.io`.
