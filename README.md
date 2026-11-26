# aiforia.eucaif.org

Landing page for AIFORIA, a EuCAIF initiative. Built with [Astro](https://astro.build),
intended to be served at `https://aiforia.eucaif.org` through GitHub Pages.

The look (fonts, colours) mirrors the main site, [eucaif.org](https://eucaif.org)
([repository](https://github.com/EuCAIF/eucaif.org)).

## Editing

The whole page is `src/pages/index.astro`; styles are in `src/styles/global.css`.

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
