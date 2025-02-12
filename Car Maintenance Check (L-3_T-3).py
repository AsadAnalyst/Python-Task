SafeHome = {
    "Exposed electrical wiring": 5,
    "Gas leak smell": 5,
    "Water leakage or mold growth": 4,
    "Loose stair railings": 3,
    "Faulty smoke detectors": 4,
    "Clogged or blocked exits": 3,
    "Slippery floors without mats": 3,
    "Windows or doors that don’t lock properly": 4
}

totalScore = 0

for test in SafeHome:
    print("Are you experiencing", test, "(Yes = 1, No = 0)")
    while True:
        responce = input()
        if responce == "1" or responce == "0":
            break
        print("Please Enter (Yes = 1, No = 0)")

    if responce == "1":
        totalScore = totalScore + SafeHome[test]

if totalScore > 15:
    print("Based on the hazards reported, your home may require safety improvements. It is recommended to address these issues to prevent accidents")
else:
    print("Based on the hazards reported, your home does not seem to have critical safety risks. However, regular maintenance is always a good idea.")
