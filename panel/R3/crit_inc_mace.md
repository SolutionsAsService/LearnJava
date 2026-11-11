# R3 Critic: Inclusion (Mace)

- Anchor used: The Principles of Universal Design (Mace et al.), Principle 4, Perceptible Information: the state you act on must show in every mode.
- Observed: real Tab presses (Playwright, 390 and 1280px; light, dark, forced-colors). `.layer a:focus-visible` uses `outline-offset:-5px`, so the ring sits on the layer fill, and `.glass` `clip-path` cuts off its sides. Only two horizontal lines remain, which read as layer rims. Ring against fill: light caramel 2.24, espresso 2.22; dark foam 1.93, milk 1.35, caramel 1.27. `.start` ring (outset, on the page): 5.77 light, 8.12 dark. Menu ring `--crema`: 7.00 light, 8.82 dark. Targets: layers 58 to 78px, menu rows 44 to 52px, start 203x48. Lowest text: caramel 5.73; chalkboard `.mn` 7.00, `.mp` 8.19. Forced colors: the clip is lifted, every layer has a border, and every ring is a full box.
- Findings:
  - F1 [defect] The focus ring inside the glass is below 3:1 on 2 of 4 layers (light) and 3 of 4 (dark), and the clip cuts its sides off: a ring nobody can see.
  - F2 [claim] Targets, 2.5.8 spacing, the start and menu rings and chalkboard contrast pass.
  - F3 [claim] Forced colors works for the glass, the menu and the start pill. No motion.
- Verdict: OBJECT
- Requested change: F1: on `.layer a:focus-visible`, use a two-tone ring (`outline:3px solid var(--ink)` plus `box-shadow:inset 0 0 0 6px var(--foam)`), or set `.glass:focus-within{clip-path:none}` so the sides survive. F2, F3: none.
