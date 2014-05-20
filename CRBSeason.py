from Season import *

class CRBSeason(SixteenTeamDivisionalSeason):
    division_defs = {"Insular": ("Santo Domingo", "Port-au-Prince", "Havana", "Santiago"),
                     "Continental": ("San Juan", "Ponce", "Guyana", "Suriname"),
                     "Commonwealth": ("Nassau", "Kingston", "Port of Spain", "Barbados"),
                     "Territorial": ("Virgin Islands", "Netherlands Antilles", "French Islands", "British West Indies")}
    division_names = ("Insular", "Continental", "Commonwealth", "Territorial")
    seeds = ("INS", "CON", "COM", "TER", "CAR", "ISL")
    labels = ("Insular", "Continental", "Commonwealth", "Territorial", "Caribbean", "Island")
    placeholders = ("Insular", "Continental", "Commonwealth", "Territorial", "Caribbean", "Island")
    name = "Caribbean"
    
