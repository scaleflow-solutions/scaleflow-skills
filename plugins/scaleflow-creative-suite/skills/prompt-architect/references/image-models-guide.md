# Image Model Prompt Guide

Detailed prompt strategies for each image generation model available in Weavy AI.

## Flux Dev (with LoRA)

**Credit cost:** 38 (Starter)
**Best for:** Consistent product rendering using trained LoRA models, photorealistic scenes
**Prompt length sweet spot:** 30-80 words

### How Flux Reads Prompts
Word order matters heavily. Flux weights earlier elements more strongly. Front-load the most important visual information. Every word must earn its place.

### Prompt Template
```
[Subject with specific details], [key action or pose], [environment/setting],
[lighting condition], [camera/lens specification], [style or mood], [color palette]
```

### What Works Well
- Specific camera and lens references: "shot on Hasselblad medium format, 85mm lens, f/1.8"
- Concrete lighting descriptions: "harsh stadium floodlights casting sharp shadows on wet turf"
- Real photography terminology produces more photorealistic results
- Style references to specific genres: "editorial sports photography", "high-fashion campaign"
- Film stock references: "Kodak Portra 400 film stock warmth"

### What to Avoid
- Conflicting styles: "vintage film grain" + "ultra-modern digital clarity"
- Overloaded compositions: if the scene is busy, request "clean negative space" or tighter crop
- Vague lighting: "good lighting" vs "directional key light from upper left with soft fill"
- Over 100 words: creates confusion and competing instructions

### LoRA-Specific Notes
When using a trained LoRA (e.g., for a product like a Clear bottle), keep the prompt focused on scene and context. The LoRA handles the product appearance — your prompt handles everything else.

Template: [LoRA trigger word], [scene and placement], [surrounding environment], [lighting], [camera angle], [mood]

---

## Flux Kontext

**Credit cost:** 50 (Starter)
**Best for:** Contextual editing and remixing existing images, scene modifications

### How Kontext Works
Designed for editing and remixing, not generation from scratch. Prompts should describe the desired change, not the entire scene.

### Template
Describe what should change and what should remain: "Change the background to a packed stadium at night while keeping the athlete's pose and lighting unchanged."

---

## Ideogram V3

**Credit cost:** 38 (Starter)
**Best for:** Images with readable text (posters, social graphics, billboards, packaging)
**Prompt length limit:** 150-160 words

### Text Rendering — The Key Advantage
Approximately 90% text accuracy — best in class. Use Ideogram whenever the deliverable requires readable text.

### Text Rules
- Enclose exact text in quotation marks: "NEVER SWEAT THE GAME"
- Place text instruction early in the prompt
- Keep text short: 2-5 words render most reliably
- Describe typography style: "bold condensed sans-serif", "elegant serif script"
- Specify placement: "centered at the top", "bottom-right corner"
- For spacing: add "generous margins", "wide tracking", "loose kerning"

### Template
```
A [format type] featuring the text "[EXACT TEXT]" in [typography style],
[placement on image], [visual scene], [color scheme], [overall style]
```

### Use the "Design" Style
For any graphic design work with text elements, select Ideogram's Design style mode.

---

## Minimax Image

**Credit cost:** 150 (Starter)
**Best for:** Quick concept exploration, initial ideation
**Note:** Expensive on Starter — consider using Mystic for drafts instead

### Prompt Approach
Simpler, more direct prompts. Responds well to straightforward scene descriptions without heavy technical camera specs.

---

## GPT Image 1 Edit

**Credit cost:** 19 (Starter)
**Best for:** Editing existing images, specific modifications, touch-ups

### Template
"Edit this image to [specific change]. Keep [elements to preserve] unchanged. The result should [desired quality or mood]."

---

## Runway Gen-4 Image

**Credit cost:** 25 (Starter)
**Best for:** High-quality image generation with cinematic quality

---

## Mystic

**Credit cost:** 13 (Starter)
**Best for:** Rapid exploration, mood testing, style direction on a budget
**Use case:** The cheapest image model — ideal for draft rounds and concept validation before committing to premium models.

---

## Imagen 4

**Credit cost:** 25 (Starter)
**Best for:** Photorealism, complex scenes, final polish renders
**Strength:** Strong at detailed natural-language descriptions.

---

## Flux Fast

**Credit cost:** 375 (Starter)
**Warning:** Very expensive. Use only when speed is critical and budget allows. For most use cases, Flux Dev or Flux Kontext are better value.
