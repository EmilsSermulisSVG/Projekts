from datetime import datetime
def iegut_datus():
    plans = {
        "datums":""
    }
    while True:
        try:
            datums = input("Ievadiet datumu kur jūs ievadīsiet plānu formā YYYY-MM-DD: ")
            format = "%Y-%m-%d"
            pareizs = bool(datetime.strptime(datums, format))
            datums_formata = datetime.strptime(datums, format)
            pasreizejs_datums = datetime.now().strftime("%Y-%m-%d")
            pasreizejs_datums = datetime.strptime(pasreizejs_datums, format)
            if datums_formata < pasreizejs_datums:
                print("Datums nevar būt mazāks par šodienas datumu.")
                continue
            elif pareizs == True:
                break
        except ValueError:
            print('Nepareizs datu formāts. Lūdzu, ievadiet datumu vēlreiz')
    plans.update({"datums":datums})
    while True:
        try:
            laiks = input("Ievadiet laiku kad šīs plāns notiks formā HH-MM: ")
            format = "%H-%M"
            pareizs = bool(datetime.strptime(laiks, format))
            datums_formata = datetime.strptime(laiks, format)
            pasreizejs_laiks = datetime.now().strftime("%H-%M")
            pasreizejs_laiks = datetime.strptime(pasreizejs_laiks, format)
            if datums_formata < pasreizejs_laiks:
                print("laiks nevar būt mazāks par pašreizējo laiku.")
                continue
            elif pareizs != True:
                print("Nepareizs datu formāts. Lūdzu, ievadiet datumu vēlreiz")
                continue
            planots = input("Ievadiet ko jūs planojat darīt šajā laikā?")
            plans.update({laiks:planots})
            vai_turp = input("Vai ir vēl plāni(j/n)?")
            if vai_turp == "j":
                continue
            elif vai_turp == "n":
                break
        except ValueError:
            print('Nepareizs datu formāts. Lūdzu, ievadiet laiku vēlreiz')
    return plans
plans = iegut_datus()
print(plans)
def saglabat_datus(plans):
    datums = plans.pop("datums")
    with open(f'{datums}.txt','w',encoding='utf8') as fails:
        for laiks, value in plans.items():
                fails.write(f"{laiks} : {value}\n")
saglabat_datus(plans)