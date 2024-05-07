from datetime import datetime
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
            planots = input("Ievadiet ko jūs planojat darīt šajā laikā?") #iegūst plānu
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