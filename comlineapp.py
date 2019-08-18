"""
A command line program which lets you see the final results for any F1 race (since the 1st season in 1950).
"""

import requests

def mainPrompt():
    """
    The main menu, where the user can type a number corresponding to their choice.
    """
    query = input("\nWhat do you want to do?\n1 - See race results\n2 - Exit program\ntype number >>  ")
    if query == "1":
        getRaceResults()
    elif query != "2":
        print("\nThis is not a valid option!")
        mainPrompt()

def getRaceResults():
    """
    The section where the user can input the season and the round, and then the results are printed.
    """

    print("\nInput F1 season and number of round to get results")
    season = input("Season: ")
    round = input("Round: ")

    # Attempts to retrieve the data from the Ergast API
    try:
        URL = f"http://ergast.com/api/f1/{season}/{round}/results.json"
        req = requests.get(url=URL)
        data = req.json()
        results = data['MRData']['RaceTable']['Races'][0]['Results']

        print(f"\nResults of round {round} of the {season} season:")
        for i in range(len(results)):
            firstname = data['MRData']['RaceTable']['Races'][0]['Results'][i]['Driver']['givenName']
            lastname = data['MRData']['RaceTable']['Races'][0]['Results'][i]['Driver']['familyName']

            if i == 0:
                print("=======")
                print(f"|| {i+1} || {firstname} {lastname}")
                print("=======")
            elif i == 1:
                print("_____")
                print(f"| {i+1} | {firstname} {lastname}")
                print("▔▔▔▔▔")
            elif i == 2:
                print("___")
                print(f"[{i + 1}] {firstname} {lastname}")
                print("▔▔▔")
            else:
                print(f"{i+1}. {firstname} {lastname}")

        mainPrompt()  # Go back to the main menu

    # Handles exception for when the query is invalid
    except:
        print("\nInvalid season or round")
        getRaceResults()

# Run program
print("\nWelcome to the F1 command line app!")
mainPrompt()
print("\nThank for using the F1 command line app!")