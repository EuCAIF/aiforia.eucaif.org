#!/usr/bin/env python3
"""Generate the AIFORIA logo draft SVGs into design/logo/. Run: python3 design/make-logo.py

The logo is a proposal under discussion and is not used on the website.

Two parents: the letters follow the COST wordmark (heavy monoline strokes, squared shapes
with rounded corners, flat stroke ends); the central O is the EuCAIF emblem reduced to its
starry blue disc with one orbit, and the I is the emblem's lowercase i with a round dot.
"""
import math, os
OUT = os.path.join(os.path.dirname(__file__), 'logo')   # drafts only; not published with the site
NAVY, WHITE, CORAL = '#1b1f4b', '#ffffff', '#e0523f'
STROKE = 20      # stroke weight on a 100-unit cap height
R = 18           # centre-line corner radius

STARS = [(38,52,1.3),(58,30,0.9),(150,34,1.1),(163,58,1.5),(170,96,1.0),(160,120,1.6),(30,104,1.0),
         (44,132,1.3),(134,22,0.8),(72,18,1.0),(22,76,0.8),(176,74,0.8),(88,186,0.9),(118,176,1.1),
         (104,164,0.7),(96,58,1.0),(84,118,1.2),(122,96,0.9),(112,140,1.0),(70,84,0.8)]

def orb(uid='o', rim=None):
    """Starry blue disc with one orbit and a coral electron, in a 200x200 box."""
    stars = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in STARS)
    rx, ry, rot, t = 74, 28, math.radians(-24), math.radians(-14)
    ex, ey = rx*math.cos(t), ry*math.sin(t)
    px, py = 100 + ex*math.cos(rot) - ey*math.sin(rot), 100 + ex*math.sin(rot) + ey*math.cos(rot)
    ring = f'<circle cx="100" cy="100" r="96.5" fill="none" stroke="{rim}" stroke-width="3"/>' if rim else ''
    return f'''<defs>
    <radialGradient id="{uid}g" gradientUnits="userSpaceOnUse" cx="100" cy="92" r="112">
      <stop offset="0" stop-color="#2a9be0"/><stop offset="0.42" stop-color="#1273bd"/>
      <stop offset="0.78" stop-color="#0a3470"/><stop offset="1" stop-color="#051531"/>
    </radialGradient>
  </defs>
  <circle cx="100" cy="100" r="98" fill="url(#{uid}g)"/>
  <g fill="{WHITE}" opacity="0.9">{stars}</g>
  <ellipse cx="100" cy="100" rx="{rx}" ry="{ry}" transform="rotate(-24 100 100)" fill="none" stroke="{WHITE}" stroke-opacity="0.88" stroke-width="6"/>
  <circle cx="{px:.1f}" cy="{py:.1f}" r="10.5" fill="{CORAL}" stroke="{WHITE}" stroke-width="3"/>
  {ring}'''

# Letters as centre-line paths (local x starts at 0; stroke adds 10 on each side).
LETTER_A = f'M10 100 V{10+R} a{R} {R} 0 0 1 {R} -{R} H{74-R} a{R} {R} 0 0 1 {R} {R} V100 M10 64 H74'      # 84 wide
LETTER_F = f'M10 100 V{10+R} a{R} {R} 0 0 1 {R} -{R} H66 M10 56 H56'                                    # 66 wide
LETTER_R = f'M10 100 V{10+R} a{R} {R} 0 0 1 {R} -{R} H52 a22 22 0 0 1 0 44 H10 M40 54 H52 a{R} {R} 0 0 1 {R} {R} V100'  # 84 wide
def stroke_path(d, x, ink):
    return f'<path transform="translate({x} 0)" d="{d}" fill="none" stroke="{ink}" stroke-width="{STROKE}" stroke-linejoin="round"/>'
def letter_i(x, ink):
    return f'<rect x="{x}" y="38" width="{STROKE}" height="62" fill="{ink}"/><circle cx="{x+10}" cy="12" r="12" fill="{ink}"/>'

GAP = 16
def wordmark(ink, rim=None):
    x = 0; parts = []
    parts.append(stroke_path(LETTER_A, x, ink)); x += 84 + GAP
    parts.append(letter_i(x, ink));              x += 20 + GAP
    parts.append(stroke_path(LETTER_F, x, ink)); x += 66 + GAP - 2
    parts.append(f'<g transform="translate({x} -8) scale(0.58)">{orb(rim=rim)}</g>'); x += 116 + GAP - 2
    parts.append(stroke_path(LETTER_R, x, ink)); x += 84 + GAP
    parts.append(letter_i(x, ink));              x += 20 + GAP
    parts.append(stroke_path(LETTER_A, x, ink)); x += 84
    return '\n  '.join(parts), x

def svg(viewbox, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" role="img" aria-label="AIFORIA">\n'
            f'  <title>AIFORIA</title>\n  {body}\n</svg>\n')
def logo(ink, rim=None):
    body, width = wordmark(ink, rim)
    return svg(f'-8 -14 {width + 16} 128', body)

files = {
    'aiforia-logo.svg': logo(NAVY),
    'aiforia-logo-inverse.svg': logo(WHITE, rim=WHITE),
    'aiforia-mark.svg': svg('0 0 200 200', orb()),
}
for name, content in files.items():
    open(os.path.join(OUT, name), 'w').write(content)
print('\n'.join(sorted(files)))
