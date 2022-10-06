import requests


res = requests.get('https://pokeapi.co/api/v2')
res.json()


pokepedia = res.json()


class PokemonAPI:
    base_url = 'https://pokeapi.co/api/v2/'
    api_method = "pokemon/"
    
    def __init__(self, pokemon):
        self.pokemon = pokemon
        
    def get(self, api_method, pokemon):
        request_url = f"{self.base_url}{api_method}{pokemon}"
        res = requests.get(request_url)
        return res.json()
    
    def get_height(self, pokemon):
        pokepedia = self.get("pokemon/",pokemon)
        height = pokepedia['height']
        return height
        
    def get_weight(self, pokemon):
        pokepedia = self.get("pokemon/", pokemon)
        weight = pokepedia["weight"]
        return weight
    
    

    
def pokedex():
    poke_storage = []
    print("Hello welcome to the world of pokemon!")
    while True:
        whos_that_pokemon = input("""What is the name of the pokemon you want to learn more about? 
        When you want to get back to your journey please press 'A' """)
        if whos_that_pokemon.lower == "a":
            break
        prof_oak = PokemonAPI(whos_that_pokemon)
        for pokemon in whos_that_pokemon:
            poke_height = prof_oak.get_height(pokemon)
            poke_weight = prof_oak.get_weight(pokemon)
            poke_storage.append(poke_height, poke_weight)
        print(f'That pokemon is {whos_that_pokemon} They measue about {poke_storage.get_height()}in in height and weights {poke_storage.get_weight()}.')
        
        
    # couldn't figure out how to fix the pokedex
    
    
# end def        
        
pokedex()