import time
import locale
locale.setlocale(locale.LC_ALL,"de_CH")

eingabe = input("Gib dein Geburtsdatum ein (TT.MM.JJJJ): ")


geburtstag = time.strptime(eingabe, "%d.%m.%Y")


wochentag_geburt = time.strftime("%A", geburtstag)
print(f"Du wurdest an einem {wochentag_geburt} geboren.")


geburtstag_30 = time.strptime(f"{geburtstag.tm_mday}.{geburtstag.tm_mon}.{geburtstag.tm_year + 30}", "%d.%m.%Y")
wochentag_30 = time.strftime("%A", geburtstag_30)
print(f"Deinen 30. Geburtstag feierst du an einem {wochentag_30}.")





# eingabe = input("Gib dein Geburtsdatum ein (TT.MM.JJJJ): ")


# geburtstag = time.strptime(eingabe, "%d.%m.%Y")


# wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

# wochentag_geburt = wochentage[geburtstag.tm_wday]
# print(f"Du wurdest an einem {wochentag_geburt} geboren.")

# geburtstag_30 = time.strptime(f"{geburtstag.tm_mday}.{geburtstag.tm_mon}.{geburtstag.tm_year + 30}", "%d.%m.%Y")
# wochentag_30 = wochentage[geburtstag_30.tm_wday]
# print(f"Deinen 30. Geburtstag feierst du an einem {wochentag_30}.")