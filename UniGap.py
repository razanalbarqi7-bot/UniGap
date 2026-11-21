project = "UniGap"
version = "0.1"
description = "Skill gap: graduate vs. job"
print("Project:", project, "| Version:", version)
print("Description:", description)
 
graduate_skills = {"Python", "SQL", "Excel"}
job_skills = {"Python", "SQL", "Docker", "Git"}
gap = job_skills - graduate_skills
print("Graduate skills:", sorted(graduate_skills))
print("Job skills:", sorted(job_skills))
print("Skills to learn:", sorted(gap))

