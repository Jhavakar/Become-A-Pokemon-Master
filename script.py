poketypes = {
    'Fire': {
        'Water': 1,
        'Grass': 2
    },
    'Water': {
        'Fire': 2,
        'Grass': 1
    },
    'Grass': {
        'Fire': 1,
        'Water': 2
    }

}


class Pokemon:

  is_knocked_out = False

  def __init__(self, name, level, type, is_knocked_out):
    self.name = name
    self.level = level
    self.type = type
    self.max_health = level
    self.health = self.max_health
    self.is_knocked_out = is_knocked_out
    self.experience = 0

  def __repr__(self):
    return "Pokemon info. {}, current level: {}, type: {}, maximun health: {}, current health: {}.\n".format(self.name, self.level, self.type, self.max_health, self.health)

  def lose_health(self, health):
      self.health -= health
      if self.health <= 0:
          self.health = 0
          self.knock_out()
      else:
            print('{} now has {} health.'.format(self.name, self.health))

  def gain_health(self, health):
    self.health += health
    if self.health > self.level:
            self.health = self.level
    else:
        print('{} now has {} health.'.format(self.name, self.health))

  def knock_out(self):
      self.is_knocked_out = True
      print('{} now has been knocked out!\n'.format(self.name))

  def revive(self, pokemon, health):
        pokemon.is_knocked_out = False
        print('{} now has been revived.\n'.format(pokemon.name))
  
  def attack(self, other_pokemon):
      multiplier = poketypes[self.type][other_pokemon.type]
      attack = 1 * multiplier
      print('{} attacked {} with {}.'.format(self.name, other_pokemon.name, attack))
      if multiplier == 2:
          print("It wasn't powerful enough.")
      elif multiplier == 0:
          print("Wow that's powerful.")
      other_pokemon.lose_health(attack)


  def gain_experience(self, experience):
    self.experience += experience
    print("{} gained {}xp.\n".format(self.name, experience))
    if self.experience >= 3:
      self.level_up()
  
  def level_up(self):
    self.experience = 0
    self.level += 1
    self.max_health += 1
    self.health = self.max_health
    print("{} leveled up to level {}! Max health now is {}.\n".format(self.name, self.level, self.max_health))


class Trainer:
  def __init__(self, name, pokemons, potions, current_pokemon):
    self.name = name
    self.pokemons = pokemons[:5]
    self.potions = potions
    self.current_pokemon = current_pokemon
    self.pokemon = pokemons[0]
    

  def use_potion(self):
   if self.potions > 0:
      if self.current_pokemon.health < self.current_pokemon.max_health:
         self.current_pokemon.gain_health(1)
         self.potions -= 1
      print("{} has {} potions left.\n".format(self.name, self.potions))
   else:
      print("{}, you have no potions!\n".format(self.name)) 

  def attack(self, other_pokemon):
    self.pokemon.attack(other_pokemon.pokemon)
    print('{} is knocked out, please choose another.\n'.format(self.pokemon.name,))
  
  
  def switch_pokemon(self, number):   
    if self.pokemons[number] == self.pokemons:
            print('{} cannot swap out active pokemon with active pokemon.\n'.format(self.name))
    elif not self.pokemons[number].is_knocked_out:
            print('{} swapped out {}with {}.\n'.format(self.name, self.current_pokemon, self.pokemons[number]))
            self.pokemon = self.pokemons[number]
    else:
            print('{} is knocked out. Choose another pokemon, {}.\n'.format(self.pokemons[number], self.name))

    def __repr__(self):
        print('{} currently has the following pokemons:\n'.format(self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return 'Current pokemon: {}.\n'.format(self.pokemon)


class Charmander(Pokemon):
  def __init__(self, name, level, type, is_knocked_out):
    super().__init__(name, level, type, is_knocked_out)
  
  def destroy(self, other_pokemon):
    other.lose_health(other_pokemon.health)
    print("{} totally destroyed {}!\n".format(self.name, other_pokemon.name))



pikachu = Pokemon("Pikachu", 3, "Fire", False)
bulbasaur = Pokemon("Bulbasaur", 3, "Grass", False)
magikarp = Pokemon("Magikarp", 1, "Water", False)
charmander = Charmander("Charmander", 3, "Fire", False)


Ash = Trainer('Ash', [pikachu], 3, pikachu)

Jhava = Trainer('Jhava', [bulbasaur, magikarp], 3, bulbasaur)

print(pikachu)
print(bulbasaur)
print(charmander)

print(Ash)

pikachu.lose_health(2)
pikachu.gain_health(5)
pikachu.gain_experience(5)

Ash.attack(Jhava)
Jhava.attack(Ash)

Ash.use_potion()
Jhava.use_potion()

Ash.switch_pokemon(0)
Jhava.switch_pokemon(1)
