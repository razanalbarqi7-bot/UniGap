import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# تخصيص ثيم عصري وجذاب للرسوم (ألوان متناسقة ومظهر احترافي)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

def plot_required_for_job(req, job, path):
    one = req[req["job_id"] == job]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.bar(one["skill_id"], one["required_level"], color='#4f46e5', edgecolor='#312e81', linewidth=1.2, width=0.6)
    ax.set_title(f"Required Skill Levels for Job {job}", fontsize=12, fontweight='bold', pad=12, color='#1e293b')
    ax.set_xlabel("Skill ID", fontsize=10, fontweight='bold', color='#334155')
    ax.set_ylabel("Required Level", fontsize=10, fontweight='bold', color='#334155')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    return path

def plot_level_hist(levels, path, bins=10):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    n, bins, patches = ax.hist(levels["level"], bins=bins, color='#0ea5e9', edgecolor='#0369a1', linewidth=1.2)
    ax.set_title("Distribution of Learner Levels", fontsize=12, fontweight='bold', pad=12, color='#1e293b')
    ax.set_xlabel("Level", fontsize=10, fontweight='bold', color='#334155')
    ax.set_ylabel("Number of Records", fontsize=10, fontweight='bold', color='#334155')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    return path

def plot_requirement_scatter(req, path):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.scatter(req["required_level"], req["importance"], color='#f59e0b', s=90, edgecolors='#b45309', linewidths=1.2, zorder=3)
    ax.set_title("Required Level vs Importance", fontsize=12, fontweight='bold', pad=12, color='#1e293b')
    ax.set_xlabel("Required Level", fontsize=10, fontweight='bold', color='#334155')
    ax.set_ylabel("Importance", fontsize=10, fontweight='bold', color='#334155')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    return path

def plot_avg_level_by_skill(levels, path):
    avg = levels.groupby("skill_id")["level"].mean()
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(avg.index, avg.values, color='#10b981', edgecolor='#047857', linewidth=1.2, width=0.6)
    ax.set_title("Average Level per Skill", fontsize=12, fontweight='bold', pad=12, color='#1e293b')
    ax.set_xlabel("Skill ID", fontsize=10, fontweight='bold', color='#334155')
    ax.set_ylabel("Average Level", fontsize=10, fontweight='bold', color='#334155')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    return path
