def winst_berekenen():
    omzet = float(input("Omzet afgelopen boekjaar: € "))
    inkoop = float(input("Inkoopkosten: € "))
    kosten = float(input("Overige kosten: € "))
    bruto_winst = omzet - inkoop
    netto_winst = bruto_winst - kosten
    print(f"Je bruto winst is €{bruto_winst:,.2f}")
    print(f"Je netto winst is €{netto_winst:,.2f}")
    if omzet:
        print(f"Bruto marge: {bruto_winst / omzet * 100:.2f}%")
        print(f"Netto marge: {netto_winst / omzet * 100:.2f}%")

winst_berekenen()