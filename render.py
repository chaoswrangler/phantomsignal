#!/usr/bin/env python3
"""
Render the agent's markdown brief into a published HTML page.

Usage:
    python render.py briefs/2026-05-11.md

Expects:
    briefs/YYYY-MM-DD.md  - the agent's markdown output
Produces:
    docs/index.html       - latest brief, styled
    docs/briefs/YYYY-MM-DD.html  - archived copy
    docs/briefs/index.html       - archive index
"""

import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import markdown
except ImportError:
    print("Run: pip install markdown", file=sys.stderr)
    sys.exit(1)


STYLE = """
:root {
  --bg: #0f0e0c;
  --paper: #f6f1e8;
  --ink: #1a1814;
  --ink-soft: #4a4640;
  --accent: #c8442a;
  --rule: #2a2622;
  --rule-soft: #d8d0c2;
  --sev-1: #6b8e6b;
  --sev-2: #a8a060;
  --sev-3: #c89040;
  --sev-4: #c8662a;
  --sev-5: #a83020;
}

* { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: "Charter", "Iowan Old Style", "Georgia", serif;
  font-size: 17px;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

.masthead {
  background: var(--bg);
  color: var(--paper);
  padding: 2rem 0 2.5rem;
  border-bottom: 6px double var(--paper);
}

.masthead-inner {
  max-width: 780px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.masthead .eyebrow {
  font-family: "JetBrains Mono", "SF Mono", "Consolas", monospace;
  font-size: 0.72rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.75rem;
}

.masthead h1 {
  font-family: "Playfair Display", "Didot", "Bodoni 72", serif;
  font-weight: 900;
  font-size: clamp(2rem, 5vw, 3.2rem);
  line-height: 1.05;
  letter-spacing: -0.02em;
  margin: 0 0 0.5rem;
}

.masthead .dateline {
  font-family: "JetBrains Mono", "SF Mono", "Consolas", monospace;
  font-size: 0.78rem;
  letter-spacing: 0.05em;
  color: rgba(246, 241, 232, 0.7);
}

.content {
  max-width: 780px;
  margin: 0 auto;
  padding: 3rem 1.5rem 5rem;
}

.content h1 { display: none; } /* the rendered H1 is replaced by masthead */

.content h2 {
  font-family: "Playfair Display", "Didot", serif;
  font-weight: 800;
  font-size: 1.65rem;
  line-height: 1.2;
  letter-spacing: -0.01em;
  margin: 3rem 0 0.5rem;
  padding-top: 2rem;
  border-top: 1px solid var(--rule-soft);
}

.content h2:first-of-type {
  border-top: none;
  padding-top: 0;
  margin-top: 0;
}

.content h3 {
  font-family: "JetBrains Mono", "SF Mono", monospace;
  font-size: 0.72rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 700;
  margin: 2rem 0 0.5rem;
}

.content p {
  margin: 0.75rem 0;
}

.content p strong:first-child {
  font-family: "JetBrains Mono", "SF Mono", monospace;
  font-size: 0.78rem;
  letter-spacing: 0.05em;
}

.content ul {
  list-style: none;
  padding-left: 0;
  margin: 0.75rem 0;
}

.content ul li {
  position: relative;
  padding-left: 1.5rem;
  margin: 0.55rem 0;
}

.content ul li::before {
  content: "›";
  position: absolute;
  left: 0;
  top: 0;
  color: var(--accent);
  font-weight: 700;
}

.content li strong:first-child {
  color: var(--ink);
  font-weight: 700;
}

.content a {
  color: var(--ink);
  text-decoration: underline;
  text-decoration-color: var(--accent);
  text-decoration-thickness: 1px;
  text-underline-offset: 3px;
}

.content a:hover {
  background: var(--accent);
  color: var(--paper);
  text-decoration: none;
}

.content hr {
  border: none;
  border-top: 1px solid var(--rule-soft);
  margin: 2.5rem 0 0;
}

.content code {
  font-family: "JetBrains Mono", "SF Mono", monospace;
  background: rgba(200, 68, 42, 0.08);
  padding: 0.1em 0.35em;
  border-radius: 2px;
  font-size: 0.88em;
}

/* Severity metadata row */
.content p:has(> strong:first-child:nth-of-type(1)) {
  /* Lightweight: metadata rows just get tighter spacing */
}

.archive-link {
  font-family: "JetBrains Mono", monospace;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ink-soft);
  margin-top: 4rem;
  padding-top: 2rem;
  border-top: 1px solid var(--rule-soft);
  display: block;
  text-decoration: none;
}

.archive-link:hover { color: var(--accent); }

/* Archive index */
.archive-list {
  list-style: none;
  padding: 0;
}

.archive-list li {
  padding: 1rem 0;
  border-bottom: 1px solid var(--rule-soft);
}

.archive-list a {
  font-family: "Playfair Display", serif;
  font-size: 1.2rem;
  text-decoration: none;
}

.archive-list a:hover { color: var(--accent); }

.archive-list .date {
  font-family: "JetBrains Mono", monospace;
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  color: var(--ink-soft);
  display: block;
  margin-bottom: 0.25rem;
}

@media (max-width: 600px) {
  body { font-size: 16px; }
  .masthead { padding: 1.5rem 0 2rem; }
  .content { padding: 2rem 1.25rem 4rem; }
  .content h2 { font-size: 1.4rem; }
}
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>{style}</style>
</head>
<body>
<header class="masthead">
  <div class="masthead-inner">
    <div class="eyebrow">PHANTOMSignal Brief · Threat signal. Not threat noise.</div>
    <h1>{display_title}</h1>
    <div class="dateline">{dateline}</div>
  </div>
</header>
<main class="content">
{body}
<a class="archive-link" href="archive.html">View archive →</a>
<a class="archive-link" href="../">← Back to PHANTOMSignal Feed</a>
</main>
</body>
</html>
"""

ARCHIVE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PHANTOMSignal Brief Archive</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>{style}</style>
</head>
<body>
<header class="masthead">
  <div class="masthead-inner">
    <div class="eyebrow">Archive</div>
    <h1>PHANTOMSignal Brief Archive</h1>
    <div class="dateline">All editions</div>
  </div>
</header>
<main class="content">
  <ul class="archive-list">
    {items}
  </ul>
  <a class="archive-link" href="index.html">← Back to latest brief</a>
  <a class="archive-link" href="../">← Back to PHANTOMSignal Feed</a>
</main>
</body>
</html>
"""


def render_brief(md_path: Path, docs_dir: Path):
    text = md_path.read_text(encoding="utf-8")

    # Extract title from first H1
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = m.group(1).strip() if m else "PHANTOMSignal Brief"
    display_title = re.sub(r"\s*—\s*\d{4}-\d{2}-\d{2}\s*$", "", title)

    # Extract dateline from italic line after H1
    m = re.search(r"^\*(.+)\*$", text, re.MULTILINE)
    dateline = m.group(1).strip() if m else ""

    html_body = markdown.markdown(
        text,
        extensions=["extra", "sane_lists", "smarty"],
    )

    page = TEMPLATE.format(
        title=title,
        display_title=display_title,
        dateline=dateline,
        body=html_body,
        style=STYLE,
    )

    # The brief lives at docs/brief/ so it doesn't collide with the
    # PHANTOMSignal Feed (the live firehose view) at docs/index.html.
    brief_dir = docs_dir / "brief"
    brief_dir.mkdir(parents=True, exist_ok=True)

    # Latest brief at docs/brief/index.html
    latest_path = brief_dir / "index.html"
    latest_path.write_text(page, encoding="utf-8")

    # Archived copy at docs/brief/YYYY-MM-DD.html
    archive_path = brief_dir / f"{md_path.stem}.html"
    archive_path.write_text(page, encoding="utf-8")

    # Regenerate archive index at docs/brief/archive.html
    briefs = sorted(brief_dir.glob("*.html"), reverse=True)
    items_html = []
    for b in briefs:
        if b.name in ("index.html", "archive.html"):
            continue
        date_str = b.stem
        try:
            d = datetime.strptime(date_str, "%Y-%m-%d")
            display = d.strftime("%A, %B %-d, %Y")
        except ValueError:
            display = date_str
        items_html.append(
            f'<li><a href="{b.name}"><span class="date">{date_str}</span>{display}</a></li>'
        )

    archive_index = ARCHIVE_TEMPLATE.format(
        style=STYLE,
        items="\n    ".join(items_html) or "<li>No briefs yet.</li>",
    )
    (brief_dir / "archive.html").write_text(archive_index, encoding="utf-8")

    print(f"Latest brief: {latest_path}")
    print(f"Archived copy: {archive_path}")
    print(f"Archive index: {brief_dir / 'archive.html'}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python render.py path/to/brief-YYYY-MM-DD.md", file=sys.stderr)
        print("Writes to docs/brief/index.html (latest) and docs/brief/YYYY-MM-DD.html (archive)", file=sys.stderr)
        sys.exit(1)
    md = Path(sys.argv[1])
    if not md.exists():
        print(f"Not found: {md}", file=sys.stderr)
        sys.exit(1)
    render_brief(md, Path("docs"))
