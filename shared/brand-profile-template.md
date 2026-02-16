# Brand Profile System

This file defines how brand identity is captured, stored, and used across all ScaleFlow skills. Every skill MUST check for a brand profile before doing any work.

---

## Storage Location

Brand profiles are saved as `brand-profile.md` in the workspace root.
Brand assets (logo, brand guide PDF) are saved in a `brand-assets/` folder in the workspace root.

These persist across sessions. Once created, the user never needs to re-enter brand information.

---

## Brand Profile Check — Every Skill Must Do This

At the very start of execution, before any other work, every ScaleFlow skill MUST:

1. Check if `brand-profile.md` exists in the workspace root.
2. **If it exists**: Read it silently. Verify it has all required fields (Brand Name, Colors, Typography Style, Brand Voice, Industry). If any required field is empty or says "not specified", use the `AskUserQuestion` tool to ask for ONLY the missing fields. Do NOT re-ask fields that are already filled.
3. **If it does NOT exist**: Run the Brand Onboarding Flow below. Do NOT skip this. Do NOT proceed without it.

**If the user tries to skip brand setup**, say: *"The brand profile is required — it controls the colors, typography, and tone across every document and asset I create for you. It takes about a minute and you'll never need to do it again."*

---

## Brand Onboarding Flow

When `brand-profile.md` does not exist, collect brand information using the `AskUserQuestion` tool. Use structured questions with predefined options wherever possible. This ensures consistent, usable data.

### Question 1: Brand Name and Industry

Use the `AskUserQuestion` tool to ask:
- "What is your brand name?"
- "What industry or sector are you in?"

Provide industry options: Sports & Fitness / Fashion & Lifestyle / Food & Beverage / Technology / Healthcare / Real Estate / Education / Entertainment / Retail & E-commerce / Other

### Question 2: Brand Colors

Use the `AskUserQuestion` tool to ask:
- "What are your brand colors? I need a primary color, secondary color, and accent color. Hex codes are ideal (e.g., #FF5722), but color names work too — I'll convert them."

If the user provides color names instead of hex codes, convert them to the closest standard hex value and confirm with the user.

If the user has uploaded a brand guide PDF or logo, extract colors from those files first and confirm: *"I found these colors in your brand guide: [colors]. Should I use these?"*

### Question 3: Typography and Visual Style

Use the `AskUserQuestion` tool with these options:
- "What typography style fits your brand?"
- Options: Modern (clean sans-serif) / Classic (elegant serif) / Bold (strong, heavy weights) / Minimal (thin, lots of whitespace) / Editorial (magazine-style, mixed weights)

### Question 4: Brand Voice

Use the `AskUserQuestion` tool to ask:
- "Describe your brand voice in 3-5 keywords."

Provide example sets to guide the user:
- Bold, Premium, Confident
- Warm, Approachable, Playful
- Professional, Authoritative, Trustworthy
- Edgy, Disruptive, Young
- Elegant, Refined, Understated

### Question 5: Logo and Brand Guide Upload

Ask the user:
- "Do you have a logo file you can upload? (PNG or SVG preferred)"
- "Do you have a brand guidelines PDF? (optional but helpful — I'll extract colors, fonts, and usage rules from it)"

If the user uploads files:
- Save the logo as `brand-assets/logo.png` (or `.svg` if SVG)
- Save the brand guide as `brand-assets/brand-guide.pdf`
- If a brand guide PDF is uploaded, read it and extract any additional brand information (fonts, color palette, logo usage rules, tone of voice details). Update the brand profile fields accordingly.

### Question 6: Background Preference

Use the `AskUserQuestion` tool with options:
- "What background style do your materials usually use?"
- Options: Dark backgrounds / Light backgrounds / Neutral (varies by project)

---

## Saving the Brand Profile

After collecting all answers, save `brand-profile.md` to the workspace root using this exact format:

```
Brand Name: [name]
Industry: [sector]

Primary Color: #[hex]
Secondary Color: #[hex]
Accent Color: #[hex]
Background Preference: [dark / light / neutral]

Typography Style: [modern / classic / bold / minimal / editorial]
Heading Font: [font name or "not specified"]
Body Font: [font name or "not specified"]

Brand Voice: [comma-separated keywords]

Logo File: brand-assets/logo.png [or "not provided"]
Brand Guide PDF: brand-assets/brand-guide.pdf [or "not provided"]

Additional Notes: [any extra context from the brand guide or user]
```

After saving, confirm: *"Brand profile saved. I'll use this automatically on every project — your colors, typography, and voice will carry through every document, presentation, and asset."*

---

## How Skills Use the Brand Profile

Once loaded, skills apply brand context as follows:

| Field | How It's Used |
|---|---|
| Brand Name | Document headers, file naming, slide titles |
| Colors (hex) | Document accent colors, chart colors, slide themes, prompt color references |
| Typography Style | Document font selection, slide font pairing, visual style direction |
| Brand Voice | Tone of all copy, writing style, messaging approach |
| Industry | Audience assumptions, platform priorities, benchmark references |
| Logo File | Document headers, slide title/closing pages, watermarks |
| Brand Guide PDF | Source of truth for any detailed brand questions |

---

## Updating the Brand Profile

If the user says "update my brand", "change my brand colors", "here's my logo", or similar:

1. Read the current `brand-profile.md`
2. Use `AskUserQuestion` to ask which fields they want to update (unless they already specified, e.g., "here's my logo")
3. Update only those fields
4. Save the updated file

### Logo Upload at Any Time

If the user uploads a logo file at any point during any skill:
- Save it as `brand-assets/logo.png` (or `.svg` if SVG format). Create the `brand-assets/` directory if it doesn't exist.
- Update the `Logo File` field in `brand-profile.md` to `brand-assets/logo.png`
- Confirm: *"Logo saved. I'll include it in all future documents, presentations, and branded outputs."*

### Brand Guide PDF Upload at Any Time

If the user uploads a brand guidelines PDF at any point:
- Save it as `brand-assets/brand-guide.pdf`
- Read the PDF and extract any new information (fonts, color palette, logo rules, tone of voice details)
- Use `AskUserQuestion` to confirm extracted updates: *"I found these details in your brand guide: [details]. Should I update your brand profile with these?"*
- If confirmed, update `brand-profile.md` with the new information
- Update the `Brand Guide PDF` field to `brand-assets/brand-guide.pdf`

### Key Rule: Any skill can trigger an update

Brand profile updates are NOT limited to a "brand setup" moment. If a user provides brand assets (logo, colors, guide PDF) during ANY skill execution — Brief Analyzer, Deck Creator, Copy Engine, etc. — that skill MUST save the assets and update `brand-profile.md` immediately. The profile is a living document, not a one-time setup.

---

## Per-Project Brand Context

Some projects involve additional brands (client brands, partner logos, co-branding). These are NOT saved in the persistent brand profile. When a project involves other brands:

- Ask: *"Are there other brands involved in this project besides [Brand Name]?"*
- If yes, collect their colors, logos, and guidelines as project-specific files in the working directory
- Do NOT overwrite the main brand profile
