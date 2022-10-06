import requests


res = requests.get('https://pokeapi.co/api/v2')
res.json()


poke_dex = res.json()


class PokemonAPI:
    base_url = 'https://pokeapi.co/api/v2'
    api_method = "/pokemon/"
    
    def __init__(self, pokemon):
        self.pokemon = pokemon
        
    def get(self):
        request_url = f"{self.base_url}{self.api_method}{self.pokemon}"
        res = requests.get(request_url)
        return res.json()
    
    def get_height(self):
        poke_dex = self.get()
        height = poke_dex['height']
        return height
        
    def get_weight(self):
        poke_dex = self.get()
        weight = poke_dex["weight"]
        return weight
    
        
        
poke = PokemonAPI("charizard")
print(poke.get_height())
print(poke.get_weight())