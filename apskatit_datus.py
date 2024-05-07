import datetime
def apskatit_datus(): # funkcija izvada iepriekš ievadītā datuma plānus(jā tājā datumā kaut ko ieplānoja)
    while True:
        try:
            
            datums = input("Kuru datumu vēlaties apskatīt? datums: YYYY-MM-DD:")
            
            try:
                plani = {}
                with open(datums+'.txt', 'r',encoding='utf8') as file:
                    for line in file.readlines():
                        atslega, vertiba = line.strip().split(' : ')   
                        plani[atslega] = vertiba                      # ieliek vārdnīcā laiku kā atslēgu un darbu kā vērtību
                sakartota = dict(sorted(plani.items()))               # sakārto pēc laikiem augošā secībā
                for key, value in sakartota.items():                  
                    print(key, ":", value)
            except FileNotFoundError:         # ja ieraksta datumu kurš nav
                print("Tāds datums nav!")

        except ValueError:
            print("Nepareizi dati! Vadi vēlreiz!!!")
            
apskatit_datus()
