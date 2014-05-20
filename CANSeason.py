from Season import *

class CANSeason(SixteenTeamDivisionalSeason):
    division_defs = {"Canadian East": ("Toronto", "Ottawa", "Montreal", "Quebec City"),
                     "Canadian West": ("Edmonton", "Calgary", "Vancouver", "Winnipeg"),
                     "National East": ("Halifax", "Charlottetown", "Hamilton", "Windsor"),
                     "National West": ("Saskatoon", "Regina", "Anchorage", "Victoria")}
    division_names = ("Canadian East", "Canadian West", "National East", "National West")
    seeds = ("CE", "CW", "NE", "NW", "CAN", "NAT")
    labels = ("East", "West", "East", "West", "Canadian", "National")
    placeholders = ("Canadian East", "Canadian West", "National East", "National West", "Canadian", "National")
    name = "Canada"
    
