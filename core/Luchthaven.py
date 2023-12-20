import re

class Luchthaven():

    def init(self):
        print("Welkom in de luchthaven applicatie.\n")
        print("1) Bekijk geplande vluchten")
        print("2) Voeg een vlucht toe")
        print("3) Schrap een vlucht")
        print("4) Beëindig sessie\n")

        while True:
            try:
                print("Gelieve een optie te selecteren")
                choice = input("> ").strip()
                if re.match(r'^[1-4]$', choice):
                    match choice:
                        case "1":
                            pass
                        case "2":
                            pass
                        case "3":
                            pass
                        case "4":
                            print("\n\nTot ziens!")
                            return;
                else:
                    print("Gelieve een getal tussen 1 en 4 in te vullen.")
            except ValueError:
                print("Gelieve een geldige waarde in te vullen.")

        

        
