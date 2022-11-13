import requests

class Super_hero:
    URL = 'https://akabab.github.io/superhero-api/api'
    def __init__(self, name, id):
        self.name = name
        self.powerstats = requests.get(self.URL + f'/powerstats/{id}.json').json()

def smartest(hero_1, hero_2, hero_3):
    intelligence = {hero_1: hero_1.powerstats['intelligence'], hero_2: hero_2.powerstats['intelligence'], hero_3: hero_3.powerstats['intelligence']}
    return max(intelligence, key=intelligence.get).name

Hulk = Super_hero('Hulk', 332)
Captain_America = Super_hero('Captain_America', 149)
Thanos = Super_hero('Thanos', 655)

print(smartest(Hulk, Captain_America, Thanos))