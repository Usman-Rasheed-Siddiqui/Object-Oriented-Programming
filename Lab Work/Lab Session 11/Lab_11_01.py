
def eligibility():
    try:
        years_of_education = int(input("Enter years of education: "))
        if years_of_education <= 16:
            raise Exception(
            "It's not enough. You must have more than 16 years of education."
            )

    except ValueError as e:
        print("Error:",e)

    except Exception as e:
        print("Error:",e)

    else:
        print("You are eligible.")

eligibility()


