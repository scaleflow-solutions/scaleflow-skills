# ScaleFlow Skills

AI-powered creative production skills for Claude. Built for creative agencies and production teams running campaigns on [Weavy AI](https://weavy.ai).

12 skills across 3 packs — from brief to final delivery.

---

## How It Works

```
Brief → Creative Direction → Production → Delivery
```

| Phase | Skills | Output |
|-------|--------|--------|
| **Understand the brief** | Brief Analyzer | Structured creative direction document |
| **Define the creative** | Moodboard Curator, Copy Engine | Visual direction + platform copy |
| **Plan the production** | Prompt Architect, Storyboard Writer, Workflow Architect | Model-ready prompts, shot lists, Weavy canvas blueprints |
| **Manage the budget** | Credit Optimizer | Credit budget with model recommendations |
| **Execute & QA** | Creative Review, Asset Spec | QA verdicts + export specs |
| **Deliver** | Deck Creator, Report Builder, SOP Writer | Presentations, reports, repeatable SOPs |

Each skill reads upstream outputs automatically — Brief Analyzer feeds Prompt Architect, which feeds Storyboard Writer, and so on. Use them individually or as a full pipeline.

---

## 3 Packs — 12 Skills

### Creative Suite (5 skills)

| Skill | Purpose | Key Output |
|-------|---------|------------|
| **Brief Analyzer** | Breaks down client briefs into structured creative direction with Weavy pipeline recommendations | `.docx` Creative Direction Document |
| **Copy Engine** | Generates platform-specific ad copy with brand voice control and character limit validation | `.docx` Copy Package |
| **Moodboard Curator** | Curates visual direction boards with reference imagery and style parameters | `.docx` Visual Direction Document |
| **Prompt Architect** | Engineers production-ready prompts optimized for Flux, Ideogram, Kling, Runway, and 100+ Weavy models | `.docx` Prompt Package |
| **Storyboard Writer** | Creates shot-by-shot video storyboards with per-shot Weavy pipeline mapping | `.docx` Storyboard |

### Production Ops (5 skills)

| Skill | Purpose | Key Output |
|-------|---------|------------|
| **Workflow Architect** | Designs node-by-node Weavy canvas workflows — translates deliverables into concrete production blueprints | `.md` Workflow Blueprint |
| **Credit Optimizer** | Plans and optimizes AI credit budgets across 90+ models with plan tier comparisons | `.docx` Credit Budget |
| **Creative Review** | QA reviews generated assets against the brief, brand guidelines, and technical specs | `.docx` Creative Review |
| **Asset Spec** | Generates export specifications with dimensions, formats, naming conventions, and folder structures | `.docx` Asset Spec |
| **SOP Writer** | Documents repeatable workflows as step-by-step SOPs with Weavy node workflow maps | `.docx` Standard Operating Procedure |

### Client Delivery (2 skills)

| Skill | Purpose | Key Output |
|-------|---------|------------|
| **Deck Creator** | Builds client presentation decks with 6 visual styles, speaker notes, and brand styling | `.pptx` Presentation Deck |
| **Report Builder** | Generates post-project reports with deliverables inventory, credit usage, and recommendations | `.docx` Project Report |

---

## Shared Resources

All skills draw from a common resource layer:

| Resource | What It Contains |
|----------|-----------------|
| `shared/brand-profile-template.md` | Brand identity template — colors, typography, logo, tone of voice |
| `shared/generate_branded_docx.py` | Branded `.docx` generator used by 9 skills |
| `shared/weavy-nodes-and-models-reference.md` | Complete Weavy platform reference — 100+ models, 30+ free nodes, editor & canvas operations |

---

## Scripts

5 production scripts bundled with their skills:

| Script | Skill | What It Does |
|--------|-------|-------------|
| `calculate_budget.py` | Credit Optimizer | Calculates credit costs from a deliverables JSON |
| `validate_copy_lengths.py` | Copy Engine | Validates copy against 22 platform character limits |
| `validate_assets.py` | Asset Spec | Validates exported files against spec (dimensions, format, DPI) |
| `check_image_specs.py` | Creative Review | Technical QA on images with auto platform suggestions |
| `generate_pptx.py` | Deck Creator | Generates branded PowerPoint from JSON slide data |

---

## Install

### Claude.ai
1. Download this repo as a `.zip`
2. Go to **Settings** → **Skills**
3. Upload the zip

### Claude Code
Place the skill folders in your Claude Code skills directory.

### Cowork
1. Open **Cowork** → **Settings** → **Plugins**
2. Add marketplace: `scaleflow-solutions/scaleflow-skills`
3. Install the packs you need

---

## Structure

```
scaleflow-skills/
├── scaleflow-creative-suite/
│   └── skills/
│       ├── brief-analyzer/
│       ├── copy-engine/
│       ├── moodboard-curator/
│       ├── prompt-architect/
│       └── storyboard-writer/
├── scaleflow-production-ops/
│   └── skills/
│       ├── workflow-architect/
│       ├── credit-optimizer/
│       ├── creative-review/
│       ├── asset-spec/
│       └── sop-writer/
├── scaleflow-client-delivery/
│   └── skills/
│       ├── deck-creator/
│       └── report-builder/
└── shared/
    ├── brand-profile-template.md
    ├── generate_branded_docx.py
    └── weavy-nodes-and-models-reference.md
```

---

## License

MIT — Built by [ScaleFlow](https://github.com/scaleflow-solutions)
