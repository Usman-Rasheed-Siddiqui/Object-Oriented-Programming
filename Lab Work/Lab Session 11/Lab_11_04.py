
class InsufficientEducationError(Exception):
    """Custom exception for Insufficient Education"""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def eligibility():
    try:
        years_of_education = int(input("Enter years of education: "))
        if years_of_education <= 16:
            raise InsufficientEducationError(
                "It's not enough. You must have more than 16 years of education."
            )

    except ValueError as e:
        print("Error:",e)

    except InsufficientEducationError as e:
        print("Error:",e)

    else:
        print("You are eligible.")  

eligibility()

