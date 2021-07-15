import json
import httpx

headers = {"TRN-Api-Key": "2813993b-99c4-4e0c-b511-fa59d121674b"}

with open("countries.json", "r") as countriesFile:
	codes = json.load(countriesFile)

class CSGOTracker:
    def __init__(self, playername):
        req = httpx.get(f"https://public-api.tracker.gg/v2/csgo/standard/profile/steam/{playername}/", headers=headers)
		res = req.text
            
        try:
            self.name = json.loads(res.text)["data"]["platformInfo"]["platformUserHandle"]
            self.kills = json.loads(res.text)["data"]["segments"][0]["stats"]["kills"]["value"]
            self.deaths = json.loads(res.text)["data"]["segments"][0]["stats"]["deaths"]["value"]
            self.kd = json.loads(res.text)["data"]["segments"][0]["stats"]["kd"]["displayValue"]   
            self.damage = json.loads(res.text)["data"]["segments"][0]["stats"]["damage"]["displayValue"]
            self.headshots = json.loads(res.text)["data"]["segments"][0]["stats"]["headshots"]["value"]
            self.shotsFired = json.loads(res.text)["data"]["segments"][0]["stats"]["shotsFired"]["displayValue"]
            self.shotsAccuracy = json.loads(res.text)["data"]["segments"][0]["stats"]["shotsAccuracy"]["displayValue"]
            self.bombsPlanted = json.loads(res.text)["data"]["segments"][0]["stats"]["bombsPlanted"]["displayValue"]
            self.moneyEarned = json.loads(res.text)["data"]["segments"][0]["stats"]["moneyEarned"]["displayValue"]
            self.wins = json.loads(res.text)["data"]["segments"][0]["stats"]["wins"]["displayValue"]
            self.losses = json.loads(res.text)["data"]["segments"][0]["stats"]["losses"]["displayValue"]
            self.matchesPlayed = json.loads(res.text)["data"]["segments"][0]["stats"]["matchesPlayed"]["displayValue"]
            self.wlr = json.loads(res.text)["data"]["segments"][0]["stats"]["wlPercentage"]["displayValue"]
            self.hsp = json.loads(res.text)["data"]["segments"][0]["stats"]["headshotPct"]["displayValue"]
        except:
            print("An unknown error occurred...")

class ApexLegendsTracker:
    def __init__(self, playername, playerplatform):
        req = requests.get(f"https://public-api.tracker.gg/v2/apex/standard/profile/{playerplatform}/{playerplatform}", headers=headers)

        try:
            self.name = json.loads(res.text)["data"]["platformInfo"]["platformUserHandle"]

            if json.loads(res.text)["data"]["platformInfo"]["platformUserHandle"] == "psn":
                self.platform = "PlayStation Network"
            elif json.loads(res.text)["data"]["platformInfo"]["platformUserHandle"] == "xbl":
                self.platform = "Xbox Live"
            else:
                self.platform = "Origin PC"

            self.country = codes[json.loads(res.text)["data"]["userInfo"]["countryCode"]]

            self.level = json.loads(res.text)["data"]["segments"][0]["stats"]["level"]["displayValue"]
            self.kills = json.loads(res.text)["data"]["segments"][0]["stats"]["kills"]["displayValue"]
            self.kpm = json.loads(res.text)["data"]["segments"][0]["stats"]["kpm"]["displayValue"]
            self.winningkills = json.loads(res.text)["data"]["segments"][0]["stats"]["winningKills"]["displayValue"]
            self.damage = json.loads(res.text)["data"]["segments"][0]["stats"]["damage"]["displayValue"]
            self.matchesPlayed = json.loads(res.text)["data"]["segments"][0]["stats"]["matchsPlayed"]["displayValue"]
            self.revives = json.loads(res.text)["data"]["segments"][0]["stats"]["revives"]["displayValue"]
            self.sniperkills = json.loads(res.text)["data"]["segments"][0]["stats"]["sniperKills"]["displayValue"]
        except:
            print("An unknown error occurred.")