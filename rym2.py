import requests

def obt_personajes():
    url = "https://rickandmortyapi.com/api/character"
    params = {
        "page": 1
    }
    response = requests.get(url, params=params)
    
    tiempo_respuesta = response.elapsed.total_seconds()
    print("Tiempo de respuesta:", tiempo_respuesta, "segundos")
    
    codigo_estado = response.status_code
    print("Código de estado:", codigo_estado)
    
    if response.ok:
        data = response.json()
        
        personajes_vivos = []
        personajes_muertos = []
        for personaje in data["results"]:
            if personaje["status"] == "Alive":
                personajes_vivos.append(personaje["name"])
            elif personaje["status"] == "Dead":
                personajes_muertos.append(personaje["name"])
        
        print("Personajes vivos:", personajes_vivos)
        print("Personajes muertos:", personajes_muertos)
        
        print("Tipo de dato de 'info':", type(data["info"]))
        print("Tipo de dato de 'results':", type(data["results"]))
    else:
        print("Error en la solicitud:", response.text)

obt_personajes()