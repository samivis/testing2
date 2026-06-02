# Design Spec — Dish Diary

> This is the design half of the project. `spec.md` says what it does; this says how it looks and sounds.
> Every choice below traces back to a reference in `day-03/design/references/`.

---

## 1. Vibe in 3 words
**warm, editorial, indulgent**

---

## 2. Color palette

| role | hex | from which reference |
|---|---|---|
| background | `#F5F0E6` | ref_7 (Fig Mint) — that warm cream/ivory page background |
| primary text | `#1A1A1A` | ref_7 — near-black headlines and body copy |
| accent (warmth) | `#C4712A` | ref_3 — the amber/golden tones of the food photography |
| action (buttons) | `#1A1A1A` | ref_7 — the solid black "Order Fig Mint" button |
| card surface | `#FFFFFF` | ref_1 (Kawaling Pinoy) — crisp white card backgrounds behind content |

---

## 3. Typography

- **Heading font:** [Playfair Display](https://fonts.google.com/specimen/Playfair+Display) — bold serifs with optional italic, matches the editorial "Introducing *Fig Mint.*" style in ref_7
- **Body font:** [Lora](https://fonts.google.com/specimen/Lora) — a warm, readable serif that pairs with Playfair and matches the editorial blog body text in ref_1
- **Labels / UI text:** `font-variant: small-caps; letter-spacing: 0.1em` — matches the "PROCESSOR / MEMORY" label style in ref_7

**CSS import:**
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Lora:wght@400;600&display=swap" rel="stylesheet">
```

**Why these:** ref_7 mixes upright bold serif with italic serif for contrast and drama — Playfair Display does exactly this. Lora keeps the body text warm and readable without going too stiff.

---

## 4. Tone & voice

Warm, enthusiastic, and specific — like a friend who is genuinely obsessed with food. Not corporate, not overly casual. Reads like a food magazine with personality.

- **Button label:** `Post this dish →`
- **Empty state:** `Your diary is empty. Go eat something worth remembering.`
- **Error message:** `Something went wrong uploading that. Try a smaller photo.`

---

## 5. Visual direction

Based on ref_7 (Fig Mint), the overall layout uses a warm cream background (`#F5F0E6`) with a lot of breathing room — generous padding, nothing cramped. Headlines are bold Playfair Display, big and confident.

Based on ref_3 (the dark moody food collage), food photos should be the hero — large, edge-to-edge on cards, slightly dark and atmospheric. The photos do the talking; the UI stays out of the way.

Based on ref_1 (Kawaling Pinoy), the blog layout is clean and editorial: white cards on the cream background, a simple header, no clutter. No sidebars, no ads, no noise.

Based on ref_7's button style, the primary action is a solid black rectangle — no rounded pill shapes, no gradients. Sharp, confident, intentional.

---

## 6. Component styles

**Buttons:**
- Background: `#1A1A1A` (solid black, from ref_7)
- Text: `#FFFFFF`, Lora or Playfair, font-weight 600
- Border radius: `4px` — slightly rounded but essentially rectangular (ref_7 uses near-square corners)
- Hover: lighten to `#3A3A3A`
- No shadows, no gradients

**Photo cards:**
- Background: `#FFFFFF`
- Border radius: `8px`
- Box shadow: `0 2px 12px rgba(0,0,0,0.08)` — subtle, not dramatic
- Photo fills the top of the card, 200px tall, `object-fit: cover`
- Caption in Lora, 0.95rem, `#1A1A1A`
- Date label in small-caps, `#C4712A`, 0.75rem

**Upload form inputs:**
- Border: `2px solid #1A1A1A` — strong, editorial (not the usual light gray)
- Border radius: `4px`
- Focus: border stays black, add `box-shadow: 0 0 0 3px rgba(196, 113, 42, 0.2)` (amber glow)
- No placeholder text that says "Enter your..."

---

## 7. Don't do this (anti-slop list)

- ❌ No blue — not a single shade. This palette is warm cream, black, and amber only.
- ❌ No rounded pill buttons (`border-radius: 999px`). Ref_7's buttons are sharp-cornered for a reason.
- ❌ No "Welcome to Dish Diary!" hero text. Let the food photos be the welcome.
- ❌ No light gray `#f5f5f5` backgrounds — the background is warm cream `#F5F0E6`, not cold gray.
- ❌ No gradient anywhere.
- ❌ No system font (Arial/Helvetica) — Playfair + Lora only.
- ❌ No box shadows bigger than `0 4px 16px` — keep it subtle.

---

## References

| file | what it is | why it made the cut |
|---|---|---|
| ref_1.png | Kawaling Pinoy food blog about page | Clean editorial layout, lots of whitespace, serif body text |
| ref_2.png | Picky Palate recipe blog | Horizontal photo grid, cheerful food blog structure |
| ref_3.jpg | Dark moody food photography collage | The vibe for food photos — atmospheric, golden, indulgent |
| ref_4.jpg | Recipe website full-page layout | Grid structure and how categories organize content |
| ref_5.png | Food delivery app (light UI) | Reference for card radius and clean minimal spacing |
| ref_6.png | Food app (dark green UI) | How bold hero sections can work with food photography |
| ref_7.png | Fig Mint product page | **Primary reference.** Dictates palette, typography, button style, and overall editorial feel |
