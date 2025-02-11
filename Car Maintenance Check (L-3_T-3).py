maintenance = {
    "Engine noise": 4,
    "Check engine light": 5,
    "Poor fuel efficiency": 3,
    "Strange vibrations": 3,
    "Difficulty starting": 4,
    "Braking issues": 5,
    "Unusual exhaust smoke": 4,
    "Steering problems": 3
}

total_score = 0

for issue in maintenance:
    print("Are you experiencing", issue, "? (Yes = 1, No = 0)")
    while True:
        user_input = input()
        if user_input == "1" or user_input == "0":
            break
        print("Please enter 1 for Yes or 0 for No.")

    if user_input == "1":
        total_score = total_score + maintenance[issue]

threshold = 15

if total_score > threshold:
    print("Based on the issues reported, your car may require maintenance. It is recommended to visit a mechanic for a thorough inspection.")
else:
    print("Based on the issues reported, your car does not seem to require immediate maintenance. However, if you are concerned, consulting a mechanic is always a good idea.")
