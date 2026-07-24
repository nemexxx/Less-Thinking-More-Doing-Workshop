# Less Overthinking, More Doing

The website for **Emely Junker's improvisation workshops** — hands-on, high-energy sessions that help people speak up before they overthink.

**→ [nemexxx.github.io/Less-Thinking-More-Doing-Workshop](https://nemexxx.github.io/Less-Thinking-More-Doing-Workshop/)**

Available in [English](https://nemexxx.github.io/Less-Thinking-More-Doing-Workshop/) and [German](https://nemexxx.github.io/Less-Thinking-More-Doing-Workshop/index-de.html).

![Emely hosting an improvisation workshop](images/emely-hero.jpg)

---

## About the workshops

Over 150 people have taken part so far. The workshops are built around one idea: you get braver by *doing*, not by planning to do. Every exercise is designed to gently push past hesitation.

Participants come away with more **confidence**, **presence**, and **creativity** — and, reliably, having laughed a lot.

Four formats are offered:

| Format | Group size | Duration |
| --- | --- | --- |
| 💼 Companies — team connection and communication | 6 – 20 | 1 – 4 h |
| 🎓 Universities — confidence and thinking on your feet | 8 – 40 | 1.5 – 3 h |
| 🎤 Events — energizers and interactive sessions | 10 – 300 | 15 min – 1.5 h |
| 💬 Coaching — one-on-one guidance and talk prep | 1 – 2 | 1 – 3 h |

Interested in booking one? [Book a free intro call](https://calendar.google.com/calendar/u/0/appointments/schedules/AcZssZ2WiO4yMRB-0gIN2waoB3rBChMY3Ll4JwP669HHJ7pe5EtFvEsVC0qRTTPQm-5gE5IaPdjjZOkn) or email [hallo@emely-junker.de](mailto:hallo@emely-junker.de).

---

## About this repository

A deliberately simple, dependency-free static site. No build step, no framework, no package manager — just HTML, CSS and a little vanilla JavaScript, served straight from GitHub Pages.

### Built with

- **HTML & CSS** — hand-written, custom properties for theming, CSS grid and flexbox for layout
- **Vanilla JavaScript** — an `IntersectionObserver` fades sections in as you scroll
- **[Swiper](https://swiperjs.com/)** — the photo gallery carousel (loaded from a CDN)
- **[Klaro](https://klaro.org/)** — cookie consent
- **Google Calendar Appointments** — embedded booking widget
- **GitHub Pages** — hosting, deployed from `main`

### Structure

```
index.html          English landing page
index-de.html       German landing page
style.css           All styles for every page
run.py              Opens the site locally in your browser
impressum.html      Legal notice (required in Germany)
datenschutz.html    Privacy policy (GDPR)
images/             Photos from the workshops
```

### Running it locally

No install, no build. Clone it and open the file:

```bash
git clone https://github.com/nemexxx/Less-Thinking-More-Doing-Workshop.git
cd Less-Thinking-More-Doing-Workshop
python3 run.py          # or: python3 run.py de
```

`run.py` just opens `index.html` in your default browser — double-clicking the file works equally well.

To serve it over `http://` instead (closer to how GitHub Pages behaves):

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

### Making changes

Both language pages share `style.css`, so **a style change affects the English and German page at once**. When you edit copy or structure, check whether the same change is needed in `index-de.html` as well as `index.html`.

Pushing to `main` publishes to the live site automatically — usually within a minute.

---

## License

The **code** (HTML, CSS, JavaScript, `run.py`) is released under the [MIT License](LICENSE) — feel free to read it, learn from it, or reuse it.

The **content** is not: the photographs, written copy, and participant testimonials are © 2025 Emely Junker, all rights reserved. Please don't reuse them without asking.

---

## Contact

**Emely Junker** · [hallo@emely-junker.de](mailto:hallo@emely-junker.de)

[LinkedIn](https://www.linkedin.com/in/emely-marie-junker-81475a24b/) · [Blog](https://emelyjunker.substack.com) · [Photography](https://www.instagram.com/emely.junker/)
