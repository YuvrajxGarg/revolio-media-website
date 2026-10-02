# Revolio website

A dependency-free, responsive portfolio with 20 project stories, a filterable work index, studio positioning, Revolio Mag, Dumb Biryani, and an email-draft enquiry flow.

## Edit

- `projects.json`: project copy, categories, images, and verified outbound links. The `pages` field maps each story to the supplied deck.
- `render.py`: shared navigation, page layouts, home, magazine/originals, contact, and privacy copy. `build.py` runs the renderer.
- `dist/revolio.css`: visual system, responsive layouts, typography, native image proportions, and motion.
- `dist/experience.js`: project reel, wall/index views, filters, discovery, menu, reveals, and enquiry draft.
- `dist/assets/`: actual project images extracted from the supplied PDF.

After editing page content, run `python build.py`. Serve `dist/` with any static web server; for example, `python -m http.server 4173 --directory dist`. Open http://localhost:4173. Directory routes require an HTTP server, rather than opening index.html directly.

## Content provenance

The main project source is the 43-page **Revolio Media Deck 2026.pdf** supplied from the Desktop. All pages were rendered and inspected. Some text was embedded in slide images and was read visually. Project imagery is extracted from the deck; no generated or stock campaign imagery is used.

Additional public sources, reviewed 2 October 2026:

- https://www.instagram.com/revoliomedia/ — all 22 posts exposed by the signed-in profile; relevant work posts are linked in the portfolio. Internal office posts and a podcast appearance were not presented as client projects.
- https://www.instagram.com/revoliomag/ — magazine identity and publication link.
- https://www.instagram.com/dumbbbiryani/ — original-series identity and Greece episode link.
- https://revoliomag.substack.com/p/why-is-everyone-recording-themselves — essay title, author, date, and short editorial summary.

The existing revolio.in website returned a 404 during research, so no inaccessible website-only material is claimed as reviewed. The Downloads PDF was empty; the working source was the later Desktop copy.

## Editorial decisions

- No follower counts, inflated audience totals, campaign performance claims, ranking claims, or agency awards were added.
- The portfolio's project count is a count of the actual displayed records.
- Original headlines and strategic observations are new website copy, grounded in the deck's descriptions. They are not attributed client quotes.
- Client scope is described only where supported. No invented dates, testimonial quotes, budgets, deliverable totals, team sizes, or results.
- Timing-dependent deck statements, such as an upcoming season, were omitted where current status could not be verified.
- Direct links come from PDF annotations or observed Instagram posts. Projects without a verified direct watch link retain a complete case page and enquiry CTA.
- The enquiry form prepares a mailto draft addressed to the deck's info@revolio.in. It does not send messages, simulate successful submission, or store data.

## Hosting and privacy

The registered Sites project is private for review. The existing revolio.in domain has not been changed. Fonts load through Google Fonts; campaign images are local. Instagram and YouTube content is linked rather than automatically embedded. No advertising or analytics code is installed.

## Brand assets

The supplied `download (4).png` is preserved byte-for-byte at `dist/assets/revolio-mark.png`. The mark has no background box. It is black on light and vermilion surfaces and inverted to white on dark sections. The transparent SVG favicon uses the same image and adapts to the browser color scheme.

## Complete redesign

The current design uses a monochrome editorial base and a vermilion accent independent of the deck colors. The homepage has a keyboard-operable six-project reel, an irregular work wall, native details disclosures, and original-series/editorial sections. The portfolio has wall/index modes and category filters. Portrait and landscape project images are shown in their native proportions or with contain-fit, never cover-cropped. Original PDF image objects were recovered for 14 primary projects; galleries show complete frames. Motion respects reduced-motion preferences.
