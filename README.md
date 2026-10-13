# Gatherly website

A responsive static multipage concept website for an activity-led social connection service. “Gatherly” is a provisional working name.

## Generate pages

Run from the project root:

```bash
python3 build_site.py
```

The generator writes nested `index.html` files under `public/`, plus the synchronized `public/manus-routes.json` page manifest. Shared styles and small navigation/filter interactions live in `public/styles.css` and `public/site.js`.

## Local preview

```bash
python3 -m http.server 3000 --bind 0.0.0.0 --directory public
```

Open `/` or one of the paths listed in `public/manus-routes.json`.

The activity images use platform-managed `/manus-storage/` paths. A plain local Python server does not proxy those paths, so local viewing can show missing images; use the managed WebDev Preview for platform storage routing. Image generation was submitted asynchronously, and its reserved URLs are expected to update when rendering finishes.

## Content status

This is a concept preview, not an event-booking site. Activity pages are illustrative. No dates, venues, prices, availability, policies, testimonials, company history, contact details, lead capture, booking, payments or customer-data collection have been configured. Add only confirmed information before public launch. Community standards, host responsibilities and reporting procedures must be operationalized before events are opened.
