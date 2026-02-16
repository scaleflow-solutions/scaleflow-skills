# Weavy Pipeline Patterns — Multi-Format & Branching Strategies

> Reference for designing complex workflows that produce multiple outputs from shared inputs. These patterns minimize credit spend by maximizing free node usage and avoiding redundant generations.

---

## Pattern 1: Single Source, Multiple Crops

**Scenario:** One generated image needs to be delivered in 5+ platform formats.

**Strategy:** Generate at the largest common dimension, then crop/resize for each platform.

```
Prompt → Generator (16:9 landscape, highest res)
              ↓
           Levels (color correct once)
              ↓
    ┌─────┬─────┬─────┬─────┬─────┐
    ↓     ↓     ↓     ↓     ↓     ↓
  Crop  Crop  Crop  Crop  Crop  Resize
  1:1   9:16  4:5   16:9  1.91:1 (original)
    ↓     ↓     ↓     ↓     ↓     ↓
  Exp   Exp   Exp   Exp   Exp   Exp
  IG    Story  IG    YT    FB    Hero
  Feed         Port  Thumb  Ad
```

**Credits:** 1 generation. All crops and exports are free.

**Key decision:** Generate in the aspect ratio that loses the least content when cropping to all targets. For most social campaigns, **16:9 landscape** works best because vertical crops (9:16) can center on the subject, while square (1:1) crops the sides.

**When this pattern fails:** When the subject needs to be repositioned differently per platform (e.g., left-aligned for desktop, centered for mobile). In that case, use Pattern 3 instead.

---

## Pattern 2: Draft-to-Final Upgrade Path

**Scenario:** Limited budget requires cheap exploration before committing to expensive final renders.

**Strategy:** Build the full pipeline with a cheap model first. Once approved, swap only the generator model — all downstream nodes stay the same.

```
DRAFT PHASE:
Prompt → Flux Schnell (1 credit) → Levels → Crop → Export

FINAL PHASE (same pipeline, swap model):
Prompt → Flux Kontext (3 credits) → Levels → Crop → Export
```

**How to swap:** Click the generator node → change model in the right panel → re-run. All downstream connections remain intact.

**Model upgrade paths:**

| Category | Draft Model (cheap) | Final Model (quality) | Credit Savings |
|---|---|---|---|
| Image | Flux Schnell (1) | Flux Kontext (3) | 2 credits/gen |
| Image | Flux Schnell (1) | Ideogram 3 (4) | 3 credits/gen |
| Video | LTX Video (2) | Kling 2.0 Master (40) | 38 credits/gen |
| Video | Wan Video (3) | Runway Gen-4 Turbo (20) | 17 credits/gen |
| 3D | Trellis (2) | Meshy (4) | 2 credits/gen |

---

## Pattern 3: Parallel Generation for Different Compositions

**Scenario:** Different platforms need fundamentally different compositions (not just crops).

**Strategy:** Share prompts but run separate generators with different aspect ratios.

```
Prompt (subject) ──→ Concatenator ──┬──→ Generator (1:1) → Levels → Export (IG Feed)
Prompt (style)   ──↗               ├──→ Generator (9:16) → Levels → Export (Story)
                                    └──→ Generator (16:9) → Levels → Export (Banner)
```

**Credits:** 1 credit per platform (3 generations for 3 formats).

**When to use over Pattern 1:** When the subject needs different framing, not just cropping. For example, a product shot might be centered in square but positioned left with copy space on the right for a banner.

---

## Pattern 4: Shared Prompt Architecture

**Scenario:** Multiple pipelines across a campaign need consistent creative direction.

**Strategy:** Build a modular prompt system using Prompt Concatenator. Change one prompt node and all connected pipelines update.

```
Prompt (brand style)  ──→ Concatenator 1 ──→ Hero Image Generator
Prompt (subject)      ──↗       ↓
                          Concatenator 2 ──→ Social Image Generator
Prompt (platform)     ──↗       ↓
                          Concatenator 3 ──→ Video Generator
Prompt (motion cues)  ──↗
```

**Prompt node responsibilities:**

| Node | Content | Example |
|---|---|---|
| Brand style | Consistent visual language | "Clean minimalist photography, soft natural lighting, muted earth tones" |
| Subject | What appears in the scene | "Athletic runner mid-stride on wet urban street" |
| Platform | Technical specs | "Photorealistic, 4K resolution, sharp focus" |
| Motion cues | Video-only additions | "Slow camera push-in, shallow depth of field rack focus" |

**Benefits:**
- Change the brand style prompt → all outputs update
- Change the subject prompt → new campaign, same visual system
- Platform and motion prompts stay constant across campaigns

---

## Pattern 5: Enhancement Chain

**Scenario:** Generated output needs multiple improvements before final export.

**Strategy:** Chain enhancement nodes left-to-right. Always put free nodes before paid ones.

```
[Generator] → Levels (free) → Relight (paid) → Topaz Upscale (paid) → Export
```

**Recommended chain order:**

1. **Levels** (free) — Fix contrast and brightness first
2. **Crop/Resize** (free) — Get to target dimensions
3. **Relight** (paid, 2-3 credits) — Fix lighting if needed
4. **Upscale** (paid, 2-5 credits) — Increase resolution last (processes fewer pixels if cropped first)

**Why this order matters:**
- Levels before Relight: gives the relighting model better tonal range to work with
- Crop before Upscale: upscaling a cropped image is cheaper (fewer pixels) and faster
- Never upscale before crop — wastes computation on pixels you will discard

---

## Pattern 6: Image-to-Video Cascade

**Scenario:** Campaign needs both static images and animated versions.

**Strategy:** Build the image pipeline first. Feed its output into a separate video pipeline.

```
PIPELINE 1 (Image):
Prompt → [Image Generator] → Levels → Export (hero image)
                                 ↓ (also feeds Pipeline 2)

PIPELINE 2 (Video):
[Image from Pipeline 1] + Prompt (motion) → [Video Generator] → Levels → Export (video)
                                                                    ↓
                                                            Extract Frame → Export (thumbnail)
```

**Connection:** The Levels node output from Pipeline 1 connects directly to the Video Generator's image input in Pipeline 2.

**Canvas organization:**
- Group 1 (green): "Hero Image" — left side of canvas
- Group 2 (red): "Hero Video" — right side of canvas
- Shared Prompt nodes sit between groups

---

## Pattern 7: Batch with Controlled Variation

**Scenario:** Need multiple variations (A/B testing, client options) with controlled differences.

**Strategy:** Use Image Iterator for quantity, but vary one input at a time.

```
VARIATION SET A (different subjects, same style):
Prompt (style, locked) → Concatenator ← Prompt (subject A) → Generator → Iterator (3x) → Export
                                       ← Prompt (subject B) → Generator → Iterator (3x) → Export

VARIATION SET B (same subject, different styles):
Prompt (subject, locked) → Concatenator ← Prompt (style A) → Generator → Iterator (3x) → Export
                                         ← Prompt (style B) → Generator → Iterator (3x) → Export
```

**Lock strategy:** Lock the constant prompt node (three-dot menu → Lock) so it cannot be accidentally changed. This is especially useful when creating a Design App from the workflow.

---

## Pattern 8: Design App Pattern

**Scenario:** A workflow needs to be reusable by non-technical team members or clients.

**Strategy:** Build the full workflow, then convert to a Design App with only the essential inputs exposed.

```
Full workflow:
[Locked: style prompt] → Concatenator → Generator → Levels → Crop → Export
[Exposed: subject prompt] ↗
[Exposed: Import image]  ↗
```

**Steps to convert:**
1. Lock all nodes that should stay constant (style prompts, settings nodes, enhancement nodes)
2. Leave unlocked only the nodes the user should change (subject prompt, image import)
3. Add an Output node connected to the final Export
4. Switch to App tab → verify only desired parameters are exposed
5. Publish and share

**What to expose vs. lock:**

| Expose (user changes) | Lock (stays constant) |
|---|---|
| Subject/scene prompt | Style/brand prompt |
| Reference image import | Enhancement settings |
| | Model selection |
| | Crop dimensions |
| | Export format |

---

## Pattern 9: Multi-Asset-Type Campaign

**Scenario:** Full campaign with images, video, and 3D assets.

**Strategy:** Separate canvas into distinct groups by asset type. Share brand prompts across all.

```
CANVAS LAYOUT:

[Shared Prompts Group] ─────────────────────────
│ Brand Style Prompt                             │
│ Subject Prompt                                 │
│ Prompt Concatenator                            │
──────────────────────────────────────────────────
        ↓               ↓               ↓
[Image Group]    [Video Group]     [3D Group]
│ Generator │    │ Generator │     │ Generator │
│ Levels    │    │ Levels    │     │ Export    │
│ Crop (5x) │    │ Crop (2x) │     ─────────────
│ Export(6x)│    │ ExtFrame  │
─────────────    │ Export(3x)│
                 ─────────────
```

**Group colors:**
- Shared Prompts: Purple (text)
- Image Group: Green
- Video Group: Red
- 3D Group: Blue

**Run sequence:**
1. Images first (fastest, cheapest — validates creative direction)
2. Video second (uses approved image as reference if needed)
3. 3D last (longest generation time)
