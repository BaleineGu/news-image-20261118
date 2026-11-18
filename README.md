[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/BaleineGu/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/BaleineGu/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

# Wednesday 18 November 2026: 36 stories, 6 continents, one front page and a map

Entry for the make.fun bounty `news-image-20261118` (deadline
2026-11-20 00:00 UTC), by @guinrm. Version 2 — a rebuild of the
six-story v1 as a full newspaper front page, following the pattern
of the competition's winning entries: more stories, a map, a numbers
strip and a sources footer.

## The image

A 1024×1024 front page, "WORLD NEWS — 18 NOVEMBER 2026", covering
**36 real stories** from Wednesday 18 November 2026, all checked
against same-day reporting:

- **3 illustrated leads:** Gulf strikes (US hits Qeshm Island; Iran
  answers with drones at US bases in Bahrain and Kuwait), the Kerch
  Bridge hit, and the Shenzhen summit (Xi hosts Putin; Trump flies
  in for APEC ahead of Thursday's first-ever trilateral summit).
- **6 more illustrated stories:** US loses measles-free status,
  Ebola surge in DR Congo, Cyclone Xavier, Peltola wins Alaska,
  Dhoni retires, QUAD unveils its plan in Manila.
- **BY THE NUMBERS strip:** S&P 500 7,341 ▼1.03%, Brent $92.47
  ▼0.72%, gold ▼2.05%, 5,400+ measles cases, 11,000+ Ebola cases,
  315 km/h cyclone gusts.
- **A dotted world map** with numbered dots for stories 1–9.
- **"ALSO ON WEDNESDAY 18 NOVEMBER — 27 MORE STORIES"**, a numbered
  list taking the total to 36: APEC, ASEAN, the Myanmar genocide
  ruling, Gaza, Israel's government, Rwanda return hubs, Sozcu TV,
  French protests, the Houthis, the Siberia plane crash, Cyclone
  Akvan, Nvidia, the NSA outages, the BBC/IKEA cyberattack,
  Anthropic's Nasdaq listing, the PNG magnitude 6.0 quake, and more.
- **Sources footer:** Reuters · AP · Al Jazeera · BBC · CNN · FT ·
  IMD · NASA · UN · UEFA · ESPNcricinfo, with the line "Disputed
  claims are attributed."

Every scene is drawn with code (no photographs, no real flags), and
all wording is typeset in fixed fonts, so no label is garbled. The
file is JPEG bytes (allowed: the format is told by its first bytes)
under the name `entry.png`, 265,517 bytes, within the 1 MiB /
1024×1024 gate.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, defaulting to
`/output/entry.png`, and checks the copy's size. Running it twice
writes identical bytes.

## License

MIT — see `LICENSE`.
