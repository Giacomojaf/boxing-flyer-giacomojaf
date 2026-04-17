from PIL import Image, ImageDraw, ImageFont
import subprocess
import os

W, H = 1080, 1920
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

def font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/ArialHB.ttc",
        "/System/Library/Fonts/Arial.ttf",
    ]
    for f in candidates:
        if os.path.exists(f):
            try:
                return ImageFont.truetype(f, size)
            except:
                pass
    return ImageFont.load_default()

BLUE     = (126, 200, 255, 255)
WHITE    = (255, 255, 255, 255)
LBLUE    = (200, 232, 255, 220)
DBLUE_BG = (10, 40, 120, 190)
DARK_BG  = (20, 20, 40, 190)
CTA_BG   = (26, 101, 214, 240)

# ── ACCENT LINE ──
draw.rectangle([65, 0, 68, H], fill=(58, 143, 255, 115))

# ── GLOW BAR BOTTOM ──
draw.rectangle([0, H-14, W, H], fill=(30, 96, 204, 230))

# ── LOCATION ──
draw.text((108, 85), "● ZÜRICH ALTSTETTEN  ·  5 MIN VOM BAHNHOF ALTSTETTEN", font=font(28), fill=WHITE)

# ── HOOK ──
draw.text((108, 155), "Therapie war gestern. 🥊", font=font(46), fill=LBLUE)
draw.text((108, 210), "Zwei Wege. Ein Ziel.", font=font(46), fill=LBLUE)

# ── OPEN GYM CARD ──
draw.rounded_rectangle([55, 300, 1025, 900], radius=18, fill=DBLUE_BG, outline=BLUE, width=2)
draw.text((108, 320), "OPEN GYM", font=font(96, bold=True), fill=WHITE)
draw.text((108, 410), "IN ALTSTETTEN", font=font(96, bold=True), fill=BLUE)
draw.text((108, 515), "Die beste Stunde deines Arbeitstages.", font=font(30), fill=LBLUE)

# Days
for i, day in enumerate(["Mo", "Mi", "Fr"]):
    x = 108 + i * 145
    draw.rounded_rectangle([x, 565, x+120, 625], radius=8, fill=(58, 143, 255, 100), outline=BLUE, width=2)
    draw.text((x+22, 570), day, font=font(44, bold=True), fill=WHITE)
draw.text((560, 570), "11–13 Uhr", font=font(44, bold=True), fill=WHITE)

draw.text((108, 645), "✓  Ring & Sandsäcke inklusive", font=font(29), fill=WHITE)
draw.text((108, 685), "✓  Solo · Sparring · Free Use", font=font(29), fill=WHITE)
draw.text((108, 725), "✓  Anfänger willkommen", font=font(29), fill=WHITE)
draw.text((108, 770), "⚠  Bitte vorher per DM anmelden", font=font(29), fill=BLUE)
draw.text((108, 820), "AB CHF 30.– / SESSION", font=font(50, bold=True), fill=BLUE)

# ── 1:1 CARD ──
draw.rounded_rectangle([55, 920, 1025, 1330], radius=18, fill=DARK_BG, outline=(255,255,255,50), width=2)
draw.text((108, 940), "1:1", font=font(100, bold=True), fill=WHITE)
draw.text((108, 1030), "TRAINING", font=font(100, bold=True), fill=BLUE)
draw.text((108, 1140), "Dein Trainer. Dein Tempo. Dein Ort.", font=font(30), fill=LBLUE)
draw.text((108, 1185), "✓  Im Gym, draussen oder online", font=font(29), fill=WHITE)
draw.text((108, 1225), "✓  Alle Level – flexibel buchbar", font=font(29), fill=WHITE)
draw.text((108, 1275), "→  Preis auf Anfrage – einfach DM", font=font(32, bold=True), fill=BLUE)

# ── CTA BOX ──
draw.rounded_rectangle([55, 1355, 1025, 1530], radius=16, fill=CTA_BG, outline=BLUE, width=2)
draw.text((200, 1370), "PLÄTZE BEGRENZT — JETZT SICHERN", font=font(26), fill=LBLUE)
draw.text((100, 1415), "DM @giacomojaf FÜR TERMIN", font=font(62, bold=True), fill=WHITE)

out = "/Users/giacomolarocca/Downloads/claudecodetest/overlay.png"
img.save(out)
print(f"Saved: {out}")
