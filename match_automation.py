import csv
import random

# Define the Mentee class
class Mentee:
    def __init__(self, data):
        self.first_name = data.get("first_name", "")
        self.last_name = data.get("last_name", "")
        self.email = data.get("email", "")
        self.occupation_profile = data.get("occupation_profile", "").split(";")
        self.industry = data.get("industry", "").split(";")
        self.years_experience = data.get("years_experience", "")
        self.areas_of_interest = data.get("areas_of_interest", "").split(";")
        self.preferred_mentor_experience = data.get("preferred_mentor_experience", "").split(";")
        self.mentorship_availability_day = data.get("mentorship_availability_day", "").split(";")
        self.mentorship_availability_time = data.get("mentorship_availability_time", "").split(";")
        self.preferred_mentoring_style = data.get("preferred_mentoring_style", "")
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
        self.anything_else = data.get("anything_else", "")

    def combine_text_fields(self):
        fields = [
            self.career_aspiration_engaging_role,
            self.career_aspiration_ideal_life,
            self.career_aspiration_specific_roles,
            self.career_aspiration_skills_critical,
            self.career_aspiration_challenges,
            self.career_aspiration_success_def,
            self.career_aspiration_admired_path,
            self.career_aspiration_work_env,
            self.career_aspiration_proud_accomplishment,
            self.personal_interest_why_mentored,
            self.personal_interest_prev_mentoring,
            self.personal_interest_expectations,
            self.anything_else
        ]
        return " ".join(fields)

# Define the Mentor class
class Mentor:
    def __init__(self, data):
        self.first_name = data.get("first_name", "")
        self.last_name = data.get("last_name", "")
        self.email = data.get("email", "")
        self.occupation_profile = data.get("occupation_profile", "").split(";")
        self.industry_profile = data.get("industry_profile", "").split(";")
        self.years_experience = data.get("years_experience", "")
        self.areas_of_expertise = data.get("areas_of_expertise", "").split(";")
        self.preferred_mentee_experience = data.get("preferred_mentee_experience", "").split(";")
        self.mentorship_availability_day = data.get("mentorship_availability_day", "").split(";")
        self.mentorship_availability_time = data.get("mentorship_availability_time", "").split(";")
        self.preferred_mentoring_style = data.get("preferred_mentoring_style", "")
        self.mobility_pillars = data.get("mobility_pillars", "").split(";")
        self.novelty_pillars = data.get("novelty_pillars", "").split(";")
        self.experience_pillars = data.get("experience_pillars", "").split(";")
        self.exposure_pillars = data.get("exposure_pillars", "").split(";")
        self.why_mentor = data.get("why_mentor", "")
        self.previous_mentoring_experience = data.get("previous_mentoring_experience", "")
        self.expectations_mentoring = data.get("expectations_mentoring", "")
        self.anything_else_mentor = data.get("anything_else_mentor", "")

    def combine_text_fields(self):
        fields = [
            self.why_mentor,
            self.previous_mentoring_experience,
            self.expectations_mentoring,
            self.anything_else_mentor
        ]
        return " ".join(fields)

def load_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def jaccard_similarity(list1, list2):
    set1, set2 = set(list1), set(list2)
    if not set1 or not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

def simulate_text_embedding_similarity(text1, text2):
    return 0.85  # Simulated strong semantic match


def compare_structured_fields(mentee, mentor):
    weights = {
        "occupation_profile": 15,
        "industry": 15,
        "years_experience": 10,
        "areas_of_interest": 20,
        "areas_of_expertise": 20,
        "mentorship_availability_day": 5,
        "mentorship_availability_time": 5,
        "preferred_mentoring_style": 5,
        "preferred_mentor_experience": 5,
        "preferred_mentee_experience": 5,
        "mobility_pillars": 5,
        "novelty_pillars": 5,
        "experience_pillars": 5,
        "exposure_pillars": 5
    }

    total_score = 0.0
    total_score += jaccard_similarity(mentee.occupation_profile, mentor.occupation_profile) * weights["occupation_profile"]
    total_score += jaccard_similarity(mentee.industry, mentor.industry_profile) * weights["industry"]
    total_score += jaccard_similarity(mentee.areas_of_interest, mentor.areas_of_expertise) * weights["areas_of_interest"]
    total_score += jaccard_similarity(mentee.preferred_mentor_experience, [mentor.years_experience]) * weights["preferred_mentor_experience"]
    total_score += jaccard_similarity([mentee.years_experience], mentor.preferred_mentee_experience) * weights["preferred_mentee_experience"]
    total_score += jaccard_similarity(mentee.mentorship_availability_day, mentor.mentorship_availability_day) * weights["mentorship_availability_day"]
    total_score += jaccard_similarity(mentee.mentorship_availability_time, mentor.mentorship_availability_time) * weights["mentorship_availability_time"]
    total_score += int(mentee.preferred_mentoring_style == mentor.preferred_mentoring_style) * weights["preferred_mentoring_style"]
    total_score += jaccard_similarity(mentee.mobility_pillars, mentor.mobility_pillars) * weights["mobility_pillars"]
    total_score += jaccard_similarity(mentee.novelty_pillars, mentor.novelty_pillars) * weights["novelty_pillars"]
    total_score += jaccard_similarity(mentee.experience_pillars, mentor.experience_pillars) * weights["experience_pillars"]
    total_score += jaccard_similarity(mentee.exposure_pillars, mentor.exposure_pillars) * weights["exposure_pillars"]

    return total_score / sum(weights.values())

def calculate_total_match_score(mentee, mentor):
    structured_score = compare_structured_fields(mentee, mentor)
    text_similarity = simulate_text_embedding_similarity(
        mentee.combine_text_fields(),
        mentor.combine_text_fields()
    )
    return (structured_score * 0.6) + (text_similarity * 0.4)

def save_matches_to_csv(matches, filename="matchesList.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["mentee_name", "mentee_email", "mentor_name", "mentor_email", "match_score"])
        for match in matches:
            writer.writerow(match)

mentees_data = load_csv("mentees.csv")
mentors_data = load_csv("mentors.csv")

mentees = [Mentee(data) for data in mentees_data]
mentors = [Mentor(data) for data in mentors_data]

print(f"Loaded {len(mentees)} mentees and {len(mentors)} mentors.")

match_results = []

for mentee in mentees:
    for mentor in mentors:
        total_score = calculate_total_match_score(mentee, mentor)
        print(f"Final match score between {mentee.first_name} and {mentor.first_name}: {total_score:.2f}")
        match_results.append([
            f"{mentee.first_name} {mentee.last_name}",
            mentee.email,
            f"{mentor.first_name} {mentor.last_name}",
            mentor.email,
            f"{total_score:.2f}"
        ])

save_matches_to_csv(match_results)