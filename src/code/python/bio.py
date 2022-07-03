from datetime import date

class Bio:
    def __init__(self, full_name, date_of_birth, place_of_birth):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        
        self.educations = []
        self.certifications = []
        self.skills = []
        self.experiences = []
        self.links = []

    def add_education(self, school, degree, start_year, end_year):
        self.educations.append({
            'school': school,
            'degree': degree,
            'start_year': start_year,
            'end_year': end_year
        })
        
    def add_certification(
        self, certificate, issuer, issue_year, expiration_year
    ):
        self.certifications.append({
            'certificate': certificate,
            'issuer': issuer,
            'issue_year': issue_year,
            'expiration_year': expiration_year
        })

    def add_skill(self, skill):
        self.skills.append(skill)

    def add_experience(
        self, position, employment_type, company, start_date, end_date
    ):
        self.experiences.append({
            'position': position,
            'employment_type': employment_type,
            'company': company,
            'start_date': start_date,
            'end_date': end_date,
        })

    def add_link(self, link_name, url):
        self.links.append({
            'link_name': link_name,
            'url': url
        })

if __name__ == "__main__":
    me = Bio(
        "Albert Wijaya",
        date(1999, 4, 3),
        "Jakarta, Indonesia"
    )

    me.add_education(
        "Universitas Multimedia Nusantara",
        "Informatics",
        2017,
        2021
    )

    me.add_certification(
        "Certified Ethical Hacker",
        "EC-Council",
        2020,
        2023
    )

    me.add_skill("Python")
    me.add_skill("JS")
    me.add_skill("SQL")
    me.add_skill("Git")
    me.add_skill("Docker")

    me.add_experience(
        "Software Developer",
        "Internship",
        "Agile Technica",
        date(2020, 6, 15),
        date(2020, 12, 30)
    )

    me.add_experience(
        "Sofware Developer",
        "Full-time",
        "Agile Technica",
        date(2021, 1, 4),
        date(2022, 1, 28)
    )

    me.add_experience(
        "DevOps Engineer",
        "Full-time",
        "JULO",
        date(2022, 2, 7),
        date(2022, 6, 24),
    )

    me.add_experience(
        "Software Engineer",
        "Full-time",
        "Indodana",
        date(2022, 6, 27),
        None,
    )

    me.add_link(
        "LinkedIn",
        "https://www.linkedin.com/in/albert-wijaya-ba5413181/"
    )
    me.add_link(
        "Website",
        "https://www.albertwijaya.com/"
    )
    me.add_link(
        "GitHub",
        "https://github.com/albetz99"
    )
    me.add_link(
        "HackerRank",
        "https://www.hackerrank.com/albetz99"
    )