import os

files = [
    "output/charts/unigap_required_for_job.png",
    "output/charts/unigap_level_hist.png",
    "output/charts/unigap_requirement_scatter.png",
    "output/charts/unigap_avg_level.png",
]

passed = 0
for f in files:
    if os.path.exists(f) and os.path.getsize(f) > 0:
        print(f"PASS - {f}")
        passed += 1
    else:
        print(f"FAIL - {f}")

print(f"{passed} of {len(files)} charts created")
