from random import randint
import requests
from datetime import datetime, timedelta




class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.types = self.get_types()
        self.hp = randint(50, 100)
        self.power = randint(5, 15)
        self.last_feed_time = datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        pass
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['other']['official-artwork']['front_default']
        else:
            return  "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
        

    def get_types(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [t['type']['name'] for t in data['types']]
        else:
            return ['normal']
        
    def attack(self, enemy):
        if enemy.__class__.__name__ == "Wizard" and randint(1, 5) == 1:
            return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else: 
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        
    def feed(self, feed_interval=20, hp_increase=10):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            next_time = self.last_feed_time + delta_time
            return f"Рано кормить. Следующее время кормления: {next_time.strftime('%H:%M:%S')}"
    
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}\n Типы: {', '.join(self.types)}, Здоровье (HP): {self.hp} Сила атаки (Power): {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img






class Fighter(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.base_power = self.power
        self.super_attack_ready = True
    

    def attack(self, enemy):
        power_boost =  randint(5, 15)
        self.power += power_boost
        result = super().attack(enemy)
        self.power = self.base_power
        return result +f"\n Боец {self.name} Боец применил супер-атаку силой, +{power_boost} к силе атаки!"
    
    def feed(self, feed_interval=20, hp_increase=20):
        reduced_interval = feed_interval
        result = super().feed(reduced_interval, hp_increase)
        return result + f"Боец {self.name} набрался сил и стал крепче!"





class Wizard(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.magic_shield = False
    
    def activate_shield(self):
        self.magic_shield = True
        return f" {self.name} активировал магический щит! (Шанс уклонения 20%)"
    
    def attack(self, enemy):
        if self.magic_shield:
            self.hp += 5
            self.magic_shield = False
            return f"{self.name} блокирует атаку щитом и восстанавливает пять хп"
        return super().attack(enemy)
    


def feed(self, feed_interval=10, hp_increase=10):
        result = super().feed(feed_interval, hp_increase)
        return result + f"  Волшебник {self.name} питается чаще благодаря магии!"