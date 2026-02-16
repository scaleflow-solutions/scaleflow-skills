#!/usr/bin/env python3
"""
ScaleFlow Credit Budget Calculator

Calculates estimated Weavy AI credit costs for a project based on deliverables.
Reads the credit table from references/weavy-credit-table.md and produces a
formatted budget breakdown.

Usage:
    python scripts/calculate_budget.py --plan starter --deliverables deliverables.txt
    python scripts/calculate_budget.py --plan professional --interactive

The deliverables file should list one deliverable per line in format:
    [count] x [type] using [model]
    Example:
    3 x hero_image using flux_kontext
    5 x social_static using ideogram_v3
    2 x video_15sec using kling_2_1
    1 x 3d_product using trellis_3d
"""

import argparse
import sys

# Credit costs per model per plan tier
CREDIT_COSTS = {
    "starter": {
        "flux_fast": 375,
        "flux_dev_lora": 38,
        "flux_kontext": 50,
        "minimax_image": 150,
        "ideogram_v3": 38,
        "gpt_image_edit": 19,
        "runway_gen4_image": 25,
        "mystic": 13,
        "imagen_4": 25,
        "topaz_image_upscale": 8,
        "magnific_upscale": 13,
        "veo_3_fast": 13,
        "seedance_v1": 88,
        "runway_gen4_turbo": 75,
        "ltx_2_fast": 38,
        "ltx_2_pro": 25,
        "kling_2_1": 88,
        "minimax_hailuo": 63,
        "wan_vace": 75,
        "runway_act_two": 38,
        "topaz_video_upscale": 13,
        "trellis_3d": 75,
        "rodin_3d": 38,
        "hunyuan_3d": 100,
    },
    "professional": {
        "flux_fast": 250,
        "flux_dev_lora": 25,
        "flux_kontext": 33,
        "minimax_image": 100,
        "ideogram_v3": 25,
        "gpt_image_edit": 13,
        "runway_gen4_image": 17,
        "mystic": 8,
        "imagen_4": 17,
        "topaz_image_upscale": 5,
        "magnific_upscale": 8,
        "veo_3_fast": 8,
        "veo_3": 333,
        "seedance_v1": 58,
        "runway_gen4_turbo": 50,
        "ltx_2_fast": 25,
        "ltx_2_pro": 17,
        "kling_2_1": 58,
        "minimax_hailuo": 42,
        "wan_vace": 50,
        "runway_act_two": 25,
        "topaz_video_upscale": 8,
        "trellis_3d": 50,
        "rodin_3d": 25,
        "hunyuan_3d": 67,
    },
    "team": {
        "flux_fast": 225,
        "flux_dev_lora": 23,
        "flux_kontext": 30,
        "minimax_image": 90,
        "ideogram_v3": 23,
        "gpt_image_edit": 11,
        "runway_gen4_image": 15,
        "mystic": 8,
        "imagen_4": 15,
        "topaz_image_upscale": 5,
        "magnific_upscale": 8,
        "veo_3_fast": 8,
        "veo_3": 300,
        "seedance_v1": 53,
        "runway_gen4_turbo": 45,
        "ltx_2_fast": 23,
        "ltx_2_pro": 15,
        "kling_2_1": 53,
        "minimax_hailuo": 38,
        "wan_vace": 45,
        "runway_act_two": 23,
        "topaz_video_upscale": 8,
        "trellis_3d": 45,
        "rodin_3d": 23,
        "hunyuan_3d": 60,
    },
}

PLAN_CREDITS = {
    "starter": 1500,
    "professional": 4000,
    "team": 4500,
}

# Average iterations needed per asset type
ITERATION_MULTIPLIERS = {
    "hero_image": 4,       # 4 generations to get 1 usable hero
    "social_static": 2,    # Simpler, fewer iterations
    "video_15sec": 5,      # Video is most iteration-heavy
    "video_30sec": 8,      # Longer video = more iterations
    "3d_product": 4,       # 3D is unpredictable
    "product_shot": 3,     # Moderate iteration
    "text_graphic": 2,     # Ideogram is reliable with text
    "upscale": 1,          # Enhancement is one-shot
    "edit": 2,             # Edits may need refinement
}


def calculate_budget(deliverables, plan):
    """Calculate total estimated credits for a list of deliverables."""
    costs = CREDIT_COSTS.get(plan, CREDIT_COSTS["starter"])
    results = []
    total = 0

    for count, asset_type, model in deliverables:
        cost_per_gen = costs.get(model, 0)
        iterations = ITERATION_MULTIPLIERS.get(asset_type, 3)
        line_total = count * cost_per_gen * iterations
        total += line_total
        results.append({
            "count": count,
            "asset_type": asset_type,
            "model": model,
            "cost_per_gen": cost_per_gen,
            "iterations": iterations,
            "line_total": line_total,
        })

    available = PLAN_CREDITS.get(plan, 1500)
    buffer = int(total * 0.2)

    return {
        "results": results,
        "total": total,
        "buffer": buffer,
        "total_with_buffer": total + buffer,
        "available": available,
        "surplus_or_shortfall": available - (total + buffer),
    }


def format_budget(budget, plan):
    """Format budget as readable text output."""
    lines = []
    lines.append(f"CREDIT BUDGET — {plan.upper()} PLAN")
    lines.append(f"{'='*60}")
    lines.append("")
    lines.append(f"{'Deliverable':<20} {'Model':<20} {'×Gen':<6} {'Iter':<5} {'Total':<8}")
    lines.append(f"{'-'*60}")

    for r in budget["results"]:
        lines.append(
            f"{r['count']}x {r['asset_type']:<16} {r['model']:<20} "
            f"{r['cost_per_gen']:<6} ×{r['iterations']:<4} {r['line_total']:<8}"
        )

    lines.append(f"{'-'*60}")
    lines.append(f"{'Estimated total:':<46} {budget['total']}")
    lines.append(f"{'Buffer (20%):':<46} {budget['buffer']}")
    lines.append(f"{'Total with buffer:':<46} {budget['total_with_buffer']}")
    lines.append(f"{'Available credits:':<46} {budget['available']}")
    lines.append(f"{'-'*60}")

    diff = budget["surplus_or_shortfall"]
    if diff >= 0:
        lines.append(f"SURPLUS: {diff} credits remaining")
    else:
        lines.append(f"SHORTFALL: {abs(diff)} credits over budget")
        lines.append(f"Options: reduce scope, use cheaper draft models, or top up")

    return "\n".join(lines)


def parse_deliverables_file(filepath):
    """Parse deliverables from a text file."""
    deliverables = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(" x ")
            if len(parts) == 2:
                count = int(parts[0].strip())
                rest = parts[1].split(" using ")
                if len(rest) == 2:
                    asset_type = rest[0].strip()
                    model = rest[1].strip()
                    deliverables.append((count, asset_type, model))
    return deliverables


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ScaleFlow Credit Budget Calculator")
    parser.add_argument("--plan", choices=["starter", "professional", "team"],
                        default="starter", help="Weavy plan tier")
    parser.add_argument("--deliverables", help="Path to deliverables file")
    args = parser.parse_args()

    if args.deliverables:
        deliverables = parse_deliverables_file(args.deliverables)
    else:
        # Example deliverables for demonstration
        deliverables = [
            (3, "hero_image", "flux_kontext"),
            (6, "social_static", "ideogram_v3"),
            (3, "video_15sec", "kling_2_1"),
            (1, "3d_product", "trellis_3d"),
            (6, "upscale", "topaz_image_upscale"),
        ]
        print("No deliverables file specified. Using example project:\n")

    budget = calculate_budget(deliverables, args.plan)
    print(format_budget(budget, args.plan))
