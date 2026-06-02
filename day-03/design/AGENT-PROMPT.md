
  # Design Spec Agent Prompt

  Copy and paste the prompt below into Replit Agent after you've saved your design references into the `references/` folder next to this file.

  There's also a fill-in template at `day-03/design-spec-template.md` if you'd rather draft the spec by hand (or have Agent fill the template in).

  ---

  ## The prompt

  > Look at all the files in `day-03/design/references/`. These are my design inspirations — screenshots of apps I like, color palettes, font choices, and visual references.
  >
  > Based on these references, create a `design-spec.md` file in my project root with:
  >
  > 1. **Color palette** — 4–5 colors with hex codes. For each color, say what it's for (background, primary action, accent, text, etc.) and which reference image inspired it.
  >
  > 2. **Typography** — a heading font and a body font from Google Fonts. Include the CSS import link. Say why you picked them based on my references.
  >
  > 3. **Tone and voice** — how the app talks to the user. Is it casual and friendly? Minimal and direct? Warm and encouraging? Base this on the copy style in my reference apps.
  >
  > 4. **Visual direction** — describe the overall look and feel. Reference specific images I saved: "Based on your Spotify screenshot, we're going with dark backgrounds and bright accent colors" or "Based on your Coolors palette, we're using warm earth tones."
  >
  > 5. **Component styles** — what buttons, cards, and inputs should look like. Border radius, shadows, hover states. Keep it consistent.
  >
  > 6. **Don't do this** — a short anti-slop list of things to avoid (generic blue gradients, "Welcome to your dashboard" headers, anything that doesn't trace to my references).
  >
  > Make the design spec specific enough that any AI agent could read it and build a consistent-looking app from it. No generic suggestions — every choice should trace back to one of my references.

  ---

  ## After the design spec is created

  Review it. If something doesn't match your vibe, tell Agent:

  - *"The palette is too bright — I want something more muted like the [app name] screenshot"*
  - *"Change the heading font to [specific font]"*
  - *"The tone should be more [casual/minimal/playful] — look at how [app] writes their button labels"*

  Once you're happy with it, save `design-spec.md` in your project root next to `spec.md`. **You won't build the app today.** On Day 4 you'll hand both `spec.md` and `design-spec.md` to Replit Agent and it will build your v1 from the two of them together.
  