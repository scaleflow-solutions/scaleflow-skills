# Weavy AI — Complete Platform Reference

> Sources:
> - Nodes & Models: https://help.weavy.ai/en/collections/15247921-nodes-and-models-documentations
> - Editor & Canvas: https://help.weavy.ai/en/collections/15341378-weavy-s-editor
> Last fetched: 2026-02-17
> Note: Credit costs and model availability may change. The most up-to-date prices are always inside your Weavy workspace.

---

## PART 1: NODES (Tools & Utilities)

### Editing Tools

| Node | Purpose | Inputs | Outputs | Credits |
|---|---|---|---|---|
| **Levels** | Adjusts brightness, contrast, tonal range using histogram controls (shadows, midtones, highlights) | Image or Video | Adjusted image/video | Free |
| **Compositor** | Merges multiple images/videos with blend modes, layer ordering, translation, rotation | Image, Video, Text | Composited image/video | Free |
| **Painter** | Hand-painting masks and sketches on inputs or blank canvas; sketch-to-image workflows | Image (optional) | Image + Mask | Free |
| **Crop** | Crops and resizes with preset aspect ratios or custom dimensions | Image or Video | Cropped image/video | Free |
| **Resize** | Stretches or squashes to custom dimensions (changes aspect ratio) | Image or Video | Resized image/video | Free |
| **Blur** | Applies Fast Box Blur or Gaussian Blur with intensity control | Image or Video | Blurred image/video | Free |
| **Invert** | Inverts image values; useful for mask inversion | Image or Video | Inverted image/video | Free |
| **Channels** | Accesses individual R, G, B, A channels for advanced compositing | Image or Video | Separate channel outputs | Free |
| **Extract Video Frame** | Extracts a single frame from video using timeline, frame number, or timecode | Video | Static image | Free |

### Text Tools

| Node | Purpose | Inputs | Outputs | Credits |
|---|---|---|---|---|
| **Prompt** | Basic text prompt input; free-form natural language, any length | Text | Text prompt | Free |
| **Prompt Concatenator** | Combines multiple text inputs into a single unified prompt; add inputs via + button | Multiple text nodes | Single concatenated text | Free |
| **Prompt Enhancer** | Refines and improves prompt clarity using an LLM; select model from dropdown | Prompt | Enhanced prompt | Uses LLM credits |
| **Run Any LLM** | Sends text and/or image inputs to any chosen LLM for text responses | Text and/or Image | Text response | Uses LLM credits |
| **Image Describer** | Analyzes images to generate descriptive prompts identifying key visual attributes | Image | Text description | Uses LLM credits |
| **Video Describer** | Analyzes videos to generate descriptive prompts capturing key attributes | Video | Text description | Uses LLM credits |

### Helper Nodes

| Node | Purpose | Key Details | Credits |
|---|---|---|---|
| **Import** | Upload files into Weavy (click, drag-drop, or paste link) | Formats: JPEG, JPG, PNG, HEIC, WEBP, MP4, QUICKTIME, MP3, WAV, OGG, GLB. Cannot upload from Google Drive or iCloud. | Free |
| **Export** | Export files to a folder; retains original format | Works with Image and Video nodes | Free |
| **Preview** | Preview generated image/video in a clean node | Display only | Free |
| **Import Model** | Import models from Fal, Replicate, or CivitAI via URL | External model integration | Free |
| **Import LoRA** | Import custom LoRA files from local storage | Single LoRA import | Free |
| **Import Multiple LoRAs** | Import multiple LoRA files simultaneously | Add via + button in list | Free |
| **Router** | Connect one input to multiple outputs; keeps workflows organized | Simplifies prompt/model changes without manual reconnections | Free |
| **Output** | Create Design Apps from workflow | Required for App feature | Free |
| **Sticky Note** | Add tags and descriptions on canvas | Organizational; font/size not customizable | Free |

### Matte Tools

| Node | Purpose | Inputs | Key Controls | Credits |
|---|---|---|---|---|
| **Mask Extractor** | Auto-separates images into parts; select objects/regions | Image | Shift to add, Alt+Shift to subtract; preview toggle for mask view | Free |
| **Mask By Text** | Mask objects by writing a text prompt describing what to mask | Image + Text | Describe mask target in detail | Free |
| **Matte Grow/Shrink** | Expand or choke matte channel for refining masks | Image, Video, or Mask | Slider for adjustment | Free |
| **Merge Alpha** | Adds alpha channel to image using a mask | Image + Mask | Composites alpha from mask | Free |
| **Extract Video Matte** | Extract matte pass from video | Video | Dropdown to select matte type | Free |
| **Video Mask by Text** | Mask video objects/elements using a text prompt | Video + Text | Auto-generates mask from description | Free |

### Iterator Nodes

| Node | Purpose | Inputs | How It Works | Credits |
|---|---|---|---|---|
| **Text Iterator** | Batch-process multiple text prompts through the same model simultaneously | Array Node (text prompts) | Keeps each prompt separated; generates results for all in one operation | Free (model costs apply) |
| **Image Iterator** | Batch-process multiple images through the same model | Multiple images | Each image processed separately as individual runs | Free (model costs apply) |
| **Video Iterator** | Batch-process multiple videos through the same model | Multiple videos | Each video processed separately as individual runs | Free (model costs apply) |

### Datatype Nodes

| Node | Purpose | Key Features |
|---|---|---|
| **Number** | Numerical attribute input with min/max and decimal control | "Set as Output" to display on canvas |
| **Text** | Text input; functions like a Prompt node | Can be used as prompt input for other nodes |
| **Toggle** | Boolean true/false input | "Set as Output" to display on canvas |
| **List Selector** | Dropdown menu from lists; manual entry or Array Node integration | Select from different input options |
| **Seed** | Controls generation reproducibility | Random or manual seed; each output receives a seed |
| **Array** | Organize multiple text inputs into groups | Feeds into List Selector and Text Iterator nodes |

---

## PART 2: IMAGE GENERATION MODELS

| Model | Credits | Key Strengths | Best For | Special Features |
|---|---|---|---|---|
| **Reve** | 4 | Style and reference imitation; multiple image refs | Matching existing visual styles | Multiple image references |
| **Higgsfield Image** | 21 | Different style options | Stylized image generation | Style selector |
| **GPT Image 1** | 8 | Style and reference imitation | General purpose with style control | Reference images |
| **Imagen 4** | 6 | Google's latest; negative prompts | High-quality photorealistic | Negative prompt support |
| **Imagen 3** | 6 | Negative prompt support | Photorealistic generation | Negative prompt |
| **Imagen 3 Fast** | 3 | Budget-friendly Google model | Quick drafts, lower cost | Negative prompt |
| **Flux 2 Pro** | 5 | Multiple image refs; custom aspect ratios | Professional image generation | LoRA, multiple refs |
| **Flux 2 Flex** | 14 | Multiple image refs; custom aspect ratios | Flexible creative work | Multiple refs |
| **Flux 2 Dev LoRA** | 4 | LoRA support; multiple image refs | Custom model fine-tuning | LoRA weights |
| **Flux 1.1 Ultra** | 7 | LoRA and multiple reference images | High-quality with customization | LoRA support |
| **Flux Pro 1.1** | 5 | Standard professional quality | General professional use | Standard |
| **Flux Fast** | 0.4 | Ultra-cheap; fastest generation | Drafts, rapid exploration | Lowest cost |
| **Flux Dev LoRA** | 4 | LoRA input capability | Custom style generation | LoRA |
| **Recraft V3** | 5 | Baked styles option | Styled/branded content | Built-in styles |
| **Mystic** | 12 | Specialized features | Specific creative needs | — |
| **Ideogram V3** | 4 | Best text rendering (~90% accuracy) | Text-in-image graphics | Multiple aspect ratios |
| **Ideogram V3 Character** | 15 | Character reference and mask support | Character-consistent generation | Style options, mask |
| **Stable Diffusion 3.5** | 8 | Diverse aspect ratios | General purpose | Multiple ratios |
| **Minimax Image 01** | 1 | Lowest entry cost | Budget generation | Cheapest option |
| **Bria** | 6 | Standard quality | General purpose | — |
| **DALLE 3** | 5 | OpenAI quality | 1:1 square images only | Single aspect ratio |
| **Luma Photon** | 2 | 1K, 2K, 4K resolution options | Variable resolution needs | Multi-resolution |
| **Nvidia Sana** | 0.2 | Ultra-low cost | Extremely budget drafts | Cheapest available |
| **Nvidia Consistory** | 5 | Subject token support | Consistent subject generation | Subject tokens |

**Output formats**: PNG universal; many support JPEG and WEBP.

---

## PART 3: VIDEO GENERATION MODELS

| Model | Credits | Duration | Aspect Ratios | Best For |
|---|---|---|---|---|
| **Seedance V1.5 Pro** | 25–74 | 5s–10s | 16:9, 9:16, 1:1 | Dance and rhythmic motion |
| **Sora 2** | 96–288 | Variable | Multiple | Premium cinematic video |
| **Runway Gen-4 Turbo** | 30–60 | Variable | 16:9, 9:16, 1:1 | Image-to-video, controlled camera |
| **Kling variants** | Variable | 5s–10s | 16:9, 9:16, 1:1 | Athletic motion, dynamic physical movement |
| **Higgsfield Video** | 14–62 | Variable | Multiple | Budget-friendly video |
| **Wan Video** | 24 | Variable | Multiple | Affordable video generation |
| **Luma Ray 2** | Variable | Flexible | Multiple | Flexible duration |
| **Veo 3 Fast** | Low cost | Variable | Multiple | Atmospheric establishing shots |
| **LTX 2 Video Fast** | Budget | Variable | 16:9 | Quick draft tests |
| **LTX 2 Video Pro** | Moderate | Variable | 16:9 | Higher quality finals |

**Resolution range**: 480p to 1080p depending on model.

---

## PART 4: GENERATE FROM IMAGE MODELS

| Model | Credits | Mandatory Inputs | Key Feature |
|---|---|---|---|
| **Flux Dev Redux** | 3 | Image | 11 aspect ratio options; base image generation |
| **Flux ControlNet & LoRA** | 10 | Control Image | LoRA link support; edge/depth control |
| **Flux Canny Pro** | 6 | Prompt + Control Image | Edge-detection control |
| **Flux Depth Pro** | 6 | Prompt + Control Image | Depth control; multiple LoRAs |
| **Qwen Edit Multiangle** | 4 | Image + Prompt | Camera control options on toolbar |
| **Image to Image** | 10 | Prompt + Image | Standard img2img conversion |
| **Stable Diffusion ControlNets** | 1 | Prompt + Control Image | Most economical option |
| **Sketch to Image** | 0.1 | Prompt + Sketch Image | Lowest cost; sketch-based generation |

---

## PART 5: GENERATE FROM VIDEO MODELS

| Model | Credits | Mandatory Inputs | Key Feature |
|---|---|---|---|
| **Kling O1 Edit Video** | 147 | Prompt + Video | Keep Audio; multiple image inputs |
| **Kling O1 Reference Video to Video** | 92–184 | Prompt + Video Reference | 5s/10s duration; Keep Audio |
| **Kling Motion Control** | 50–80 | Image URL + Video URL | Pro/Standard tiers; Keep Audio |
| **LTX 2 Video to Video** | 30 | Prompt + Video | Generate Audio option |
| **Runway Aleph** | 66 | Prompt | 720p/580p/480p resolution |
| **Runway Act-Two** | 165–330 | Prompt | Character performance; 5s/10s |
| **Luma Reframe** | 320–600 | Prompt | Fast/Standard; Generate Audio |
| **Luma Modify** | 320–600 | Prompt | Fast/Standard; Generate Audio |
| **Wan 2.2 Animate - Replace** | 48–100 | Video + Character Image | Character replacement; 480p–720p |
| **Wan 2.2 Animate - Move** | 48–100 | Character Image + Driving Video | Character motion; 480p–720p |
| **Wan Vace Depth** | 300–400 | Prompt | Depth-based animation; 5s/8s |
| **Wan Vace Pose** | 18–176 | Prompt | Pose-controlled; Lite/Pro tiers |
| **Wan Vace Reframe** | 60–90 | Prompt | Sound effect and style options |
| **Wan Vace Outpainting** | 120 | Prompt + Video | Expand ratio control |
| **Hunyuan Video to Video** | 60 | Prompt + Video | 720p/580p/480p |

---

## PART 6: IMAGE ENHANCEMENT / UPSCALING MODELS

| Model | Credits | Outputs | Key Feature |
|---|---|---|---|
| **Topaz Upscale** | 19 | PNG, JPEG | General upscaling |
| **Topaz Sharpen** | 19 | PNG, JPEG, JPG, TIFF | Detail enhancement with style options |
| **Recraft Crisp Upscale** | 5 | PNG | Most economical upscaler |
| **Magnific Skin Enhancer** | 18 | PNG, JPEG | Facial focus; accepts optional prompt |
| **Magnific Upscale** | 12 | PNG, JPEG | 2X, 4X, 8X scaling options |
| **Magnific Precision Upscale** | 18 | PNG | Details and sharpening controls |
| **Magnific Precision Upscale V2** | 18 | PNG | Details and grain adjustments |
| **Enhancor Image Upscale** | 36 | PNG | Premium upscaling with modes |
| **Enhancor Realistic Skin** | 36 | PNG | Advanced skin work with detail controls |

---

## PART 7: IMAGE EDITING MODELS

### Inpainting

| Model | Credits | Inputs | Key Feature |
|---|---|---|---|
| **Flux Dev LoRA Inpaint** | 4 | Prompt + Image + Mask | LoRA + weight customization; multiple aspect ratios |
| **Ideogram V3 Inpaint** | 11 | Prompt + Image + Mask | Negative prompt; PNG output |
| **Ideogram V2 Inpaint** | 10 | Prompt + Image + Mask | Style reference images |
| **SD3 Inpaint** | 4 | Prompt + Image + Mask | Text-guided inpainting |
| **Bria Inpaint** | 5 | Prompt + Image + Mask | Multiple aspect ratios; PNG/JPEG |

### Outpainting

| Model | Credits | Inputs | Key Feature |
|---|---|---|---|
| **Flux Pro Outpaint** | 6 | Image | Flexible aspect ratios; PNG/JPEG |
| **SD3 Outpaint** | 5 | Image | Outpaint-specific aspect ratios |

### Background Manipulation

| Model | Credits | Inputs | Key Feature |
|---|---|---|---|
| **SD3 Remove Background** | 2 | Image | Returns original aspect ratio |
| **Bria Remove Background** | 0.6 | Image | Lowest cost background removal |
| **SD3 Content-Aware Fill** | 4 | Image + Mask | Intelligent fill |
| **Bria Content-Aware Fill** | 4 | Prompt + Image + Mask | Prompt-guided fill |
| **Replace Background** | 8 | Person image + Garment image | Multiple image inputs |
| **Bria Replace Background** | 2 | Background prompt + Image | Budget background replacement |

### Relighting

| Model | Credits | Inputs | Key Feature |
|---|---|---|---|
| **Relight 2.0** | 10 | Prompt + Image | Denoise and downscale options; PNG/JPEG |

### General-Purpose Editing

| Model | Credits | Inputs | Key Feature |
|---|---|---|---|
| **Gemini 3 Pro** | 15 | Prompt | Multiple image inputs |
| **Seedream V4.5 Edit** | 4 | Prompt + Image (optional) | Extensive aspect ratios incl. custom |
| **Reve Edit** | 4 | Prompt + Image | Preserves original aspect ratio |
| **Qwen Edit Image Plus** | 3 | Prompt + Image | Budget-friendly; multiple inputs |
| **Runway Gen-4 Image** | 6 | Prompt | Multiple aspect ratios; multiple images |
| **Seedream V4 Edit** | 4 | Prompt + Image | Custom aspect ratios |
| **Flux Kontext** | 3 | Prompt | Multiple aspect ratios; PNG/JPEG |
| **Flux Kontext Multi Image** | 10 | Image 1 + Image 2 | Dual image editing |
| **Flux Kontext LoRA** | 12 | Prompt | LoRA weight customization |
| **GPT Image 1.5 Edit** | 7 | Prompt + Image | Multiple image inputs |
| **GPT Image 1 Edit** | 8 | Prompt + Image | Multiple image inputs |
| **SeedEdit 3.0** | 4 | Prompt + Image | Standard editing |
| **Gemini 2.0 Flash** | 0.1 | Prompt + Image | Ultra-low cost (cheapest editor) |
| **Flux 2 Max** | 10 | Prompt | Premium editing; multiple aspect ratios |
| **Flux Fill Pro** | 6 | Prompt + Image + Mask | Fill with aspect ratio options |

---

## PART 8: VIDEO ENHANCEMENT MODELS

| Model | Credits | Key Feature |
|---|---|---|
| **Bria Video Upscale** | 154 | Premium upscaling; does not accept MOV with Alpha |
| **Topaz Video Upscaler** | 12 | Cost-effective upscaling |
| **Real-ESRGAN Video Upscaler** | 2 | Budget-friendly; 2K and 4K options; no MOV with Alpha |
| **Video Smoother** | 5 | Frame interpolation; output FPS customization |

---

## PART 9: LIP SYNC MODELS

| Model | Credits | Mandatory Inputs | Key Feature |
|---|---|---|---|
| **Omnihuman V1.5** | 352 | Audio + Image | Voice ID customization |
| **Sync 2 Pro** | 184 | Audio + Video | Video-based lip sync |
| **Pixverse Lipsync** | 66 | Video URL | Most affordable lip sync |
| **Kling AI Avatar Pro** | 253 | Image + Audio | Image-based with prompt support |

---

## PART 10: 3D MODELS

| Model | Credits | Inputs | Key Feature |
|---|---|---|---|
| **Sam 3D Objects** | 3 | Image + Prompt | Materials, T-pose mode |
| **Rodin** | 48 | Image | Materials, quality mesh options |
| **Rodin V2** | 36 | Image | Materials, quality mesh; newer version |
| **Meshy** | 4 | Image | Surface mode settings |
| **Meshy V6** | 96 | Image | Topology, remesh; texture prompt/image |
| **Hunyuan 3D V3** | 80 | Front image | Multi-view (back/left/right); polygon type |
| **Hunyuan 3D** | 18 | Front image | Multi-view support; target face number |
| **Hunyuan 3D V2.1** | 25 | Image | Textured mesh output |
| **Trellis** | 2 | Image | Texture size, mesh simplification; cheapest |

---

## PART 11: VECTOR MODELS

| Model | Credits | Inputs | Output Formats | Key Feature |
|---|---|---|---|---|
| **Vectorizer** | 24 | Image | SVG, EPS, PDF, DXF, PNG | Raster-to-vector; most format support |
| **Recraft V3 SVG** | 10 | Prompt | PNG | 14 resolution options |
| **Text To Vector** | 6 | Prompt | PNG | Negative prompt support; cheapest |

---

## QUICK REFERENCE: FREE NODES (0 Credits)

All editing tools, matte tools, iterators, helpers, and datatype nodes are free:

**Editing**: Levels, Compositor, Painter, Crop, Resize, Blur, Invert, Channels, Extract Video Frame
**Text**: Prompt, Prompt Concatenator
**Matte**: Mask Extractor, Mask By Text, Matte Grow/Shrink, Merge Alpha, Extract Video Matte, Video Mask by Text
**Iterators**: Text Iterator, Image Iterator, Video Iterator
**Helpers**: Import, Export, Preview, Router, Output, Sticky Note
**Datatypes**: Number, Text, Toggle, List Selector, Seed, Array

## QUICK REFERENCE: BUDGET MODELS (Under 5 Credits)

| Category | Model | Credits |
|---|---|---|
| Image Generation | Nvidia Sana | 0.2 |
| Image Generation | Flux Fast | 0.4 |
| Image Generation | Minimax Image 01 | 1 |
| Image Generation | Luma Photon | 2 |
| Image from Image | Sketch to Image | 0.1 |
| Image from Image | Stable Diffusion ControlNets | 1 |
| Image from Image | Flux Dev Redux | 3 |
| Image Editing | Gemini 2.0 Flash | 0.1 |
| Image Editing | Bria Remove Background | 0.6 |
| Image Editing | Bria Replace Background | 2 |
| Image Editing | Flux Kontext | 3 |
| Image Editing | Qwen Edit Image Plus | 3 |
| Image Upscaling | Recraft Crisp Upscale | 5 |
| Video Enhancement | Real-ESRGAN Video Upscaler | 2 |
| 3D | Trellis | 2 |
| 3D | Sam 3D Objects | 3 |
| 3D | Meshy | 4 |

---

## PART 13: WEAVY EDITOR & CANVAS

> Source: https://help.weavy.ai/en/collections/15341378-weavy-s-editor

### Canvas Navigation

The canvas is Weavy's primary creative workspace where all node-based workflows are built.

**Panning:**
- Click the hand tool in the toolbar or press **Space** to activate panning mode
- Mouse: Click and drag to pan in any direction; scroll to move up/down
- Trackpad: Click and drag to pan; two-finger scroll

**Zooming:**
- Keyboard + Mouse: Hold **⌘ Cmd** (Mac) or **Ctrl** (Windows) while scrolling up (zoom in) or down (zoom out)
- Trackpad: Two-finger pinch gesture

### Understanding Nodes

A node is a function with specific inputs (left side) and outputs (right side). Connect nodes by dragging from an output handle to a compatible input handle.

**Two categories:**

| Category | Description | Credits | Examples |
|---|---|---|---|
| **Generative AI Nodes** | Feature a "Run" button, generate new content from inputs | Yes — per generation | Image generators, video generators, upscalers |
| **Non-Generative Nodes** | Manual tools and utilities, no AI generation | Free | Painter, Blur, Prompt Concatenator, Compositor |

**Node color coding:**

| Color | Content Type |
|---|---|
| Green | Image |
| Purple | Text / LoRA |
| Red | Video |
| Blue | Array / List / 3D |
| White | Multiple inputs |
| Lime | Mask |

**Running a model node:** Ensure all required inputs are connected, then click the "Run" button on the node. Node properties (aspect ratio, prompt adherence, model-specific settings) appear in the right-side panel when selected.

### Working with Media

**Viewing:** Click the gallery icon (bottom-right of media node) or hover and press **Space** to open gallery view.

**Downloading:**
- Right-click a node → "Download current" (single) or "Download all" (everything in node)
- Three-dot menu (top-right) for additional options
- Gallery view: download button at top-right; option to generate shareable links

**Generation history:** Open gallery view → "Show info" to see prompt, parameters, settings, seed number, and technical details for any generation.

### Importing Custom Models

Weavy supports importing models from three platforms:

| Source | How to Import |
|---|---|
| **Replicate** | Copy the model's page URL → paste into Import Model node |
| **Fal** | Copy the model's name → paste into Import Model node |
| **CivitAI** | Copy the model URL → paste into Import Model node |

**Steps:**
1. Drag "Import Model" node onto canvas from Toolbox (or press **Tab** and search)
2. Paste the URL or model name from your chosen source
3. Parameters auto-populate in the right-side toolbar
4. Click "Save model to my library" to reuse across all workflows (appears under "My Models" in left menu)

### Importing LoRAs

LoRA (Low-Rank Adaptation) models customize base AI models with specific styles, characters, or concepts.

**Import steps:**
1. Open toolbox or right-click canvas → search "LoRA" → select "Import LoRA"
2. Click the node → "Upload" → choose your LoRA file
3. Connect to a compatible model (e.g., **FluxDev LoRA**)
4. Connect text prompt to the model's prompt input; connect LoRA node to "LoRA1"

**Strength control:** Add a Number node (set type to "float") and connect to "LoRA1 scale":
- **1** = full strength
- **0–1 decimals** = subtle effects (e.g., 0.7 for 70% influence)

**Stacking LoRAs:** Up to **2 LoRAs** can be stacked — connect second LoRA to "LoRA2" with its own strength via "LoRA2 scale".

**Tips:**
- Test different strength values to balance LoRA style with base model output
- Not all LoRA combinations work well together — experiment
- FluxDev LoRA is the primary supported model in Weavy
- External models from Replicate and CivitAI may have specific input requirements

### The Design App

The Design App turns any workflow into a reusable, shareable application — "a design machine with your own chosen attributes."

**Creating a Design App:**
1. Add an **Output node** and connect it to your workflow's final result
2. The **App** tab unlocks at the top of the canvas
3. Only nodes without inputs (prompts, image imports) appear as adjustable parameters
4. To hide parameters from end users, set nodes to "locked" mode (three-dot menu → lock icon)

**Publishing & sharing:**
- Click **Publish** in the App tab to save a version
- Use **Share** (top-right) to distribute — shared users see it in app mode only
- Users can modify parameters without affecting your original workflow
- Re-publishing automatically updates everyone's version

**Version management:** Each publish creates a timestamped version. View history via the dropdown next to the Publish button. Historical versions are read-only.

### Managing Node Files

**Remove a single file:** Three-dot menu (top-right of node) → "Remove Current Generation"

**Keep only one file:** Three-dot menu → "Remove All Other Generations" (keeps the selected file, removes everything else)

### Grouping & Ungrouping Nodes

Groups organize related nodes visually on the canvas.

**Group:** Select nodes → **Ctrl+G** (Windows) / **⌘+G** (Mac), or right-click → "Group Selection"

**Customize groups:**
- Click the group title to rename
- Right-click → "Title Size" to adjust text prominence
- Right-click → "Color" to change group color
- Right-click → "Resize to Fit" to eliminate extra space

**Move:** Click empty space within the group and drag (moves all nodes together). Individual nodes can be rearranged inside — the group auto-expands as needed.

**Ungroup:** Right-click → "Ungroup" (removes group entirely)
**Remove one node from group:** Three-dot menu on the node → "Remove from Group"

### Preferences Settings

Access via: **Weavy icon** (top-left) → scroll down → **Preferences**

Preferences are toggleable options for customizing editor behavior. Enable all options or only select ones based on your workflow needs.

---

## QUICK REFERENCE: KEYBOARD SHORTCUTS

| Action | Shortcut |
|---|---|
| Pan canvas | **Space** + drag |
| Zoom in/out | **⌘/Ctrl** + scroll |
| Search nodes | **Tab** |
| Group nodes | **⌘/Ctrl + G** |
| View media | Hover node + **Space** |
