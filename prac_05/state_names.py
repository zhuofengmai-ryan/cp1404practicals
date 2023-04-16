# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": 'Australian Capital Territory', "VIC": "Victoria",
                "TAS": "Tasmania"}
print(CODE_TO_NAME)

while True:
    try:
        state_code = input("Enter short state: ").upper()
        if not state_code:
            break
        state_name = CODE_TO_NAME[state_code]
    except KeyError:
        print("Invalid short state")
    else:
        print(f"{state_code} is {state_name}")

for code, name in CODE_TO_NAME.items():
    print("{:<3} is {}".format(code, name))