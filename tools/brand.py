#!/usr/bin/env python3
"""brand.py - Talent Social brand tokens and font loading for the kit's drawing tools.

Source of the values: the live site talentsocial.network (measured 22 Oct 2026) and the team's confirmed
type preferences (NTS Edits/_toolkit/LEARNINGS.md). `IDENTITY.md` section 6 explains the choices.
Not for logins or secrets; no media.
"""
import os, sys

try:
    from PIL import ImageFont
except ImportError:
    sys.exit("brand.py: Pillow is missing. Use $STT_PYTHON or `pip install pillow`.")

# colours (hex, no #)
INK = "131210"          # warm black (site page background)
PANEL = "191715"        # warm black, raised
PANEL2 = "1E1C1A"
OFFWHITE = "F6F5F4"
MUTED = "A9A39E"
GOLD = "D8B579"         # site text accent: payoff phrase, eyebrow
GOLD_VIDEO = "E2B05A"   # site button fill; use for small gold text over moving footage (more legible)
ON_GOLD = "181410"      # dark text on a gold button


def rgb(hexstr, a=None):
    t = tuple(int(hexstr.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    return t + (a,) if a is not None else t


SEARCH = [os.environ.get("TS_FONT_DIR", ""), os.path.expanduser("~/.local/share/vetted-video/fonts"),
          os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")]


def find_font(name):
    """Look for a font file by name in $TS_FONT_DIR, ~/.local/share/vetted-video/fonts and tools/fonts."""
    for d in SEARCH:
        p = os.path.join(d, name) if d else ""
        if p and os.path.isfile(p):
            return p
    sys.exit(f"brand.py: font '{name}' not found. Put the open-licence Inter Tight files "
             "(InterTight[wght].ttf and InterTight-Italic[wght].ttf from Google Fonts) in $TS_FONT_DIR or "
             "~/.local/share/vetted-video/fonts. See CONFIG.md.")


def load(path, size, weight=600):
    """Open a font. A variable font (file name has [wght]) is set to `weight`."""
    f = ImageFont.truetype(path, int(round(size)))
    if "[wght]" in os.path.basename(path):
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f


def inter(size, weight=600, italic=False):
    return load(find_font("InterTight-Italic[wght].ttf" if italic else "InterTight[wght].ttf"), size, weight)


def payoff(size, face=None):
    """Gold payoff face. Instrument Serif Italic (open licence, Google Fonts; files in the font folders) when present,
    else Didot Italic on macOS (the team's confirmed taste), else Inter Tight Italic. `face` forces one: "instrument" or "didot"."""
    if face != "didot":
        for d in SEARCH:
            p = os.path.join(d, "InstrumentSerif-Italic.ttf") if d else ""
            if p and os.path.isfile(p):
                return ImageFont.truetype(p, int(round(size * 1.12)))      # drawn a little smaller than Didot at the same size
    p = "/System/Library/Fonts/Supplemental/Didot.ttc"
    if face != "instrument" and os.path.isfile(p):
        try:
            return ImageFont.truetype(p, int(round(size)), index=1)
        except Exception:
            pass
    return inter(size, 500, italic=True)


def payoff_stroke(default=1):
    """Instrument Serif is heavy enough to read on video as it is; Didot's hairlines need a 1 to 2 px stroke."""
    for d in SEARCH:
        if d and os.path.isfile(os.path.join(d, "InstrumentSerif-Italic.ttf")):
            return 0
    return default
