# Guess Who Generator

Static browser app for making custom printable Guess Who cards. Hosted for now on my website and [available to run](http://samrickman.com/guess-who/index.html).

## What It Does

- Upload your own character images in the browser.
- Edit the displayed names after upload.
- Generate a single printable PDF containing blue player cards, red player cards, selection card fronts, and selection card backs.
- Switch between A4 and US Letter paper.
- Choose black or white card-front backgrounds.

I originally built this because I wanted to make a custom Deltarune version for my daughter's birthday and kept running into paid Etsy templates which required lots of image resizing and manual dragging and dropping. I also used it as a real test of Codex with GPT-5.4 and was extremely impressed by how much of the app could be built and iterated that way.

The sample sets are Undertale and Deltarune images but you can upload any images.

## Run Locally

Serve the folder with any static file server, for example:

```bash
python -m http.server 8000 -d .
```

Then open `http://localhost:8000`.

## Deploy on the web

If you want to host this from an existing website, create the desired folder e.g. `public/guess-who/`.

Then copy into that folder:

- `index.html`
- `app.js`
- `styles.css`
- `assets/`
- `presets/`

## Notes

- Everything runs client-side in the browser.
- User data (e.g. images) are not uploaded to a backend server.
- The generated output is downloaded as `guess-who-printables.pdf`.
- The page uses a CDN copy of `jsPDF`, so internet access is needed unless you vendor that dependency locally.
- `index.html` references `app.js` and `styles.css` with a version query string for cache busting. That is safe on the web and simply helps browsers pick up new deployments faster.

## Sample Presets

Sample sets are loaded from `presets/<name>/manifest.json`.

If you change the images inside a preset folder, regenerate the manifests with:

```bash
python generate-preset-manifest.py
```

Supported preset image formats are:

- `png`
- `webp`
- `jpg`
- `jpeg`
- `gif`

## Project Structure

- `index.html`: page markup
- `styles.css`: page styling
- `app.js`: browser-side app logic and PDF generation
- `assets/`: bundled card-back images
- `presets/`: bundled sample image sets
- `generate-preset-manifest.py`: helper to refresh preset manifests

## License

- The source code in this folder is licensed under MIT. See `LICENSE`.
- Bundled sample images and other third-party visual assets are excluded from that license. See `NOTICE`.
- Only use images you have the right to use.
- This is provided as-is and is for personal use only. Please don't sue me.
