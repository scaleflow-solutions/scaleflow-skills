# Platform Dimension & Format Specifications

Last updated: February 2026. Update this file when platforms change their requirements.

## Social Media — Static Images

| Platform | Format | Dimensions (px) | Aspect Ratio | File Type | Max Size |
|---|---|---|---|---|---|
| Instagram Feed | Square | 1080 × 1080 | 1:1 | JPG, PNG | 30 MB |
| Instagram Feed | Portrait | 1080 × 1350 | 4:5 | JPG, PNG | 30 MB |
| Instagram Feed | Landscape | 1080 × 566 | 1.91:1 | JPG, PNG | 30 MB |
| Instagram Story | Full screen | 1080 × 1920 | 9:16 | JPG, PNG | 30 MB |
| Instagram Carousel | Per slide | 1080 × 1080 | 1:1 | JPG, PNG | 30 MB |
| TikTok | Vertical | 1080 × 1920 | 9:16 | JPG, PNG | — |
| Twitter/X | Single image | 1200 × 675 | 16:9 | JPG, PNG, GIF | 5 MB |
| Twitter/X | Card | 1200 × 628 | 1.91:1 | JPG, PNG | 5 MB |
| LinkedIn | Feed post | 1200 × 627 | 1.91:1 | JPG, PNG | 10 MB |
| LinkedIn | Square | 1080 × 1080 | 1:1 | JPG, PNG | 10 MB |
| Facebook | Feed | 1200 × 630 | 1.91:1 | JPG, PNG | 30 MB |
| Facebook | Story | 1080 × 1920 | 9:16 | JPG, PNG | 30 MB |
| YouTube | Thumbnail | 1280 × 720 | 16:9 | JPG, PNG | 2 MB |

## Social Media — Video

| Platform | Format | Dimensions | Aspect Ratio | Duration | File Type | Max Size |
|---|---|---|---|---|---|---|
| Instagram Reel | Vertical | 1080 × 1920 | 9:16 | 3-90 sec | MP4 | 650 MB |
| Instagram Story | Vertical | 1080 × 1920 | 9:16 | up to 60 sec | MP4 | 650 MB |
| Instagram Feed | Square | 1080 × 1080 | 1:1 | 3-60 sec | MP4 | 650 MB |
| TikTok | Vertical | 1080 × 1920 | 9:16 | 3-10 min | MP4 | 287 MB |
| YouTube | Landscape | 1920 × 1080 | 16:9 | any | MP4 | 256 GB |
| YouTube | 4K | 3840 × 2160 | 16:9 | any | MP4 | 256 GB |
| YouTube Shorts | Vertical | 1080 × 1920 | 9:16 | up to 3 min | MP4 | — |
| Twitter/X | Any | 1920 × 1080 | 16:9 | 0.5-140 sec | MP4 | 512 MB |
| LinkedIn | Landscape | 1920 × 1080 | 16:9 | 3 sec-10 min | MP4 | 5 GB |
| Facebook | Any | 1920 × 1080 | varies | up to 240 min | MP4 | 10 GB |

## Video Technical Specs

| Setting | Web Delivery | Broadcast | Archive |
|---|---|---|---|
| Codec | H.264 | ProRes 422 | ProRes 422 HQ |
| Container | MP4 | MOV | MOV |
| Frame rate | 24/30 fps | 24/25/30 fps | Match source |
| Bitrate (1080p) | 10-20 Mbps | 50+ Mbps | 100+ Mbps |
| Bitrate (4K) | 35-50 Mbps | 100+ Mbps | 200+ Mbps |
| Audio codec | AAC | PCM/WAV | PCM/WAV |
| Audio bitrate | 128-256 kbps | Uncompressed | Uncompressed |
| Color space | sRGB/Rec.709 | Rec.709 | Rec.709 |

## Print & Out-of-Home

| Format | Typical Dimensions | DPI | Color Space | File Type |
|---|---|---|---|---|
| Billboard (48-sheet) | 6096 × 3048 mm | 150-300 DPI | CMYK | PDF, TIFF |
| Bus shelter | 1800 × 1200 mm | 300 DPI | CMYK | PDF, TIFF |
| A3 poster | 297 × 420 mm | 300 DPI | CMYK | PDF, TIFF |
| A4 flyer | 210 × 297 mm | 300 DPI | CMYK | PDF, TIFF |
| Stadium LED | Varies by venue | 72-150 DPI | RGB | PNG, MP4 |

**CMYK Conversion Note:** All AI-generated assets are RGB. CMYK conversion must be done in Photoshop, Illustrator, or a dedicated color management tool before print production. Colors will shift — always proof.

## 3D Asset Formats

| Format | Extension | Best For |
|---|---|---|
| glTF / GLB | .gltf / .glb | Web viewers, Three.js, e-commerce |
| USDZ | .usdz | Apple AR (Quick Look) |
| OBJ | .obj | General editing, 3D software import |
| FBX | .fbx | Animation, game engines |
| STL | .stl | 3D printing |

## Web Assets

| Format | Use | Notes |
|---|---|---|
| WebP | Web images | 25-34% smaller than JPG, supported by all modern browsers |
| AVIF | Web images (next-gen) | Even smaller, growing support |
| SVG | Icons, logos | Vector, infinitely scalable |
| PNG | Transparency needed | Larger files, use only when transparency required |
| JPG | Photos, no transparency | Best compression for photographic content |
