"""
Created on Tue Sep 22 20:01:05 2026

@author: Nicolas Ekholdt

This script is a trial for the required work task in PY1010 USN. 
I take no responsibility for errors in this program, as this is my first trial
at coding. 

Version 1.0.1

Oppgavetekst:
    Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene ved elbil sammenliknet med bensinbil.

    Lag et Python-program som beregner og presenterer (viser) de årlige totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. Du kan her for enkelhets skyld se bort fra kostnader som renter på billån og verditap (du har da egentlig antatt at slike kostnader er like for elbil og bensinbil).

    Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)

    Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
    Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
    Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
    Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
    Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.
"""
Di = 10000  # [Kilometer per year]

FEl = 5000 # [Kroner per year] 
FBe = 7500 # [Kroner per year] 

TF = 8.38 # [Kroner per day] 
TFy = TF*365 # [Kroner per year] 

DrEl = 0.2*2 # [Kroner per kilometer]
DrBe = 1 # [Kroner per kilometer] 

BEl = 0.1 # [Kroner per kilometer]
BBe = 0.3 # [Kroner per kilometer]

TotEl = Di*(DrEl + BEl) + FEl + TFy # [Kroner per year]
TotBe = Di*(DrBe + BBe) + FBe + TFy # [Kroner per year] 

Dif = TotBe - TotEl #[Kroner per year]

print("Yearly cost of electric car =", TotEl,"kr")
print("Yearly cost of gas car =", TotBe,"kr")
print("Difference in yearly cost are", Dif, "kr") 