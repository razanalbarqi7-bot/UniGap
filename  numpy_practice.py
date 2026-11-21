import numpy as np

# UniGap: Python, SQL, Statistics, Communication, Cloud (0-100, sample)
student_skills = np.array([70, 80, 40, 55, 50])
print("Student skills:", student_skills) 

import numpy as np

# UniGap: Python, SQL, Statistics, Communication, Cloud (0-100, sample)
student_skills = np.array([70, 80, 75, 55, 50])
print("Student skills:", student_skills)

# الأسطر المضافة (المنزلتين العشريتين، أعلى وأقل قيمة)
print("Average density:", np.round(np.mean(student_skills), 2))
print("Highest density:", np.max(student_skills))
print("Lowest density:", np.min(student_skills))