# Critic: Inclusion (Mace), R2

**Anchor used:** The Principles of Universal Design (Mace et al.): Principle 4, Perceptible Information, and Principle 3, Simple and Intuitive Use.

**Observed:** I pressed Tab on the home page (Playwright) at 390 and 1280, in light and dark.
- 390: nav, `.start` (y147), the six `.lg a` (y616–727), then the strip (y927). This is the visual order, so R1 F1 is fixed.
- 1280: nav, `.start`, the right-column legend (x932), then back to the left-column strip (x32, y454).
- `.start` is 120×44 / 189×44, with text at 14.6 / 15.2:1. Its offset ring is on the paper at 5.46 / 9.28:1.
- Phone destinations (`.lg-go-m`): 12px, at 5.73:1 or better. Cards: 44px or taller, 4px gap.
- Forced colours: `[aria-current]` gets a 3px LinkText border, so R1 F2 is fixed.
- Magic tiles: 5.24 / 8.33:1, so R1 F4 is fixed.

**Findings:**
- F1 [claim] At 1280, focus leaps about 900px from the right column back to the upper-left. Each column is in order, so this passes WCAG 2.4.3.
- F2 [defect] In forced colours, `.start` has no border. It renders as bare text wrapped onto three lines, with no button boundary.
- F3 [premise] The phone destinations sit exactly at the 12px floor.

**Verdict:** PASS

**Requested change:**
- F1: optionally, put the strip under the legend at 1000px and up.
- F2: add `border: 1px solid transparent` and `white-space: nowrap` to `.start`.
- F3: none.
