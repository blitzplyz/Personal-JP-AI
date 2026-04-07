# 速い Hayai — Japanese Immersion PWA

A free, open-source Japanese language learning app inspired by HayaiLearn. Built as a Progressive Web App — works on iPhone, Android, and desktop with no App Store required.

## Features

- **YouTube Player** — load any Japanese YouTube video and study alongside it
- **AI Subtitle Analysis** — paste any Japanese text and get instant breakdowns of grammar, vocabulary, and JLPT level
- **Pop-up Dictionary** — tap any character for an AI-powered explanation
- **Local Dictionary** — 256 built-in N5–N3 entries for instant offline lookups
- **SRS Flashcard Review** — spaced repetition system with Again / Hard / Good ratings
- **Vocabulary Tracker** — save words, track your progress from new → learning → known
- **Furigana Support** — toggle kana above kanji (settable in the app)
- **PWA** — add to home screen on iOS or Android, works like a native app

## Stack

- Vanilla HTML / CSS / JS — no frameworks, single file
- [Ollama](https://ollama.com) — local AI inference (runs on your own machine)
- [ngrok](https://ngrok.com) — tunnels your local Ollama to the internet so your phone can reach it
- Hosted on [Cloudflare Pages](https://pages.cloudflare.com) / [Netlify](https://netlify.com) (free tier)

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/blitzplyz/hayai.git
cd hayai
```

### 2. Install Ollama

Download from [ollama.com](https://ollama.com) and pull a model:

```bash
ollama pull qwen2.5:3b
```

### 3. Run the proxy server

The included `proxy.py` handles CORS between the PWA and Ollama:

```bash
python proxy.py
```

### 4. Tunnel with ngrok

```bash
ngrok http 8080
```

Copy the `https://xxx.ngrok-free.dev` URL and paste it into the app's Settings (⚙️).

### 5. One-click launch (Windows)

Double-click `start-hayai.bat` to start Ollama, the proxy, and ngrok all at once.

### 6. Deploy the PWA

Drag the project folder to [Cloudflare Pages](https://pages.cloudflare.com) or [Netlify](https://netlify.com). Both are free.

Then on your phone:
- **iPhone** — open the URL in Safari → Share → Add to Home Screen
- **Android** — open in Chrome → menu → Add to Home Screen

## Usage

1. Open the app on your phone
2. Tap ⚙️ → paste your ngrok URL → Save
3. **Player tab** — paste a YouTube URL to load a video, type Japanese text below to analyze it
4. **Review tab** — SRS flashcard review of your saved words
5. **Vocab tab** — all saved words with select/delete management
6. **Dictionary tab** — instant local lookup or AI-powered deep lookup

## Project Structure

```
hayai/
├── index.html          # Entire app (single file)
├── proxy.py            # Python CORS proxy for Ollama
├── start-hayai.bat     # Windows one-click launcher
├── manifest.json       # PWA manifest
├── sw.js               # Service worker (offline support)
├── icon-192.png        # App icon
├── icon-512.png        # App icon (large)
└── apple-touch-icon.png
```

## Why Ollama?

Hayai runs AI inference locally on your own GPU — no API keys, no usage limits, no cost. Your data never leaves your machine.

Tested with `qwen2.5:3b` on an RTX 4060 8GB. Any Ollama-compatible model works.

## License

MIT — see [LICENSE](LICENSE)

---

Built by Ahmed • Inspired by [HayaiLearn](https://hayailearn.com)
