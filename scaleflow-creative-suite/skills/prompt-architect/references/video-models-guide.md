# Video Model Prompt Guide

Detailed prompt strategies for each video generation model available in Weavy AI.

## Kling 2.1 Standard

**Credit cost:** 88 (Starter)
**Best for:** Athletic motion, dynamic physical movement, sports action, 360° rotation

### How Kling Reads Prompts
Formula: Subject + Movement + Scene + Camera Language + Lighting + Atmosphere

Camera movement is the single most important element. Without it, footage looks stiff and lifeless.

### Prompt Structure
```
[Subject with visual details], [precise physical movement],
[scene environment with 3-5 elements max],
[specific camera movement with start and end points],
[lighting conditions], [atmospheric details and mood]
```

### Camera Movement is Critical
- Always name the specific move: "slow dolly in", "lateral tracking shot", "gentle orbit"
- Specify speed: "slow", "rapid", "gentle", "steady"
- Define start and end: "camera begins wide and pushes in to a tight close-up"
- Add motion endpoints: "then settles back into place" prevents drift
- Layer movements: "tracking shot with slight handheld shake"

### 360° Rotation
Works well but needs 10 seconds. 5-second clips won't complete the full spin. Use "360-degree rotation" or "360 spin" in prompt.

### Micro-Motions for Realism
Add life to scenes with: condensation on surfaces, steam rising, hair moving in wind, jersey fabric rippling, water droplets, flickering lights, dust particles.

### What to Avoid
- Multiple simultaneous camera transforms: zoom + rotate + pan = warped geometry
- Abstract concepts instead of physical actions: "convey determination" vs "clenches fist, jaw tightens"
- Mixing incompatible lighting: "golden hour" + "studio lighting"
- More than 3-5 scene elements: overloading creates confusion

---

## Runway Gen-4 Turbo

**Credit cost:** 75 (Starter)
**Best for:** Image-to-video animation, controlled camera movements

### Key Rule: Motion, Not Visuals
When using image-to-video, the image provides all visual information. Text prompt focuses ENTIRELY on motion and camera direction.

### Rules
- Do NOT redescribe what is visible in the input image
- Focus on: what moves, how it moves, what the camera does
- No negative phrasing ("don't show" — model may do exactly that)
- Concrete movements, not feelings: physical actions, not emotions
- Each 5-10 second generation = single scene (don't pack multiple scenes)
- Up to 1,000 characters but shorter focused prompts often outperform

### Template (Image-to-Video)
```
[Subject movement — specific physical action],
[camera movement with direction and speed],
[ambient motion — wind, particles, fabric],
[motion style — smooth, handheld, cinematic]
```

### Genre-Specific Guidance
- Action/thriller: fast camera changes, dynamic angles, kinetic energy
- Drama: smooth, intimate framing, slow movements
- Documentary: naturalistic, observational, steady handheld
- Commercial/product: smooth orbits, clean reveals, controlled lighting shifts

---

## Runway Act-Two

**Credit cost:** 38 (Starter)
**Best for:** Character performance, facial expressions, acting, gesture

### Template
```
[Character action — specific gesture or expression],
[emotional quality], [movement speed and style], [eye direction and gaze]
```

---

## Veo 3 Fast

**Credit cost:** 13 (Starter)
**Best for:** Atmospheric establishing shots, cinematic sequences (budget-friendly)

### How Veo Reads Prompts
Scene + Visual Style + Camera + Subject + Background + Lighting and Mood. Film grammar terms are well understood.

### Template
```
[Scene setting in one sentence], [visual style],
[camera movement with film terms], [main subject and action],
[background environment], [lighting and mood]
```

### Lighting Veo Understands Well
- "Golden hour sunlight" — warm, directional
- "Rembrandt lighting" — dramatic portrait
- "Chiaroscuro" — extreme light/dark contrast
- Color temperature: "warm 3200K", "cool 5600K daylight"

---

## Seedance V1.0

**Credit cost:** 88 (Starter)
**Best for:** Dance, athletics, dynamic physical movement, rhythmic motion

### Template
```
[Subject in motion — detailed physical movement],
[movement quality — fluid, explosive, graceful, mechanical],
[environment], [camera following strategy], [rhythm and pacing]
```

---

## LTX 2 Video Fast

**Credit cost:** 38 (Starter)
**Best for:** Drafts, iteration, quick motion tests at lower cost

## LTX 2 Video Pro

**Credit cost:** 25 (Starter)
**Best for:** Higher quality finals at moderate cost

### Strategy
Use Fast for exploring concepts and motion tests. Switch to Pro once the right prompt is dialed in.

---

## Minimax Hailuo 02

**Credit cost:** 63 (Starter)
**Best for:** Smooth, stylized motion, product reveals, atmospheric scenes

---

## Wan Vace

**Credit cost:** 75 (Starter)
**Best for:** Versatile video generation. Experiment with different prompt styles.

---

## Veo 3 (Full)

**Credit cost:** Not available on Starter plan
**Note:** Only available on Professional and Team plans. Superior quality to Veo 3 Fast.
