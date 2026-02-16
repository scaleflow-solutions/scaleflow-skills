# Brand Profile

This file stores the brand identity for the current workspace. It is created once (the first time any ScaleFlow skill needs brand context) and read silently by all skills in every future session. The user should never need to re-enter this information unless they want to update it.

## How This File is Created

When any ScaleFlow skill detects that this file does not exist in the workspace, it should:

1. Ask the user: "I don't have your brand on file yet. Let me set that up so you never have to repeat it."
2. Collect the following through feedback questions:
   - Brand name
   - Upload logo (save to workspace as `brand-assets/logo.png`)
   - Primary color, secondary color, accent color (hex codes)
   - Typography preference: modern / classic / bold / minimal / editorial
   - Brand voice keywords (e.g., bold, premium, playful, authoritative, warm)
   - Industry or sector (e.g., sports marketing, fashion, FMCG, tech)
   - Optionally: upload a brand guidelines PDF (save to workspace as `brand-assets/brand-guide.pdf`)
3. Save this file to the workspace root as `brand-profile.md`
4. Proceed with the original task

## How Skills Use This File

Every skill should check for `brand-profile.md` at the start of execution:

- **If found**: Read it silently and incorporate brand context into the output. Do NOT ask the user any brand-related questions.
- **If not found**: Trigger the setup flow above before proceeding.
- **If the user says "update my brand"**: Re-run the setup flow and overwrite this file.

## Brand Profile Fields

```
Brand Name: [name]
Industry: [sector]

Primary Color: #[hex]
Secondary Color: #[hex]
Accent Color: #[hex]
Background Preference: dark / light / neutral

Typography Style: modern / classic / bold / minimal / editorial
Heading Font (if specified): [font name or "not specified"]
Body Font (if specified): [font name or "not specified"]

Brand Voice: [comma-separated keywords — e.g., bold, premium, confident, warm]

Logo File: brand-assets/logo.png
Brand Guide PDF: brand-assets/brand-guide.pdf (or "not provided")

Additional Notes: [any extra context the user provided]
```

## Per-Project Brand Context (NOT saved here)

Some projects involve other brands (client brands, partner logos, co-branding). These are asked per project through feedback loops and are NOT persisted in this file. Skills should ask:

- "Are there other brands involved in this project? Upload their logos and provide their brand colors if you have them."
- Save per-project brand assets temporarily in the working directory, not in the persistent brand profile.
