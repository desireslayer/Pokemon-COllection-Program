# Pokémon Collection Manager

# Initialize the Pokémon collection with the starter Pokémon

starter = input("You are starting a pokemon adventure-"
                "\n Choose your starter pokemon ! \n"
                "Bulbasaur🐸🌿🍃, 💧Squirtle🐢 or 🦎🔥Charmander ")

print(f"Your first pokemon is {starter}, Congractulations😃🌄")
Pokemons = [starter]
def add_Pokemon(*args):
    new_pokemon = input("Enter the pokemon! ")
    Pokemons.append(new_pokemon)
    print(f"Added {new_pokemon} to your collection! 🌟")
def release_Pokemon():
    while True:
        remov = input("Which Pokémon do you want to release? 🪶🕊️ ")
        if remov not in Pokemons:
            print(f"{remov} not in our collection. Try again!")
        else:
            print(f"{remov} is removed from our collection! ❌")
            break
    Pokemons.remove(remov)

def show_collection():
    print(Pokemons)



while True:
    print("Choose an option- \n"
          "1. Add Pokemons \n"
          "2. Release Pokemons \n"
          "3. Show Pokemons \n"
          "4. Exit ")
    ans = input("Enter 1,2,3,4")
    if ans == "1":
        add_Pokemon()
    elif ans == "2":
        release_Pokemon()
    elif ans == "3":
        show_collection()
    elif ans == "4":
        print("Thanks for playing🙏🛝🧸")
        break
    else:
        print(f"{ans} is Invalid response")

