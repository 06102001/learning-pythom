#Script description:

import requests
import os
os.system('clear')

def get_comets():
    global comet
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    print("::: COMET INFORMATION::::")

    try:
        #Request to API
        response = requests.get(url)
        response.raise_for_status()

        #Convertir la respuesta a formato JSON (JS Object Notation)
        data = response.json() #Convierte en JSON
        #Print all comets names
        count = 0

        print(":::SOLAR SYSTEM MENU:::")
        print("[1]. Planets")
        print("[2]. Moons")
        print("[3]. Stars")
        print("[4]. Asteroid")
        print("[5]. Comets")
        opt = int(input("Choose and option: "))

        if opt == 1:
            body_type = "Planet"
        elif opt == 2:
            body_type = "Moons"
        elif opt == 3:
            body_type = "Stars"
        elif opt == 4:
            body_type = "Asteroid"
        elif opt == 5:
            body_type = "Comets"
        else:
            print(":::Invalid Option:::")

        total = int(input("Cantidad de datos a mostrar: "))
        
        print("\n")

        for comet in data["bodies"]:

            #if comet["isPlanet"] == True:
            if comet["bodyType"] == body_type:
                print("english name: ", comet["englishName"])
                #print("english moons: ", comet["moons"])
                print("english gravity: ", comet["gravity"])
                print("Is planet?: ", comet["isPlanet"])
                print("\n")

                count = count + 1
            if count == total:
                break
        print(count)    

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")


#Call fuction
get_comets()