#!/usr/bin/env python3
"""Build the short /n/<slug>/ landing pages the printed QR codes point at.

The codes on the poster and the hand-out cards encode jfc-mit.github.io/n/<slug>/
rather than a CDN or raw URL. Two reasons:

  * short URL -> 29-module symbol instead of 41, which is what makes a 24mm code
    on a business card scannable;
  * the destination stays editable after the paper is printed. If a host stops
    rendering PDFs on some phone, fix it here — the printed code is unchanged.

Each page offers the note explicitly rather than auto-redirecting: a phone that
refuses to render application/pdf inline (Chrome on Android is inconsistent
about this) still shows a page with a working link instead of a blank viewer.
"""
from pathlib import Path

HERE = Path(__file__).parent

# slug -> (English title, Portuguese title, pages, repo, branch, path)
NOTES = {
    "lund": ("ALEPH — Lund jet plane", "ALEPH — plano de Lund", 57,
             "analysis_aleph_lund_plane", "master",
             "phase5_documentation/outputs/ANALYSIS_NOTE_5_v1.pdf"),
    "zlineshape": ("ALEPH — Z lineshape", "ALEPH — lineshape do Z", 50,
                   "analysis_aleph_z_lineshape", "master",
                   "phase5_documentation/outputs/ANALYSIS_NOTE_5_v1.pdf"),
    "heavyflavour": ("ALEPH — heavy flavour", "ALEPH — sabores pesados", 48,
                     "analysis_aleph_z_heavy_flavour", "master",
                     "phase5_documentation/outputs/ANALYSIS_NOTE_5_v1.pdf"),
    "eec": ("ALEPH — energy–energy correlators", "ALEPH — correlacionadores EEC", 56,
            "analysis_aleph_eec_correlators", "main",
            "phase4_inference/4c_observed/outputs/ANALYSIS_NOTE_4c_v1.pdf"),
    "alphas": ("ALEPH — event shapes, α_s", "ALEPH — event shapes, α_s", 47,
               "analysis_aleph_eventshapes_alphas", "main",
               "phase5_documentation/outputs/ANALYSIS_NOTE_5_v1.pdf"),
    "htautau": ("CMS — H → τ⁺τ⁻ signal strength", "CMS — intensidade do sinal H → τ⁺τ⁻", 75,
                "analysis_cms_higgs_tautau", "master",
                "phase5_documentation/outputs/ANALYSIS_NOTE_5_v2.pdf"),
}

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_en} — JFC analysis note</title>
<meta name="description" content="{pages}-page agent-written, agent-reviewed analysis note: {title_en}.">
<link rel="icon" type="image/png" href="../../images/favicon.png">
<style>
  :root{{ color-scheme: light; }}
  *{{ margin:0; padding:0; box-sizing:border-box; }}
  body{{ font-family:'IBM Plex Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
    background:#fff; color:#131417; line-height:1.5;
    display:flex; min-height:100vh; align-items:center; justify-content:center; padding:2rem 1.25rem; }}
  .card{{ width:100%; max-width:32rem; min-width:0; }}
  .eyebrow{{ font-size:.63rem; letter-spacing:.12em; color:#6B7280; text-transform:uppercase;
    border-top:1px solid #131417; padding-top:.6rem; display:flex; justify-content:space-between;
    gap:.75rem; flex-wrap:wrap; }}
  h1{{ font-family:ui-sans-serif,system-ui,sans-serif; font-weight:650; font-size:1.45rem; overflow-wrap:anywhere;
    line-height:1.15; letter-spacing:-.02em; margin:1.4rem 0 .4rem; }}
  .meta{{ font-size:.8rem; color:#6B7280; }}
  .meta b{{ color:#D24A33; font-weight:600; }}
  .meta .pt{{ display:block; font-size:.72rem; opacity:.85; }}
  .btns{{ display:flex; flex-direction:column; gap:.65rem; margin:1.8rem 0 1.2rem; }}
  a.btn{{ display:block; text-align:center; text-decoration:none; padding:.8rem .9rem;
    border:1px solid #131417; color:#131417; font-size:.86rem; overflow-wrap:anywhere; }}
  a.btn .pt{{ display:block; font-size:.72rem; opacity:.8; margin-top:.15rem; }}
  a.btn.primary{{ background:#131417; color:#fff; }}
  .foot{{ font-size:.72rem; color:#6B7280; border-top:1px solid #D9D9D4; padding-top:.8rem;
    display:flex; justify-content:space-between; gap:1rem; flex-wrap:wrap; }}
  .foot a{{ color:#6B7280; }}
</style>
</head>
<body>
  <div class="card">
    <div class="eyebrow"><span>JFC — Just Furnish Context</span><span>arXiv:2603.20179</span></div>
    <h1>{title_en}</h1>
    <div class="meta"><b>{pages} pages</b> · agent-written, agent-reviewed<span class="pt" lang="pt-BR">{pages} páginas, escritas e revisadas pelo agente</span></div>
    <div class="btns">
      <a class="btn primary" href="{pdf}">Open the analysis note (PDF)<span class="pt" lang="pt-BR">Abrir a nota de análise (PDF)</span></a>
      <a class="btn" href="https://github.com/jfc-mit/{repo}">Repository on GitHub<span class="pt" lang="pt-BR">Repositório no GitHub</span></a>
    </div>
    <div class="foot">
      <span><a href="/">jfc-mit.github.io</a> · <a href="/pt/" lang="pt-BR">versão em português</a></span>
      <span>ICHEP 2026 · Natal</span>
    </div>
  </div>
</body>
</html>
"""


def main():
    for slug, (en, pt, pages, repo, branch, path) in NOTES.items():
        pdf = f"https://cdn.jsdelivr.net/gh/jfc-mit/{repo}@{branch}/{path}"
        out = HERE / "n" / slug
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(
            PAGE.format(title_en=en, title_pt=pt, pages=pages, repo=repo, pdf=pdf))
        print(f"n/{slug}/  -> {repo}")
    print(f"{len(NOTES)} note pages written")


if __name__ == "__main__":
    main()
