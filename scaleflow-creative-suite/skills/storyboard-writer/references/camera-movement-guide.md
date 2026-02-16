# Camera Movement Guide for AI Video Generation

A reference mapping camera movements to their visual effect, best use cases, and which Weavy AI video model handles them best.

---

## Camera Movements and Weavy Model Compatibility

| Movement | Description | Best For | Best Weavy Model |
| --- | --- | --- | --- |
| Static / locked-off | No camera movement, fixed frame | Composed reveals, product beauty shots, dialogue | Any model — safest default |
| Slow dolly in | Gradual push toward subject | Building tension, drawing focus, intimate reveal | Kling 2.1, Runway Gen-4 Turbo |
| Slow dolly out | Gradual pull away from subject | Revealing context, endings, scope | Kling 2.1, Veo 3 Fast |
| Lateral tracking | Camera moves sideways alongside subject | Following action, energy, sports | Kling 2.1, Seedance |
| Pan left/right | Camera rotates horizontally on fixed point | Revealing environment, following action | Veo 3 Fast, Kling 2.1 |
| Tilt up/down | Camera rotates vertically on fixed point | Revealing scale, building anticipation | Veo 3 Fast, Kling 2.1 |
| Crane / boom up | Camera rises vertically | Dramatic reveal, scale, establishing | Veo 3 Fast |
| Crane / boom down | Camera descends vertically | Focusing in, arrival, intimate | Veo 3 Fast |
| Orbit / arc | Camera circles around subject | 3D showcase, product reveal, hero moment | Kling 2.1, Minimax Hailuo 02 |
| Handheld | Slight natural shake, documentary feel | Authenticity, urgency, sports action | Kling 2.1 |
| Rack focus | Focus shifts between foreground and background | Directing attention, storytelling | Runway Gen-4 Turbo |
| Whip pan | Rapid horizontal snap | Transition, energy, surprise | Kling 2.1 |
| Zoom in/out | Optical zoom without camera movement | Emphasis, Hitchcock effect | LTX 2 Video, Veo 3 Fast |

---

## Movement Speed Vocabulary

Use these specific terms in shot descriptions for consistency:

| Speed Term | Feel | Duration |
| --- | --- | --- |
| Glacial | Almost imperceptible, meditative | Best for 10-sec clips |
| Slow | Contemplative, building tension | Standard for reveals |
| Gentle | Subtle, naturalistic | Good for beauty shots |
| Steady | Neutral, professional | Default for most shots |
| Medium | Purposeful, following action | Standard for tracking |
| Rapid | Energetic, urgent | Action sequences |
| Whip / snap | Instant direction change | Transitions only |

---

## Combination Movements

These work well in AI video models when described clearly:

| Combination | Description | Effect |
| --- | --- | --- |
| Dolly + tilt up | Push toward subject while tilting up | Dramatic reveal, hero introduction |
| Track + dolly in | Move alongside then push in | Building connection, intimacy |
| Crane up + pan | Rise while rotating horizontally | Establishing shot, scope reveal |
| Orbit + dolly in | Circle while closing distance | Intensifying focus on subject |

**Warning:** Avoid combining more than 2 movements. AI models struggle with 3+ simultaneous transforms and produce warped geometry.

---

## Shot Duration and Movement

| Duration | What Works | What Doesn't |
| --- | --- | --- |
| 2-3 seconds | Static, single simple move, hard cuts | Complex movements (not enough time) |
| 5 seconds | One complete movement with start/end | Full orbits (need 10 sec) |
| 10 seconds | Full orbits, combination moves, slow reveals | Multiple scene changes (one move per clip) |

**Rule of thumb:** One camera movement per generated clip. If the storyboard calls for a move that changes direction (e.g., "pan left then dolly in"), split it into two shots with a cut between them.

---

## Writing Shot Descriptions for Weavy Prompts

Each shot description in the storyboard should be structured so it can be almost directly pasted into the target Weavy model. Follow this format:

**[Subject with visual details], [specific physical action], [environment with 3-5 elements], [camera movement with speed and start/end], [lighting], [atmosphere/mood]**

### Good example:
> "An athlete mid-stride on a rain-soaked pitch, sprinting toward camera, stadium floodlights creating rim lighting around their silhouette, slow dolly out revealing the packed stadium behind, humid haze catches the light, intense and electric"

### Bad example:
> "The athlete runs with determination while the camera captures the excitement of the moment"

The good example gives the AI model concrete visual instructions. The bad example uses abstract concepts ("determination", "excitement") that models cannot interpret.

---

## Weavy Pipeline Mapping

For each shot type, here is the recommended Weavy production pipeline:

### Image-to-Video (most controlled)
1. Generate still image with Flux/Ideogram (best visual control)
2. Feed image into Runway Gen-4 Turbo
3. Prompt describes ONLY motion and camera (not visual appearance)
4. Best for: product shots, beauty shots, any shot where visual precision matters

### Text-to-Video (most creative freedom)
1. Write full prompt describing visual + motion + camera
2. Generate directly with Kling 2.1, Veo 3 Fast, or Seedance
3. Best for: action sequences, establishing shots, atmospheric content

### Character Performance
1. Generate or upload character reference image
2. Feed into Runway Act-Two
3. Prompt focuses on facial expression, gesture, emotion
4. Best for: dialogue scenes, reaction shots, emotional moments

### Product Showcase
1. Generate 3D model with Rodin/Trellis
2. Render at desired angle
3. Animate with smooth orbit/dolly via Runway Gen-4 Turbo
4. Or: Generate product still with Flux → animate with camera move
