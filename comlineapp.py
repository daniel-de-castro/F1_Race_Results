import requests

def mainPrompt():
    query = input("\nWhat do you want to do?\n1 - See race results\n2 - Exit program\ntype number >>  ")
    if query == "1":
        getRaceResults()
    elif query != "2":
        print("\nThis is not a valid option!")
        mainPrompt()

def getRaceResults():
    print("\nInput F1 season and number of round to get results")
    season = input("Season: ")
    round = input("Round: ")

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

        mainPrompt()

    except:
        print("\nInvalid season or round")
        getRaceResults()

print("\nWelcome to the F1 command line app!")
mainPrompt()
print("\nThank for using the F1 command line app!")