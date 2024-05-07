print('Labdien')
def redige_failu(datums):
    while True:
        darbiba = int(input('Ko jūs gribat darīt?\n1)Pievienot plānu\n2)Izdzēst planu\n3)Rediģēt failu\nAtbildēt ar (1/2/3)'))
        if darbiba == 1:
            with open(datums+'.txt','a',encoding='utf8') as fails:
                laiks = input('ievadiet laiku (hh-mm): ')
                plans = input('ievadiet plānu: ')
                fails.write(f"{laiks} : {plans}\n")

        elif darbiba == 2:
            plani = {}
            with open(datums+'.txt', 'r',encoding='utf8') as file:
                for line in file.readlines():
                    atslega, vertiba = line.strip().split(' : ')
                    plani[atslega] = vertiba
            sakartota = dict(sorted(plani.items()))
            for key, value in sakartota.items():
                print(key, ":", value)
            while True:
                laiks_dzest = input('kuru laiku jus gribat izdzest: ')
                if laiks_dzest in sakartota.keys():
                    del sakartota[laiks_dzest]
                    with open(datums+'.txt','w',encoding='utf8') as fails:
                        fails.write('')
                    for key, value in sakartota.items():
                        print(key, ":", value)
                        with open(datums+'.txt','a',encoding='utf8') as fails:
                            darbs = (key+" : "+value+'\n')
                            fails.write(darbs)
                    print('\n-------------\n')
                    break
                else:
                    print('ievadiet pareizu laiku')

        elif darbiba == 3:
            plani = {}
            with open(datums+'.txt', 'r',encoding='utf8') as file:
                for line in file.readlines():
                    atslega, vertiba = line.strip().split(' : ')
                    plani[atslega] = vertiba
            sakartota = dict(sorted(plani.items()))
            for key, value in sakartota.items():
                print(key, ":", value)
            while True:
                laiks_mainit = input('kuru laiku jus gribat izdzest: ')
                if laiks_mainit in sakartota.keys():
                    plans_mainit = input('ievadiet jauno plānu: ')
                    sakartota.update({laiks_mainit:plans_mainit})
                    with open(datums+'.txt','w',encoding='utf8') as fails:
                        fails.write('')
                    for key, value in sakartota.items():
                        print(key, ":", value)
                        with open(datums+'.txt','a',encoding='utf8') as fails:
                            darbs = (key+" : "+value+'\n')
                            fails.write(darbs)
                    print('\n-------------\n')
                    break
                else:
                    print('ievadiet pareizu laiku')

        else:
            print('Ievadiet(1/2/3)')


 




redige_failu('2024-12-03')