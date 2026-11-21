import os
import pandas as pd
from core.charts import (
    plot_required_for_job,
    plot_level_hist,
    plot_requirement_scatter,
    plot_avg_level_by_skill,
)

os.makedirs("output/charts", exist_ok=True)
req = pd.read_csv("data/job_requirements.csv")
levels = pd.read_csv("output/learner_skills_cleaned.csv")

p1 = plot_required_for_job(req, "J01", "output/charts/unigap_required_for_job.png")
print(f"Saved: {p1}")

p2 = plot_level_hist(levels, "output/charts/unigap_level_hist.png")
print(f"Saved: {p2}")

p3 = plot_requirement_scatter(req, "output/charts/unigap_requirement_scatter.png")
print(f"Saved: {p3}")

p4 = plot_avg_level_by_skill(levels, "output/charts/unigap_avg_level.png")
print(f"Saved: {p4}")
