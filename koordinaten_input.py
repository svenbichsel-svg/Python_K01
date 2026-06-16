Ost = float(input("Geben die Ost-Koordinate ein: "))
Nord = float(input("Geben die Nord-Koordinate ein: "))

o_formatiert = f"{Ost:,.0f}".replace(",", "'")
n_formatiert = f"{Nord:,.0f}".replace(",", "'")

print (o_formatiert, n_formatiert)

if 2480000 <= Ost <= 2840000 and 1070000 <= Nord <= 1300000:
      print("liegt innerhalb der Schweiz.")
else:
    print("liegt ausserhalb der Schweiz.")
