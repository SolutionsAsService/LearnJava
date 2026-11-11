# Critic: Inclusion (Mace), R2

**Anchor used:** The Principles of Universal Design (Mace et al.): Principle 4, Perceptible Information, and Principle 3, Simple and Intuitive Use.

**Observed:** I pressed Tab on the home page in Playwright at 390 and 1280, in light and dark.
- 390: the order is nav, `.start` (y147), the six `.lg a` (y616–727), then the 13 `.strip` tiles (y927). This matches the visual order, so R1 F1 is fixed.
- 1280: the order is nav, `.start`, the legend in the right column (x932, y228–772), then back to the strip in the left column (x32, y454).
- `.start` is 120×44 at 390 and 189×44 at 1280. Its text is 14.6:1 (light) and 15.2:1 (dark). Its 3px offset ring falls on the paper at 5.46:1 and 9.28:1.
- The phone `.lg-go-m` destinations are 12px, at 5.73:1 or better.
- The cards are 44px or taller with a 4px gap.
- In forced colours, `[aria-current]` computes to a 3px solid LinkText bottom border, so R1 F2 is fixed.
- The magic tiles are 5.24:1 (light) and 8.33:1 (dark), at 38px and 92px. R1 F4 is fixed.

**Findings:**
- F1 [claim] At 1280, focus crosses from the right column back to the upper-left. Each column stays in order and the sequence keeps its meaning, so this passes WCAG 2.4.3, but the jump is about 900px.
- F2 [defect] In forced colours, `.start` loses its ink fill and has no border. It renders as bare wrapped LinkText ("Start / lesson 01 / →"), with no button boundary.
- F3 [premise] The phone destinations sit at the 12px floor. This is legal, with no margin.

**Verdict:** PASS

**Requested change:**
- F1: optionally, put the strip under the legend, or give lede and strip a full-width row at 1000px and up.
- F2: give `.start` a `border: 1px solid transparent` and `white-space: nowrap`.
- F3: none.
