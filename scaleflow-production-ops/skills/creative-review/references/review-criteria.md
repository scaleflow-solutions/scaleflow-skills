# Creative Review Criteria Checklist

Structured QA checklist for evaluating AI-generated creative assets before client presentation.

---

## Brief Compliance

| Check | What to Evaluate |
| --- | --- |
| Deliverable type matches brief | Is it the right format (static, video, 3D)? |
| Dimensions correct | Does it match the specified platform/format? |
| Subject present | Is the required subject/product visible? |
| Key message conveyed | Does the visual communicate the campaign message? |
| Target audience appropriate | Would the target audience connect with this? |
| Mandatory elements included | Tagline, logo, product, legal text — all present? |
| Restrictions respected | Nothing the brief said to avoid? |

---

## Brand Consistency

| Check | What to Evaluate |
| --- | --- |
| Primary color match | Within tolerance of brand primary hex code? |
| Secondary/accent colors | Used appropriately, not dominating? |
| Color temperature | Consistent with brand warmth/coolness? |
| Logo placement | Correct position, size, clear space? |
| Logo legibility | Readable against background? |
| Typography style | Matches brand direction (modern/classic/bold/minimal)? |
| Font weight hierarchy | Headlines > subheads > body — clear hierarchy? |
| Brand voice alignment | Visual tone matches voice keywords? |
| Product accuracy | Correct label, proportions, color rendering? |

---

## Technical Quality — Images

| Check | What to Evaluate |
| --- | --- |
| Resolution | Sufficient for intended use (72 DPI web, 300 DPI print)? |
| Aspect ratio | Correct for platform? |
| Hands/fingers | Natural count and positioning? |
| Facial features | Symmetrical, natural, no warping? |
| Text rendering | Legible, correctly spelled, properly positioned? |
| Shadow consistency | All shadows cast from same light source? |
| Edge quality | No melting, blurring, or unnatural transitions? |
| Background consistency | No repeated patterns, tiling artifacts? |
| Color banding | Smooth gradients, no stepping? |
| Composition | Subject placement matches visual direction? |
| Text overlay space | Room for copy where needed? |

---

## Technical Quality — Video

| Check | What to Evaluate |
| --- | --- |
| Motion smoothness | No jitter, stuttering, or frame drops? |
| Subject consistency | Does the subject maintain form throughout? No morphing? |
| Camera movement | Smooth and intentional? Matches storyboard? |
| Lighting consistency | Same lighting throughout clip? No flickering? |
| Temporal coherence | No sudden scene changes, color shifts, or object teleportation? |
| Duration | Matches the specified length? |
| Frame rate | Consistent, no dropped frames? |
| Audio sync | If audio present, is it synchronized? |
| Start/end frames | Clean entry and exit? Usable for editing? |

---

## Technical Quality — 3D Models

| Check | What to Evaluate |
| --- | --- |
| Geometry integrity | No holes, floating vertices, inverted normals? |
| Texture mapping | Accurate, no stretching or seams? |
| Proportions | Matches real-world product dimensions? |
| Polygon count | Appropriate for intended use (web vs. film)? |
| Topology quality | Clean quads for animation, tris ok for static display? |
| File format | Correct for target (GLB for web, USDZ for AR, OBJ for editing)? |

---

## Common AI Artifacts to Flag

| Artifact | Where It Appears | Severity |
| --- | --- | --- |
| Extra/missing fingers | Hands | Must fix |
| Warped text | Ideogram/Flux text overlays | Must fix |
| Melted edges | Subject outlines, especially hair | Should fix |
| Impossible reflections | Glass, water, metal surfaces | Should fix |
| Repeated patterns | Backgrounds, crowds, textures | Should fix |
| Inconsistent shadows | Multiple light sources implied | Should fix |
| Floating objects | Products, accessories | Must fix |
| Morphing subject | Video — face or body changes between frames | Must fix |
| Flickering | Video — brightness or color instability | Must fix |
| Plastic skin | Over-smoothed skin texture | Consider |

---

## Revision Priority Framework

**Must fix before client presentation:**
- Anything factually wrong (wrong product, wrong logo, wrong text)
- Major AI artifacts visible at normal viewing distance
- Brand violations (wrong colors, missing logo, off-tone)
- Technical failures (wrong dimensions, corrupt file)

**Should fix if time allows:**
- Minor AI artifacts visible on close inspection
- Color grading doesn't quite match mood board
- Composition could be stronger
- Motion quality slightly unnatural in video

**Consider for next round:**
- Stylistic preferences (slightly different lighting angle)
- Minor text positioning adjustments
- Additional micro-detail in textures
- Alternative crop options for different platforms
