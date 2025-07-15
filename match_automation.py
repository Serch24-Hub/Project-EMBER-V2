import csv

# Define the Mentee class
class Mentee:
    def __init__(self, data):
        self.first_name = data.get("first_name", "")
        self.last_name = data.get("last_name", "")
        self.email = data.get("email", "")
        self.first_generation = data.get("first_generation", "")
        self.current_status = data.get("current_status", "")
        self.occupation_profile = data.get("occupation_profile", "").split(";")
        self.industry = data.get("industry", "").split(";")
        self.years_experience = data.get("years_experience", "")
        self.education = data.get("education", "")
        self.areas_of_interest = data.get("areas_of_interest", "").split(";")
        self.preferred_mentor_experience = data.get("preferred_mentor_experience", "").split(";")
        self.mentorship_availability_day = data.get("mentorship_availability_day", "").split(";")
        self.mentorship_availability_time = data.get("mentorship_availability_time", "").split(";")
        self.preferred_mentoring_style = data.get("preferred_mentoring_style", "")
        self.session_duration = data.get("session_duration", "").split(";")
        self.commitment = data.get("commitment", "").split(";")
        self.cadence = data.get("cadence", "")
        self.communication_style = data.get("communication_style", "").split(";")
        self.mobility_pillars = data.get("mobility_pillars", "").split(";")
        self.novelty_pillars = data.get("novelty_pillars", "").split(";")
        self.experience_pillars = data.get("experience_pillars", "").split(";")
        self.exposure_pillars = data.get("exposure_pillars", "").split(";")
        self.career_aspiration_engaging_role = data.get("career_aspiration_engaging_role", "")
        self.career_aspiration_ideal_life = data.get("career_aspiration_ideal_life", "")
        self.career_aspiration_specific_roles = data.get("career_aspiration_specific_roles", "")
        self.career_aspiration_skills_critical = data.get("career_aspiration_skills_critical", "")
        self.career_aspiration_challenges = data.get("career_aspiration_challenges", "")
        self.career_aspiration_success_def = data.get("career_aspiration_success_def", "")
        self.career_aspiration_admired_path = data.get("career_aspiration_admired_path", "")
        self.career_aspiration_work_env = data.get("career_aspiration_work_env", "")
        self.career_aspiration_proud_accomplishment = data.get("career_aspiration_proud_accomplishment", "")
        self.personal_interest_why_mentored = data.get("personal_interest_why_mentored", "")
        self.personal_interest_prev_mentoring = data.get("personal_interest_prev_mentoring", "")
        self.personal_interest_expectations = data.get("personal_interest_expectations", "")
        self.hobbies = data.get("hobbies", "").split(";")
        self.anything_else = data.get("anything_else", "")

# Define the Mentor class
class Mentor:
    def __init__(self, data):
        self.first_name = data.get("first_name", "")
        self.last_name = data.get("last_name", "")
        self.email = data.get("email", "")
        self.occupation_profile = data.get("occupation_profile", "").split(";")
        self.industry_profile = data.get("industry_profile", "").split(";")
        self.years_experience = data.get("years_experience", "")
        self.education_profile = data.get("education_profile", "")
        self.areas_of_expertise = data.get("areas_of_expertise", "").split(";")
        self.preferred_mentee_experience = data.get("preferred_mentee_experience", "").split(";")
        self.mentorship_availability_day = data.get("mentorship_availability_day", "").split(";")
        self.mentorship_availability_time = data.get("mentorship_availability_time", "").split(";")
        self.preferred_mentoring_style = data.get("preferred_mentoring_style", "")
        self.session_duration = data.get("session_duration", "")
        self.commitment = data.get("commitment", "")
        self.cadence = data.get("cadence", "")
        self.communication_style = data.get("communication_style", "").split(";")
        self.mobility_pillars = data.get("mobility_pillars", "").split(";")
        self.novelty_pillars = data.get("novelty_pillars", "").split(";")
        self.experience_pillars = data.get("experience_pillars", "").split(";")
        self.exposure_pillars = data.get("exposure_pillars", "").split(";")
        self.why_mentor = data.get("why_mentor", "")
        self.previous_mentoring_experience = data.get("previous_mentoring_experience", "")
        self.expectations_mentoring = data.get("expectations_mentoring", "")
        self.hobbies = data.get("hobbies", "").split(";")
        self.anything_else_mentor = data.get("anything_else_mentor", "")

# Load data from CSV files into lists of Mentee and Mentor objects
def load_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

mentees_data = load_csv("mentees.csv")
mentors_data = load_csv("mentors.csv")

mentees = [Mentee(data) for data in mentees_data]
mentors = [Mentor(data) for data in mentors_data]

print(f"Loaded {len(mentees)} mentees and {len(mentors)} mentors.")