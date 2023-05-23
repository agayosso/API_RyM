import requests

def obt_personajes_principales():
    url = "https://rickandmortyapi.com/api/character"
    params = {
        "page": 1,
        "status": "alive"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["results"]

personajes_principales = obt_personajes_principales()

for personaje in personajes_principales:
    print(personaje["name"])