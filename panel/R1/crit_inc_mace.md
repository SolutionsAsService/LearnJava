# Critic: Inclusion (Mace), R1

**Anchor used:** The Principles of Universal Design (Mace et al.): Principle 4, Perceptible Information (redundant modes), and Principle 1, Equitable Use.

**Observed:** I pressed Tab through index and lesson 05 at 390 and 1280, in light and dark. Every stop showed a 3px roast outline with a 3px offset: nav, 6 `.lg a`, 13 `.strip ol a`, the pager and the scrollable `.code`. Outline contrast is at least 4.23 (light) and at least 5.36 (dark). The only targets under 44px are inline sentence links. Each `:hover` rule is gated. There is no motion.

Contrast: ink on the tints is 11.3–13.4 (light) and 8.8–10.7 (dark). Text on the marks is 6.7–8.5 and 9.0–11.2. Code tokens are 6.25–10.63. Magic tiles: roast on t1 is 4.23 (light) and 8.33 (dark). Each tint is paired with a number, and LTS colour with the "LTS" tag.

**Findings:**
- F1 [defect] At 390, focus runs from the nav to `.strip` (y≈450), then jumps back to `.legend` (y≈93). CSS `order` places the legend first visually, but the DOM does not (WCAG 2.4.3).
- F2 [defect] In forced colours, the `[aria-current]` mark is a `box-shadow`, which computes to `none`. The current page loses its only visual cue.
- F3 [claim] In forced colours, every `.by` is bordered and the regions merge. Only the 9px badges separate them. This is acceptable only because the dump is `aria-hidden`.
- F4 [premise] The light magic tiles (4.23) pass only as large text, at 30px or more.

**Verdict:** OBJECT

**Requested change:**
- F1: put the legend before the strip in the DOM.
- F2: use a `border-bottom` or an underline for `[aria-current]`.
- F3: none.
- F4: keep `.magic` at 24px or larger, or darken it to at least 4.5.
