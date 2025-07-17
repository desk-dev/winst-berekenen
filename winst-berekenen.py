def winst_berekenen():
    omzet = float(input("Omzet afgelopen boekjaar: € "))
    inkoop = float(input("Inkoopkosten: € "))
    kosten = float(input("Overige kosten: € "))
    winst = omzet - inkoop - kosten
    print(f"Je winst is €{winst:,.2f}")
    if omzet:
        print(f"Marge: {winst / omzet * 100:.2f}%")

winst_berekenen()