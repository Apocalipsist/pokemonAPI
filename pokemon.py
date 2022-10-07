import requests


res = requests.get('https://pokeapi.co/api/v2')
res.json()





class PokemonAPI:
    api_method = "pokemon/"
    base_url = 'https://pokeapi.co/api/v2/'
    
    def __init__(self, pokemon):
        self.pokemon = pokemon
        
        
    def _get(self):
        request_url = f"{self.base_url}{self.api_method}{self.pokemon}"
        pokepedia = requests.get(request_url)
        return pokepedia.json()


class Pokemon(PokemonAPI):

    def __init__(self, pokemon):
        super().__init__(pokemon)
        
        
    def get_height(self):
        pokepedia = self._get()
        height = pokepedia['height']
        return height
        
        
    def get_weight(self):
        pokepedia = self._get()
        weight = pokepedia["weight"]
        return weight

# prof_oak = PokemonAPI()
    
def pokedex():
    print("Hello, welcome to the world of Pokemon!")
    while True:
        whos_that_pokemon = input("""\nMy name is Professor Oaks!\nThis is a Pokedex it will aid you in your journey to be a Pokemon Master!\nWhat is the name of the Pokemon you want to learn more about? 
When you want to get back to your journey please press 'A' """).lower()
        if whos_that_pokemon.lower() == "a":
            break
        prof_oak = Pokemon(whos_that_pokemon)
        poke_height = prof_oak.get_height()
        poke_weight = prof_oak.get_weight()
        print(f'That Pokemon is {whos_that_pokemon.title()} They measure about {poke_height}m in height and weighs {poke_weight}lbs.')
        
        
    # couldn't figure out how to fix the pokedex
    
    
# end def        
        
pokedex()