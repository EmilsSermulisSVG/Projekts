from datetime import datetime

print('labdien\n---------------\n')

def iegut_datus(): #Funkcija kura iegūst datumu, laiku un pārbauda vai tie ir pareizi formatēti un vai nav pagātnē, kā arī iegūst plānu
    plans = {
        "datums":""
    }
    while True: #iegūst darumu
        try:
            datums = input("Ievadiet datumu kur jūs ievadīsiet plānu formā YYYY-MM-DD: ")
            format = "%Y-%m-%d" #formās daumam
            pareizs = bool(datetime.strptime(datums, format)) #pārbauda vai ir pareiz formatējum
            datums_formata = datetime.strptime(datums, format) #pārveido uz datetime tipu 
            pasreizejs_datums = datetime.now().strftime("%Y-%m-%d")#iegūst pašreizējo datumu 
            pasreizejs_datums = datetime.strptime(pasreizejs_datums, format) #pārveido uz datetime tipu 
            if datums_formata < pasreizejs_datums:
                print("Datums nevar būt mazāks par šodienas datumu.")
                continue
            elif pareizs == True: #ja ir pareiz formatēts tad beidz while ciklu
                break
        except ValueError:
            print('Nepareizs datu formāts. Lūdzu, ievadiet datumu vēlreiz')
    plans.update({"datums":datums}) #datumu ieliek dict plans
    while True: #igūst laiku un plānu
        try:
            laiks = input("Ievadiet laiku kad šīs plāns notiks formā HH-MM: ")
            format = "%H-%M" #laika formatējum
            pareizs = bool(datetime.strptime(laiks, format)) #pārbauda vai ir pareizs formatējum
            datums_formata = datetime.strptime(laiks, format) #pārveido uz datetime tipu 
            if pareizs != True:#ja ir nepareizi formatēts tad sāk no sākuma while ciklu
                print("Nepareizs datu formāts. Lūdzu, ievadiet datumu vēlreiz")
                continue
            planots = input("Ievadiet ko jūs planojat darīt šajā laikā? ") #iegūst plānu
            plans.update({laiks:planots}) # ievieto laiku kā key un plānu kā value
            vai_turp = input("Vai ir vēl plāni(j/n)?") #vai lietotājs grib pierakstīt vēl plānus
            if vai_turp == "j":
                continue
            elif vai_turp == "n":
                break
        except ValueError:
            print('Nepareizs datu formāts. Lūdzu, ievadiet laiku vēlreiz')
    return plans

def saglabat_datus(plans): #sglabā datus pēc formāta "laiks : plans"
    datums = plans.pop("datums") #izņem datumu no dict
    with open(f'{datums}.txt','a',encoding='utf8') as fails: #izveiod jaunu failu vai ieliek eksistējošā
        for laiks, value in plans.items(): #izņem no vārdnīcas laiku un plānu
                fails.write(f"{laiks} : {value}\n") #katru ieliek failā pēc formāta

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
                rediget = input('vai jūs gribat rediģēt plānu (j/n): ')
                if rediget == 'j':
                    redige_failu(datums)
                    break
                else:
                    break
            except FileNotFoundError:         # ja ieraksta datumu kurš nav
                print("Tāds datums nav!")

        except ValueError:
            print("Nepareizi dati! Vadi vēlreiz!!!")




def redige_failu(datums):
    while True:
        darbiba = int(input('kā jūs gribat rediģēt?\n1)Pievienot plānu\n2)Izdzēst planu\n3)Rediģēt plānu\nAtbildēt ar (1/2/3): '))

        if darbiba == 1: #pievieno plānu failam
            with open(datums+'.txt','a',encoding='utf8') as fails:
                laiks = input('ievadiet laiku (hh-mm): ')
                plans = input('ievadiet plānu: ')
                fails.write(f"{laiks} : {plans}\n")#pievieno

        elif darbiba == 2:#izdzēš plānu no faila
            plani = {}
            with open(datums+'.txt', 'r',encoding='utf8') as file:
                for line in file.readlines():
                    atslega, vertiba = line.strip().split(' : ')#atdala laiku un plānu
                    plani[atslega] = vertiba
            sakartota = dict(sorted(plani.items()))
            for key, value in sakartota.items():
                print(key, ":", value) #parāda visus plānus vienā datumā
            while True:
                laiks_dzest = input('kuru laiku jus gribat izdzest: ')
                if laiks_dzest in sakartota.keys():#parbauda vai ir tāds laiks
                    del sakartota[laiks_dzest]
                    with open(datums+'.txt','w',encoding='utf8') as fails:
                        fails.write('') #iztukšo failu lai var ielikt atpakaļ bez izdzēstā
                    for key, value in sakartota.items():
                        print(key, ":", value)#parāda visus plānus vienā datumā bez izdzēstā
                        with open(datums+'.txt','a',encoding='utf8') as fails:
                            darbs = (key+" : "+value+'\n')
                            fails.write(darbs)#pievieno visus datus failam
                    print('\n-------------\n')
                    break
                else:
                    print('ievadiet pareizu laiku')

        elif darbiba == 3:#rediģē plānu failā
            plani = {}
            with open(datums+'.txt', 'r',encoding='utf8') as file:
                for line in file.readlines():
                    atslega, vertiba = line.strip().split(' : ')#atdala laiku no plāna
                    plani[atslega] = vertiba
            sakartota = dict(sorted(plani.items()))
            for key, value in sakartota.items():
                print(key, ":", value)#parāda visus plānus vienā datumā
            while True:
                laiks_mainit = input('kuru laiku jus gribat rediģēt: ')
                if laiks_mainit in sakartota.keys():#parbauda vai ir tāds laiks
                    plans_mainit = input('ievadiet jauno plānu: ')
                    sakartota.update({laiks_mainit:plans_mainit}) #rediģē plānus
                    with open(datums+'.txt','w',encoding='utf8') as fails:
                        fails.write('')#iztukšo failu lai var ielikt jauno bez rediģētā
                    for key, value in sakartota.items():
                        print(key, ":", value)
                        with open(datums+'.txt','a',encoding='utf8') as fails:
                            darbs = (key+" : "+value+'\n')
                            fails.write(darbs)#plānus ieraksta failā
                    print('\n-------------\n')
                    break
                else:
                    print('ievadiet pareizu laiku')
            break
        else:
            print('Ievadiet(1/2/3)')

def galvenais():
    while True:
        print('1)pievienot planus\n2)apskatīt,rediģēt plānus\nstop = stop')
        darbiba = input('ko jūs gribat darīt: ')
        if darbiba == 'stop':
            exit('paldies par lietošanu')
        elif darbiba == '1':
            saglabat_datus(iegut_datus())
        elif darbiba == '2':
            apskatit_datus()
        else:
            print('ievadiet (1/2/stop)')

galvenais()