import json
import os

DATA_FILE = "career_data.json"


# Load data from file
def load_data():

    if not os.path.exists(DATA_FILE):
        return {
            "students": [],
            "careers": [],
            "skills": [],
            "applications": []
        }

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        return data

    except:
        print("Problem reading data file. Starting with empty data.")

        return {
            "students": [],
            "careers": [],
            "skills": [],
            "applications": []
        }


# Save data in file
def save_data(data):

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Check if student already exists
def student_exists(data, student_id):

    for student in data["students"]:

        if student["id"] == student_id:
            return True

    return False


# ---------------- STUDENT MANAGEMENT ----------------

def add_student(data):

    print("\n--- Add Student ---")

    student_id = input("Enter student ID: ")

    if student_exists(data, student_id):
        print("Student already exists.")
        return

    name = input("Enter student name: ")
    course = input("Enter course: ")
    year = input("Enter year: ")
    email = input("Enter email: ")

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "year": year,
        "email": email
    }

    data["students"].append(student)

    save_data(data)

    print("Student added successfully.")


def view_students(data):

    print("\n--- Student List ---")

    if len(data["students"]) == 0:
        print("No students found.")
        return

    for student in data["students"]:

        print("\nStudent ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Year:", student["year"])
        print("Email:", student["email"])


def search_student(data):

    print("\n--- Search Student ---")

    student_id = input("Enter student ID: ")

    for student in data["students"]:

        if student["id"] == student_id:

            print("\nStudent Found")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Year:", student["year"])
            print("Email:", student["email"])

            return

    print("Student not found.")


# ---------------- CAREER MANAGEMENT ----------------

def add_career(data):

    print("\n--- Add Career ---")

    title = input("Enter career name: ")
    company = input("Enter company/organisation: ")
    location = input("Enter location: ")
    qualification = input("Enter required qualification: ")

    career = {
        "title": title,
        "company": company,
        "location": location,
        "qualification": qualification
    }

    data["careers"].append(career)

    save_data(data)

    print("Career added successfully.")


def view_careers(data):

    print("\n--- Career List ---")

    if len(data["careers"]) == 0:
        print("No careers found.")
        return

    for i in range(len(data["careers"])):

        career = data["careers"][i]

        print("\nCareer", i + 1)
        print("Career:", career["title"])
        print("Company:", career["company"])
        print("Location:", career["location"])
        print("Qualification:", career["qualification"])


def search_career(data):

    print("\n--- Search Career ---")

    search = input("Enter career name: ").lower()

    found = False

    for career in data["careers"]:

        if search in career["title"].lower():

            print("\nCareer:", career["title"])
            print("Company:", career["company"])
            print("Location:", career["location"])
            print("Qualification:", career["qualification"])

            found = True

    if not found:
        print("Career not found.")


# ---------------- SKILL MANAGEMENT ----------------

def add_skill(data):

    print("\n--- Add Skill ---")

    student_id = input("Enter student ID: ")

    if not student_exists(data, student_id):
        print("Student does not exist.")
        return

    skill_name = input("Enter skill name: ")

    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    choice = input("Enter skill level: ")

    if choice == "1":
        level = "Beginner"

    elif choice == "2":
        level = "Intermediate"

    elif choice == "3":
        level = "Advanced"

    else:
        print("Invalid skill level.")
        return

    skill = {
        "student_id": student_id,
        "skill": skill_name,
        "level": level
    }

    data["skills"].append(skill)

    save_data(data)

    print("Skill added successfully.")


def view_skills(data):

    print("\n--- All Skills ---")

    if len(data["skills"]) == 0:
        print("No skills found.")
        return

    for skill in data["skills"]:

        print("\nStudent ID:", skill["student_id"])
        print("Skill:", skill["skill"])
        print("Level:", skill["level"])


def search_student_skills(data):

    print("\n--- Search Student Skills ---")

    student_id = input("Enter student ID: ")

    found = False

    for skill in data["skills"]:

        if skill["student_id"] == student_id:

            print("\nSkill:", skill["skill"])
            print("Level:", skill["level"])

            found = True

    if not found:
        print("No skills found for this student.")


# ---------------- APPLICATION TRACKING ----------------

def add_application(data):

    print("\n--- Add Application ---")

    student_id = input("Enter student ID: ")

    if not student_exists(data, student_id):
        print("Student does not exist.")
        return

    career = input("Enter career/job name: ")
    company = input("Enter company name: ")

    print("\nApplication Status")
    print("1. Planned")
    print("2. Applied")
    print("3. Selected")
    print("4. Rejected")

    choice = input("Enter status: ")

    if choice == "1":
        status = "Planned"

    elif choice == "2":
        status = "Applied"

    elif choice == "3":
        status = "Selected"

    elif choice == "4":
        status = "Rejected"

    else:
        print("Invalid status.")
        return

    application = {
        "student_id": student_id,
        "career": career,
        "company": company,
        "status": status
    }

    data["applications"].append(application)

    save_data(data)

    print("Application added successfully.")


def view_applications(data):

    print("\n--- Application List ---")

    if len(data["applications"]) == 0:
        print("No applications found.")
        return

    for i in range(len(data["applications"])):

        application = data["applications"][i]

        print("\nApplication", i + 1)
        print("Student ID:", application["student_id"])
        print("Career:", application["career"])
        print("Company:", application["company"])
        print("Status:", application["status"])


def update_application(data):

    print("\n--- Update Application ---")

    student_id = input("Enter student ID: ")
    career = input("Enter career/job name: ")

    found = False

    for application in data["applications"]:

        if (
            application["student_id"] == student_id
            and application["career"].lower() == career.lower()
        ):

            print("\nCurrent Status:", application["status"])

            print("1. Planned")
            print("2. Applied")
            print("3. Selected")
            print("4. Rejected")

            choice = input("Enter new status: ")

            if choice == "1":
                application["status"] = "Planned"

            elif choice == "2":
                application["status"] = "Applied"

            elif choice == "3":
                application["status"] = "Selected"

            elif choice == "4":
                application["status"] = "Rejected"

            else:
                print("Invalid choice.")
                return

            save_data(data)

            print("Application updated.")

            found = True
            break

    if not found:
        print("Application not found.")


# ---------------- REPORTS ----------------

def show_reports(data):

    print("\n--- Reports ---")

    students = len(data["students"])
    careers = len(data["careers"])
    skills = len(data["skills"])
    applications = len(data["applications"])

    print("Total Students:", students)
    print("Total Careers:", careers)
    print("Total Skills:", skills)
    print("Total Applications:", applications)

    planned = 0
    applied = 0
    selected = 0
    rejected = 0

    for application in data["applications"]:

        if application["status"] == "Planned":
            planned += 1

        elif application["status"] == "Applied":
            applied += 1

        elif application["status"] == "Selected":
            selected += 1

        elif application["status"] == "Rejected":
            rejected += 1

    print("\nApplication Status")
    print("Planned:", planned)
    print("Applied:", applied)
    print("Selected:", selected)
    print("Rejected:", rejected)


def student_summary(data):

    print("\n--- Student Summary ---")

    if len(data["students"]) == 0:
        print("No students found.")
        return

    student_id = input("Enter student ID: ")

    student = None

    for s in data["students"]:

        if s["id"] == student_id:
            student = s
            break

    if student is None:
        print("Student not found.")
        return

    print("\nStudent Details")
    print("Name:", student["name"])
    print("Course:", student["course"])
    print("Year:", student["year"])
    print("Email:", student["email"])

    print("\nSkills")

    skill_found = False

    for skill in data["skills"]:

        if skill["student_id"] == student_id:

            print("-", skill["skill"], "(", skill["level"], ")")
            skill_found = True

    if not skill_found:
        print("No skills added.")

    print("\nApplications")

    application_found = False

    for application in data["applications"]:

        if application["student_id"] == student_id:

            print(
                "-",
                application["career"],
                "at",
                application["company"],
                ":",
                application["status"]
            )

            application_found = True

    if not application_found:
        print("No applications found.")


# ---------------- MENUS ----------------

def student_menu(data):

    while True:

        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(data)

        elif choice == "2":
            view_students(data)

        elif choice == "3":
            search_student(data)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def career_menu(data):

    while True:

        print("\n===== CAREER MANAGEMENT =====")
        print("1. Add Career")
        print("2. View Careers")
        print("3. Search Career")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_career(data)

        elif choice == "2":
            view_careers(data)

        elif choice == "3":
            search_career(data)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def skill_menu(data):

    while True:

        print("\n===== SKILL MANAGEMENT =====")
        print("1. Add Skill")
        print("2. View Skills")
        print("3. Search Student Skills")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_skill(data)

        elif choice == "2":
            view_skills(data)

        elif choice == "3":
            search_student_skills(data)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def application_menu(data):

    while True:

        print("\n===== APPLICATION TRACKING =====")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Update Application")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_application(data)

        elif choice == "2":
            view_applications(data)

        elif choice == "3":
            update_application(data)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


# ---------------- MAIN MENU ----------------

def main():

    data = load_data()

    while True:

        print("\n")
        print("===== CAREER MANAGEMENT SYSTEM =====")
        print("1. Student Management")
        print("2. Career Management")
        print("3. Skill Management")
        print("4. Application Tracking")
        print("5. Reports")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu(data)

        elif choice == "2":
            career_menu(data)

        elif choice == "3":
            skill_menu(data)

        elif choice == "4":
            application_menu(data)

        elif choice == "5":

            while True:

                print("\n===== REPORTS =====")
                print("1. Overall Report")
                print("2. Student Summary")
                print("3. Back")

                report_choice = input("Enter your choice: ")

                if report_choice == "1":
                    show_reports(data)

                elif report_choice == "2":
                    student_summary(data)

                elif report_choice == "3":
                    break

                else:
                    print("Invalid choice.")

        elif choice == "6":

            print("\nThank you for using Career Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()