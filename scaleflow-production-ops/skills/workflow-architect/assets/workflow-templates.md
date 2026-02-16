# Weavy Workflow Templates

> Reusable node-by-node templates for common deliverable types. Each template shows the minimum viable pipeline — extend with additional free nodes as needed.

---

## Template 1: Single Hero Image

**Use when:** One high-quality image deliverable at a single dimension.

```
Prompt → [Image Generator] → Levels → Export
```

| # | Node | Type | Key Settings | Credits |
|---|---|---|---|---|
| 1 | Prompt | Text | Full creative description | Free |
| 2 | Image Generator | Generative | Model + aspect ratio + guidance | Varies |
| 3 | Levels | Editing | Fine-tune contrast/brightness | Free |
| 4 | Export | Output | Format (PNG/JPG), quality | Free |

**Total credits:** 1 generation cost only.

---

## Template 2: Hero Image + Multi-Platform Adaptations

**Use when:** One hero image needs to be adapted to multiple platform dimensions.

```
Prompt → Prompt Concatenator → [Image Generator] → Levels
                                                      ↓
                                              ┌───────┼───────┐
                                              ↓       ↓       ↓
                                           Crop 1  Crop 2  Crop 3
                                              ↓       ↓       ↓
                                          Export 1 Export 2 Export 3
```

| # | Node | Type | Key Settings | Credits |
|---|---|---|---|---|
| 1 | Prompt (subject) | Text | Subject/scene description | Free |
| 2 | Prompt (style) | Text | Visual style, lighting, mood | Free |
| 3 | Prompt Concatenator | Text | Combines subject + style | Free |
| 4 | Image Generator | Generative | Highest-res aspect ratio | Varies |
| 5 | Levels | Editing | Contrast/brightness | Free |
| 6-8 | Crop (per platform) | Editing | Platform dimensions | Free |
| 9-11 | Export (per platform) | Output | Format per platform | Free |

**Total credits:** 1 generation cost. All adaptations are free.

**Common crop dimensions:**
- Instagram Feed: 1080x1080 (1:1)
- Instagram Story: 1080x1920 (9:16)
- Facebook Cover: 820x312
- Twitter Header: 1500x500
- LinkedIn Banner: 1128x191

---

## Template 3: Image with Reference Input

**Use when:** Generating an image based on a reference photo (style transfer, product placement, etc.).

```
Import (reference) → [Image Generator] ← Prompt
                           ↓
                        Levels → Export
```

| # | Node | Type | Key Settings | Credits |
|---|---|---|---|---|
| 1 | Import | Input | Upload reference image | Free |
| 2 | Prompt | Text | Description + style direction | Free |
| 3 | Image Generator | Generative | Model with image input (Flux Kontext, IP Adapter) | Varies |
| 4 | Levels | Editing | Fine-tune output | Free |
| 5 | Export | Output | Format + dimensions | Free |

---

## Template 4: Image with LoRA Style

**Use when:** Custom style consistency is required across multiple outputs.

```
Import LoRA → [FluxDev LoRA] ← Prompt
  Number (strength) ↗        ↓
                           Levels → Export
```

| # | Node | Type | Key Settings | Credits |
|---|---|---|---|---|
| 1 | Import LoRA | Input | Upload .safetensors file | Free |
| 2 | Number | Datatype | Float, 0-1 (strength) | Free |
| 3 | Prompt | Text | Subject description | Free |
| 4 | FluxDev LoRA | Generative | LoRA1 + LoRA1 scale connected | Varies |
| 5 | Levels | Editing | Adjust output | Free |
| 6 | Export | Output | Final format | Free |

**Stacking two LoRAs:** Add a second Import LoRA → Number pair connected to LoRA2 + LoRA2 scale.

---

## Template 5: Text-to-Video

**Use when:** Generating a video from a text description only.

```
Prompt → [Video Generator] → Levels → Export
```

| # | Node | Type | Key Settings | Credits |
|---|---|---|---|---|
| 1 | Prompt | Text | Scene, action, camera movement | Free |
| 2 | Video Generator | Generative | Model + duration + aspect ratio | Varies |
| 3 | Levels | Editing (video) | Color correction | Free |
| 4 | Export | Output | MP4 format | Free |

**Draft vs. final model path:**
- Draft: LTX Video (2 credits), Wan Video (3 credits)
- Final: Kling 2.0 Master (40 credits), Runway Gen-4 Turbo (20 credits)

---

## Template 6: Image-to-Video (Hero Frame Animation)

**Use when:** Animating a static hero image into a video.

```
[Image Pipeline] → image output
                        ↓
Prompt (motion) → [Video Generator] → Levels → Export
```

| # | Node | Type | Key Settings | Credits |
|---|---|---|---|---|
| 1 | Image output | From previous pipeline | Hero image | Already paid |
| 2 | Prompt (motion) | Text | Camera movement + action | Free |
| 3 | Video Generator | Generative | Image-to-video model | Varies |
| 4 | Levels | Editing | Color match to hero | Free |
| 5 | Export | Output | MP4 format | Free |

**Recommended image-to-video models:**
- Runway Gen-4 Turbo (20 credits) — best motion quality
- Kling 2.0 Master Image-to-Video (40 credits) — longest duration
- Hailuo I2V Director (10 credits) — good balance

---

## Template 7: Video with Social Cutdowns

**Use when:** A hero video needs to be adapted to multiple social formats.

```
[Video Pipeline] → video output
                        ↓
                ┌───────┼───────┐
                ↓       ↓       ↓
             Crop 1  Crop 2  Extract Frame
                ↓       ↓       ↓
            Export 1 Export 2 Export 3 (thumbnail)
```

| # | Node | Type | Key Settings | Credits |
|---|---|---|---|---|
| 1 | Video output | From previous pipeline | Full video | Already paid |
| 2-3 | Crop (per format) | Editing | Social dimensions | Free |
| 4 | Extract Video Frame | Editing | Thumbnail frame selection | Free |
| 5-7 | Export | Output | MP4 for videos, PNG for thumbnail | Free |

---

## Template 8: 3D Product Render

**Use when:** Generating 3D product renders or objects.

```
Import (product photo) → [3D Generator] → Export
                              ↓
                      [Additional angles via re-run]
```

| # | Node | Type | Key Settings | Credits |
|---|---|---|---|---|
| 1 | Import | Input | Product reference photo | Free |
| 2 | 3D Generator | Generative | Trellis/Meshy/Sam 3D | Varies |
| 3 | Export | Output | GLB/OBJ format | Free |

**3D model options:**
- Trellis (2 credits) — fast, good for simple objects
- Sam 3D Objects (3 credits) — better detail
- Meshy (4 credits) — highest quality

---

## Template 9: Batch Image Production (Image Iterator)

**Use when:** Producing multiple variations of the same concept (e.g., A/B testing, color variants).

```
Prompt → [Image Generator] → Image Iterator → Export
                                   ↓
                          (runs N generations)
```

| # | Node | Type | Key Settings | Credits |
|---|---|---|---|---|
| 1 | Prompt | Text | Base creative description | Free |
| 2 | Image Generator | Generative | Model + settings | Varies per run |
| 3 | Image Iterator | Helper | Count = number of variations | Free |
| 4 | Export | Output | All variations | Free |

**Total credits:** Generation cost × number of iterations.

---

## Template 10: Composite/Multi-Layer Design

**Use when:** Building a final image from multiple generated elements (e.g., background + product + text overlay).

```
Prompt (BG) → [Generator 1] → Compositor ← [Generator 2] ← Prompt (FG)
                                    ↓
                                 Levels → Export
```

| # | Node | Type | Key Settings | Credits |
|---|---|---|---|---|
| 1 | Prompt (background) | Text | Background scene | Free |
| 2 | Generator 1 | Generative | Background image | Varies |
| 3 | Prompt (foreground) | Text | Product/subject | Free |
| 4 | Generator 2 | Generative | Foreground element | Varies |
| 5 | Compositor | Editing | Blend mode, layer order, position | Free |
| 6 | Levels | Editing | Final color balance | Free |
| 7 | Export | Output | Final composite | Free |

**Compositor settings:** Use "Normal" blend mode for most cases. Adjust translation/rotation to position the foreground element. Use layer ordering to control z-depth.

---

## Template 11: Image Enhancement Pipeline

**Use when:** Improving existing images (upscaling, relighting, background removal/replacement).

```
Import (original) → [Enhancement Node] → Levels → Export
```

**Enhancement options:**

| Enhancement | Node | Credits | When to Use |
|---|---|---|---|
| Upscale resolution | Topaz Upscale / Recraft Crisp Upscale | 2-5 | Low-res source needs print quality |
| Fix lighting | Relight | 2-3 | Flat or wrong lighting direction |
| Remove background | Bria Remove Background | 0.6 | Product isolation |
| Replace background | Bria Replace Background | 2 | Scene change |
| Style transfer | Flux Kontext | 3 | Match a visual style |

Chain multiple enhancements left-to-right. Free nodes (Levels, Blur, Crop) can go between paid ones at no cost.
