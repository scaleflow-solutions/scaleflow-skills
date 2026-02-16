# Presentation Style Guide

This reference contains the design intelligence for the Deck Creator skill. It covers visual styles, layout patterns, typography pairings, and design techniques achievable in .pptx format using PptxGenJS.

## Visual Style Presets

When the user is asked "What visual style?", these are the options with their pptx implementation approach:

### Glassmorphism
- Semi-transparent shape fills with soft edges (use `transparency: 70-80%` on rectangles with rounded corners)
- Frosted panel effect: light-colored shape over a gradient or image background
- Subtle borders (`line` property with low-opacity white or light gray)
- Gradient backgrounds from deep color to slightly lighter variant
- Works best with: dark backgrounds, photography-heavy decks, premium brands

### Neubrutalism
- Bold black borders on all elements (`line: { width: 3, color: '000000' }`)
- Flat, saturated color fills — no gradients, no transparency
- Slightly offset shadow rectangles behind main elements (second shape offset +4px right, +4px down)
- Chunky typography: Impact or Arial Black headers at 40pt+
- Works best with: bold brands, youth-oriented campaigns, social-first content

### Minimalist
- Maximum whitespace — content occupies 40-50% of slide area
- Thin typography: Calibri Light or similar
- Single accent color against white/off-white backgrounds
- No borders, no shadows, no gradients — just type and space
- Works best with: executive presentations, premium brands, data-heavy content

### Editorial
- Asymmetric layouts — text blocks and images don't center-align
- Serif typography for headlines (Georgia, Cambria, Palatino)
- Full-bleed photography with text overlays using contrast bars
- Muted color palette: deep charcoals, warm grays, single accent
- Works best with: storytelling decks, brand campaigns, annual reports

### Bold Gradient
- Full-slide gradient backgrounds (diagonal or radial)
- White text for maximum contrast
- Geometric accent shapes (circles, diagonal stripes) with transparency
- Sans-serif typography: Arial Black headers, Calibri body
- Works best with: energetic brands, sports campaigns, launch events

### Corporate Clean
- Light gray backgrounds (#F5F5F5) with white content cards
- Subtle drop shadows on content blocks
- Two-column layouts with clear grid alignment
- Conservative typography: Calibri headers, Calibri Light body
- Works best with: internal reviews, stakeholder presentations, budget decks

## Dimensionality Options

### 3D Depth Effects (in pptx)
- Layered shapes with offset shadows to simulate depth
- Background shape at 30% opacity, mid-ground at 60%, foreground at 100%
- Slight rotation on image frames (1-2 degrees) for visual interest
- Shadow properties: `shadow: { type: 'outer', blur: 8, offset: 4, angle: 45, color: '000000', opacity: 0.3 }`
- Gradient fills on shapes to simulate lighting

### Flat 2D
- No shadows, no gradients on shapes
- Solid color fills only
- Clean edges with consistent border weights
- Emphasis through color contrast and size, not depth

## Image Handling Options

### Placeholder Images with Descriptions
- Gray rectangles (#E0E0E0) with centered italic text describing what should go there
- Example: *"Hero key visual — athlete mid-sprint, stadium background, dramatic lighting"*
- Include dimensions in small text below: "1920 x 1080px"

### AI-Generated Placeholders
- Generate simple branded color blocks with the brand's primary color at 20% opacity
- Center the brand logo watermark if available
- Label with asset description

### Empty Frames with Specs
- Thin-bordered empty rectangles with dimension labels
- Clean and professional — for when the client will provide assets

## Layout Density

### Breathing Space (recommended for client decks)
- 1-2 key points per slide maximum
- 60%+ whitespace
- Large images, minimal text
- Speaker notes carry the detail

### Balanced (recommended for team reviews)
- 3-4 points per slide
- 40% whitespace
- Mix of text, images, and data elements

### Information-Dense (for internal/data decks only)
- Tables, charts, and multi-column layouts
- 20-30% whitespace
- Detailed text — these slides are meant to be read, not presented

## Multi-Brand Presentations

When multiple brands appear in a deck:

### Title Slide
- User's agency logo in bottom-left or top-left corner
- Client brand logo centered or prominent
- Partner logos in a row at bottom if applicable
- Clear visual hierarchy: client brand is the hero, agency brand is the signature

### Content Slides
- Agency branding in footer or corner (consistent, small, unobtrusive)
- Client brand elements integrated into content where relevant
- Never mix brand color systems within a single slide — use the client's palette for content, agency palette for structural elements (footer, slide numbers)

### Closing Slide
- Both logos with "Presented by [Agency] for [Client]" format
- Contact information uses agency branding

## Typography Pairings for PptxGenJS

Since PptxGenJS uses system-installed fonts, these pairings are safe:

| Style | Header | Body | Best For |
|-------|--------|------|----------|
| **Premium** | Georgia (36-44pt bold) | Calibri (14-16pt) | Luxury, editorial |
| **Bold Impact** | Impact (40-48pt) | Arial (14-16pt) | Sports, energy |
| **Modern Clean** | Calibri (36-44pt bold) | Calibri Light (14-16pt) | Corporate, tech |
| **Classic** | Cambria (36-44pt bold) | Garamond (14-16pt) | Heritage, tradition |
| **Playful** | Trebuchet MS (36-44pt bold) | Calibri (14-16pt) | Youth, casual |
| **Technical** | Consolas (32-40pt bold) | Calibri (14-16pt) | Data, dev-oriented |

## Slide Transition Techniques

In pptx format, transitions are limited. Achieve visual flow through:

- **Consistent element positioning** — keep titles, logos, and navigation in the same spot across slides
- **Color progression** — gradually shift background shade across sections (Act 1 = light, Act 2 = dark for creative, Act 3 = light for details)
- **Reveal builds** — split one visual across 2-3 slides, revealing more each time
- **Section divider slides** — full-color slides with single section title marking transitions between acts

## Color Palette Generation

When building from brand colors:

1. **Primary** (60% usage): Brand's main color for backgrounds, headers
2. **Secondary** (25% usage): Complementary tone for content blocks, borders
3. **Accent** (10% usage): Contrast color for CTAs, highlights, key stats
4. **Neutral** (5% usage): Off-white or dark gray for text backgrounds
5. **Text colors**: Always ensure WCAG AA contrast ratio — dark text on light, light text on dark

### Deriving Extended Palette from Brand Colors
- Lighten primary by 40% for subtle backgrounds
- Darken primary by 30% for text on light backgrounds
- Use accent sparingly — only for the single most important element per slide
