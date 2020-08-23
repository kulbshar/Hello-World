def schedule_interview(applicant):
    print(f"Scheduled interview with {applicant['name']}")


applicants = [
    {
        "name": "Devon Smith",
        "programming_languages": ["c++", "ada"],
        "years_of_experience": 1,
        "has_degree": False,
        "email_address": "devon@email.com",
    },
    {
        "name": "Susan Jones",
        "programming_languages": ["python", "javascript"],
        "years_of_experience": 2,
        "has_degree": False,
        "email_address": "susan@email.com",
    },
    {
        "name": "Sam Hughes",
        "programming_languages": ["java"],
        "years_of_experience": 4,
        "has_degree": True,
        "email_address": "sam@email.com",
    },
]


for applicant in applicants:
    knows_python = "python" in applicant["programming_languages"]
    experienced_dev = applicant["years_of_experience"] >= 5

    meets_criteria = (
        knows_python
        or experienced_dev
        or applicant["has_degree"]
    )
    if meets_criteria:
        schedule_interview(applicant)

print("Check any()")
for applicant in applicants:
    knows_python = "python" in applicant["programming_languages"]
    experienced_dev = applicant["years_of_experience"] >= 5

    credentials = (
        knows_python,
        experienced_dev,
        applicant["has_degree"],
    )
    if any(credentials):
        schedule_interview(applicant)


print(any([0, 0, 1, 0]))

print(any(set((True, False, True))))

print(any(map(str.isdigit, "hello world")))


def knows_python(applicant):
    print(f"Determining if {applicant['name']} knows Python...")
    return "python" in applicant["programming_languages"]


def is_local(applicant):
    print(f"Determine if {applicant['name']} lives near the office...")


should_interview = knows_python(applicant) or is_local(applicant)

# Here, Python will call is_local() for every applicant, even for those who know Python. Because is_local()
# will take a long time to execute and is sometimes unnecessary, this is an inefficient implementation of the logic

should_interview = any([knows_python(applicant), is_local(applicant)])
print("should_interview=", should_interview)


# any((meets_criteria(applicant) for applicant in applicants))

any((1, 0))

1 or 0

None or 0
