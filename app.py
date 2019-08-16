import tkinter as tk
import datetime
import requests

HEIGHT = 400
WIDTH = 700

def runQuery():
    """
    Runs a GET request to the Ergast API to retrieve information about the round selected.
    """
    try:
    	URL = f"http://ergast.com/api/f1/{seasonSelected.get()}/{roundSelected.get()}/results/1.json"
    	req = requests.get(url=URL)
    	data = req.json()
    	firstname = data['MRData']['RaceTable']['Races'][0]['Results'][0]['Driver']['givenName']
    	lastname = data['MRData']['RaceTable']['Races'][0]['Results'][0]['Driver']['familyName']
    	winnerLabel.configure(text=f"Winner: {firstname} {lastname}")
    except:
    	winnerLabel.configure(text="Round invalid for this season.")

# --- Define main window ---

root = tk.Tk()
root.title("F1 Race Results")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#bd0000')
frame.place(relwidth=1, relheight=1)

# --- Define widgets ---

# Season label
seasonLabel = tk.Label(frame, text="Season:")
seasonLabel.grid(row=0, column=0)

# Season selection
c_year = int(datetime.datetime.now().year)
seasonList = range(1950, c_year+1)
seasonSelected = tk.StringVar(frame)
seasonSelected.set("Season")
seasonSelection = tk.OptionMenu(frame, seasonSelected, *seasonList)
seasonSelection.grid(row=0, column=1)

# Round label
roundLabel = tk.Label(frame, text="Round:")
roundLabel.grid(row=1, column=0)

# Round selection
roundList = range(1, 22)
roundSelected = tk.StringVar(frame)
roundSelected.set("Round")
roundSelection = tk.OptionMenu(frame, roundSelected, *roundList)
roundSelection.grid(row=1, column=1)

submitBtn = tk.Button(frame, text="Submit", command=runQuery)
submitBtn.grid(row=2, column=0)

winnerLabel = tk.Label(frame, text="Winner:")
winnerLabel.grid(row=3, column=0)

root.mainloop()







