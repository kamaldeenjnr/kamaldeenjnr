"""Draws assets/safewatch-architecture-{light,dark}.svg (run: python tools/safewatch_diagram.py)."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
THEMES = {
    "light": dict(bg="#ffffff", fg="#0C203B", sub="#57606a", line="#d0d7de", box="#f6f8fa", core="#0C203B",
                  core_fg="#ffffff", core_sub="#AFC0D6", red="#C4412B", red_bg="#FBE9E5"),
    "dark": dict(bg="#0d1117", fg="#e6edf3", sub="#9198a1", line="#30363d", box="#161b22", core="#1C3A63",
                 core_fg="#ffffff", core_sub="#AFC0D6", red="#F08A74", red_bg="#2b1714"),
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(t):
    W, H = 960, 560
    o = []
    add = o.append

    def box(x, y, w, h, title, sub=None, fill=None, stroke=None, tc=None, sc=None, mono_title=False):
        add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill or t["box"]}" stroke="{stroke or t["line"]}"/>')
        ff = MONO if mono_title else SANS
        add(f'<text x="{x+14}" y="{y+(24 if sub else h/2+5)}" font-family="{ff}" font-size="14" font-weight="600" fill="{tc or t["fg"]}">{esc(title)}</text>')
        if sub:
            for i, line in enumerate(sub if isinstance(sub, list) else [sub]):
                add(f'<text x="{x+14}" y="{y+44+i*17}" font-family="{SANS}" font-size="12.5" fill="{sc or t["sub"]}">{esc(line)}</text>')

    def arrow(x1, y1, x2, y2, col=None, dash=False, label=None, lx=None, ly=None):
        col = col or t["sub"]
        d = ' stroke-dasharray="4 4"' if dash else ''
        add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="1.4"{d} marker-end="url(#a-{col[1:]})"/>')
        if label:
            add(f'<text x="{lx}" y="{ly}" font-family="{MONO}" font-size="11" fill="{col}">{esc(label)}</text>')

    def head(x, y, s):
        add(f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="11" letter-spacing="1.5" fill="{t["sub"]}">{esc(s)}</text>')

    markers = "".join(f'<marker id="a-{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>'
                      for c in {t["sub"], t["red"]})
    add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
        f'aria-label="SafeWatch architecture: an SOS from the Android app, browser app, SMS or a USSD dial code reaches a FastAPI and PostgreSQL server, which sends it to the on-duty responder, then the backup and coordinator if nobody accepts, and to the nearest responder sharing their location. A dispatch screen handles the alert. Trip check-ins, hourly storm warnings and an audit log run alongside.">')
    add(f'<defs>{markers}</defs><rect width="{W}" height="{H}" rx="10" fill="{t["bg"]}" stroke="{t["line"]}"/>')

    # column 1: ways in
    head(28, 40, "1  REPORT FROM ANY PHONE")
    ins = [("Android app", "one-tap SOS with GPS"), ("Browser app", "installs from a link"),
           ("SMS", "when there is no data"), ("USSD dial code", "phones without internet")]
    for i, (a, b) in enumerate(ins):
        y = 56 + i * 66
        box(28, y, 196, 54, a, b)
        arrow(224, y + 27, 300, 170 + 0, t["sub"])

    # column 2: core
    head(300, 40, "2  SERVER")
    box(300, 120, 220, 112, "FastAPI · PostgreSQL", ["alert stored with location", "and the reporter's choice:", "drowning, boat, missing, other"],
        fill=t["core"], stroke=t["core"], tc=t["core_fg"], sc=t["core_sub"])
    add(f'<text x="300" y="262" font-family="{MONO}" font-size="11.5" fill="{t["red"]}">saved → sent → received → accepted</text>')
    add(f'<text x="300" y="280" font-family="{SANS}" font-size="12" fill="{t["sub"]}">a named person must accept it</text>')

    # column 3: escalation
    head(580, 40, "3  ESCALATE UNTIL ACCEPTED")
    chain = [("On-duty responder", "for that stretch of water"), ("Backup responder", None), ("Coordinator", None)]
    ys = [56, 150, 228]
    for (a, b), y in zip(chain, ys):
        box(580, y, 210, 54 if b else 44, a, b)
    arrow(520, 160, 578, 83, t["red"])
    arrow(685, 110, 685, 148, t["red"], label="no answer in time", lx=693, ly=134)
    arrow(685, 194, 685, 226, t["red"], label="still no answer", lx=693, ly=214)
    box(580, 296, 210, 54, "Nearest responder", "sharing their location")
    arrow(520, 200, 578, 322, t["sub"], dash=True)

    # column 4: dispatch
    head(816, 40, "4  RESPOND")
    box(816, 120, 118, 112, "Dispatch", ["accept", "nearest landing", "same-accident", "check"])
    arrow(790, 83, 814, 150, t["sub"])

    # bottom: jobs that run alongside
    add(f'<line x1="28" y1="384" x2="{W-28}" y2="384" stroke="{t["line"]}"/>')
    head(28, 412, "RUNNING ALONGSIDE")
    jobs = [("Trip check-in", ["fisher sets a return time;", "no check-in → alert with", "last known position"]),
            ("Storm warnings", ["forecast checked hourly;", "draft in Ewe, Twi, English", "for staff to send by SMS"]),
            ("Audit log", ["every step recorded with", "who did it and when, for", "partner and funder reports"])]
    for i, (a, b) in enumerate(jobs):
        box(28 + i * 302, 426, 290, 104, a, b)
    arrow(126, 426, 306, 236, t["red"], dash=True)
    add("</svg>")
    return "\n".join(o)


if __name__ == "__main__":
    for name, t in THEMES.items():
        (OUT / f"safewatch-architecture-{name}.svg").write_text(build(t), encoding="utf-8")
    print("written")
