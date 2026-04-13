# Slime Simulator

Touch, poke, stretch, swirl, slice digital slime with satisfying ASMR sounds. No mess, infinite replay value.

**Live:** https://gcicc.github.io/slime-sim/

## Features

- **Touch Interactions**
  - **Poke** — Tap to push a dent into the slime, it bounces back
  - **Stretch** — Drag from edge outward, stretches like taffy then snaps back
  - **Swirl** — Circular drag motion swirls the slime surface
  - **Slice** — Quick swipe cuts it in two, pieces merge back
  - **Fold** — Drag one edge over to fold onto itself

- **Slime Types**
  - Classic — Smooth, shiny, medium bounce
  - Glitter — Sparkles mixed in
  - Butter — Smoother, slower bounce, matte finish
  - Cloud — Fluffy-looking, fast bounce
  - Galaxy — Dark with nebula colors and star speckles

- **ASMR Sounds** (Web Audio API)
  - Squelch on poke
  - Stretch rising-pitch tone
  - Pop on snap-back
  - Squish on fold
  - Toggle sound with button (top right)

- **Customization**
  - 8 preset colors + custom picker
  - Switch slime types instantly

- **PWA Features**
  - Installable on iOS/Android
  - Offline playable
  - Wake lock (keeps screen on)

## Technical Stack

- Vanilla HTML/CSS/JavaScript
- Canvas 2D + Spring-mass physics (32 control points)
- Web Audio API (procedural ASMR sounds)
- Zero dependencies

## Files

- `index.html` — Complete single-file app with physics, rendering, audio
- `manifest.json` — PWA manifest
- `sw.js` — Service worker (cache-first)
- `generate-icons.py` — Icon generation (Pillow)

## Development

```bash
# Generate icons
python generate-icons.py

# Test locally
python -m http.server 8000
# Visit http://localhost:8000
```

## Deploy to GitHub Pages

```bash
git add -A
git commit -m "feat: description"
git push origin master
# Pages deploys automatically via GitHub Actions workflow
```

## Design System

- **Colors:** #0d1117 (bg), #161b22 (panels), #c4a882 (accent)
- **Fonts:** Cormorant Garamond (display), Inter (body)
- **Minimal UI:** Slime type pills at bottom, color dots, sound toggle

## Browser Support

- iOS Safari 14.5+
- Android Chrome 88+
- Desktop Safari/Chrome/Firefox (touch-enabled)

---

Part of the **Keystone Apps** portfolio. Undercutting the subscription-heavy App Store with free, open PWAs.
