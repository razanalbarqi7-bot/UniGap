import numpy as np

skills = ["Python", "SQL", "Statistics", "Communication", "Cloud"]
columns = ["job_requires", "learner_level"]

levels = np.array([
    [90, 70],
    [85, 80],
    [70, 75],
    [60, 55],
    [80, 50]
])  # level 0-100

# المهام 1 و 2: حساب الفجوة وأكبر فجوة
gap = levels[:, 0] - levels[:, 1]
print("Shape:", levels.shape)
print("Gap:", gap)
print("Largest gap:", skills[np.argmax(gap)])

# المهمة 3: المهارات التي فجوتها 25 فأكثر
high_gaps_count = np.sum(gap >= 25)
print("Gaps >= 25:", high_gaps_count)

# المهمة 4: متوسط الفجوة
avg_gap = np.mean(gap)
print("Average gap:", avg_gap)