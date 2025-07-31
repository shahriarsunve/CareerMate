from langchain.tools import tool
from data.skills_data import skills_required
from data.jobs_data import job_listings
from data.courses_data import course_catalog

@tool
def get_missing_skills(user_skills_and_job: str) -> str:
    """Find missing skills. Input: 'Excel, Python | data scientist'"""
    try:
        skills, job = user_skills_and_job.split('|')
        user_skills = [s.strip() for s in skills.split(',')]
        required = skills_required.get(job.strip().lower(), [])
        missing = [s for s in required if s not in user_skills]
        return f"Missing skills for {job.title()}: {missing}"
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def find_jobs(user_skills_and_location: str) -> str:
    """Find jobs. Input: 'SQL, Excel | Remote'"""
    try:
        skills, location = user_skills_and_location.split('|')
        user_skills = [s.strip() for s in skills.split(',')]
        location = location.strip().lower()
        matches = []
        for job in job_listings:
            if all(s in user_skills for s in job["skills"]):
                if not location or job["location"].lower() == location:
                    matches.append(f"{job['title']} @ {job['company']} ({job['location']})")
        return "\n".join(matches) or "No matching jobs found."
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def recommend_courses(skills_input: str) -> str:
    """Recommend courses. Input: 'SQL, Pandas'"""
    skills = [s.strip() for s in skills_input.split(',')]
    output = ""
    for skill in skills:
        if skill in course_catalog:
            output += f"\n📘 {skill}:\n"
            for title, platform, link in course_catalog[skill]:
                output += f"- {title} ({platform}) → {link}\n"
    return output or "No course recommendations found."