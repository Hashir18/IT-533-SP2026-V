"Repositry Url: https://github.com/Hashir18/IT-533-SP2026-V/blob/main/college_records.py"

class Validator:
    """Holds the validation rules for the submitted information."""

    # Characters that are not allowed in a name.
    NAME_FORBIDDEN = set('!"@#$%^&*()_=+,<>/?;:[]{}\\')

    # Characters that are not allowed in an email address.
    EMAIL_FORBIDDEN = set('!"\'#$%^&*()=+,<>/?;:[]{}\\')

    @staticmethod
    def is_present(value):
        """Return True only if the field has actually been filled in."""
        return value is not None and value.strip() != ""

    @staticmethod
    def validate_name(value):
        if not Validator.is_present(value):
            return False, "A name is required."
        if not any(ch.isalpha() for ch in value):
            return False, "A name must be made up mainly of letters."
        for ch in value:
            if ch in Validator.NAME_FORBIDDEN:
                return False, "A name cannot contain the character: " + ch
        return True, ""

    @staticmethod
    def validate_email(value):
        if not Validator.is_present(value):
            return False, "An email address is required."
        if not any(ch.isalnum() for ch in value):
            return False, "An email address must contain alphanumeric characters."
        for ch in value:
            if ch in Validator.EMAIL_FORBIDDEN:
                return False, "An email address cannot contain the character: " + ch
        return True, ""

    @staticmethod
    def validate_id(value, max_digits):
        """Validate an ID: required, numeric, and no longer than max_digits."""
        if not Validator.is_present(value):
            return False, "An ID is required."
        if not value.isdigit():
            return False, "The ID must be a number."
        if len(value) > max_digits:
            return False, "The ID must be " + str(max_digits) + " or fewer digits long."
        return True, ""

    @staticmethod
    def validate_required_text(value, field_name):
        """Validate any field that simply must not be left blank."""
        if not Validator.is_present(value):
            return False, field_name + " is required."
        return True, ""

    @staticmethod
    def validate_person_type(value):
        if Validator.is_present(value) and value.strip().lower() in ("student", "instructor"):
            return True, ""
        return False, "Please enter either 'student' or 'instructor'."


class Person:
    """Base class shared by every individual in the college records."""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def displayInformation(self):
        details = ""
        details += "Name: " + self.name + "\n"
        details += "Email: " + self.email + "\n"
        return details


class Student(Person):
    """A student. Inherits name and email from Person."""

    def __init__(self, name, email, student_id, program_of_study):
        super().__init__(name, email)
        self.student_id = student_id
        self.program_of_study = program_of_study

    def displayInformation(self):
        details = "Type: Student\n"
        details += super().displayInformation()
        details += "Student ID: " + self.student_id + "\n"
        details += "Program of Study: " + self.program_of_study + "\n"
        return details


class Instructor(Person):
    """An instructor. Inherits name and email from Person."""

    def __init__(self, name, email, instructor_id, last_institution, highest_degree):
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.last_institution = last_institution
        self.highest_degree = highest_degree

    def displayInformation(self):
        details = "Type: Instructor\n"
        details += super().displayInformation()
        details += "Instructor ID: " + self.instructor_id + "\n"
        details += "Last Institution Graduated From: " + self.last_institution + "\n"
        details += "Highest Degree Earned: " + self.highest_degree + "\n"
        return details


def prompt_until_valid(prompt_text, validation_function):
    """Keep asking for input until the validation function is satisfied."""
    while True:
        value = input(prompt_text)
        is_valid, message = validation_function(value)
        if is_valid:
            return value
        print(message + " Please re-enter.")


def main():
    college_records = []

    while True:
        person_type = prompt_until_valid(
            "Is this person a student or an instructor? ",
            Validator.validate_person_type
        ).strip().lower()

        name = prompt_until_valid(
            "Enter the person's name: ",
            Validator.validate_name
        )
        email = prompt_until_valid(
            "Enter the person's email address: ",
            Validator.validate_email
        )

        if person_type == "student":
            student_id = prompt_until_valid(
                "Enter the Student ID (7 or fewer digits): ",
                lambda v: Validator.validate_id(v, 7)
            )
            program = prompt_until_valid(
                "Enter the program of study: ",
                lambda v: Validator.validate_required_text(v, "Program of study")
            )
            college_records += [Student(name, email, student_id, program)]
        else:
            instructor_id = prompt_until_valid(
                "Enter the Instructor ID (5 or fewer digits): ",
                lambda v: Validator.validate_id(v, 5)
            )
            institution = prompt_until_valid(
                "Enter the last institution graduated from: ",
                lambda v: Validator.validate_required_text(v, "Last institution")
            )
            degree = prompt_until_valid(
                "Enter the highest degree earned: ",
                lambda v: Validator.validate_required_text(v, "Highest degree")
            )
            college_records += [Instructor(name, email, instructor_id, institution, degree)]

        answer = input("Add another individual? Enter 'yes' to continue, anything else to finish: ")
        if answer.strip().lower() not in ("yes", "y"):
            break

    print("\n===== College Records =====\n")
    for record in college_records:
        print(record.displayInformation())


if __name__ == "__main__":
    main()
