import random
import requests
import time

my_score = 0
opponent_score = 0

print('Welcome to Pokémon Top Trumps!')


def choose_pokemon():
    pokemon_names = []
    while len(pokemon_names) < 5:
        pokemon_number = random.randint(1, 151)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
        response = requests.get(url)
        if response.status_code == 200:
            pokemon = response.json()
            pokemon_name = pokemon['name']
            if pokemon_name not in pokemon_names:
                pokemon_names.append(pokemon_name)

    print("Choose your Pokémon from the following list:")
    time.sleep(1)
    for i, name in enumerate(pokemon_names, start=1):
        print("{}. {}".format(i, name.capitalize()))
        time.sleep(1)

    while True:
        chosen_name = input("Enter the name of the Pokémon you want to choose: ").lower()
        if chosen_name in pokemon_names:
            url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(chosen_name)
            response = requests.get(url)
            pokemon = response.json()
            chosen_pokemon = {
                'name': pokemon['name'],
                'id': pokemon['id'],
                'height': pokemon['height'],
                'weight': pokemon['weight'],
                'hp': pokemon['stats'][0]['base_stat'],
                'attack': pokemon['stats'][1]['base_stat'],
                'defense': pokemon['stats'][2]['base_stat'],
                'special-attack': pokemon['stats'][3]['base_stat'],
                'special-defense': pokemon['stats'][4]['base_stat'],
                'speed': pokemon['stats'][5]['base_stat'],
            }
            return chosen_pokemon
        else:
            print("Invalid Pokémon name. Please try again.")


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'hp': pokemon['stats'][0]['base_stat'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defense': pokemon['stats'][2]['base_stat'],
        'special-attack': pokemon['stats'][3]['base_stat'],
        'special-defense': pokemon['stats'][4]['base_stat'],
        'speed': pokemon['stats'][5]['base_stat'],
    }


def run():
    my_pokemon = choose_pokemon()

    global my_score   # global is to allow the function to be modified from anywhere within the code
    global opponent_score

    print('\nYour Pokémon is {};'.format(my_pokemon['name'].capitalize()))  # returns API result with a capital letter at the start
    print('\nID = {}'.format(my_pokemon['id']), end=', ')  # end=' ' keeps everything on the same line but separated with a space
    print('Height = {}'.format(my_pokemon['height']), end=', ')  # otherwise everything is on separate lines
    print('Weight = {}'.format(my_pokemon['weight']), end=', ')
    print('HP = {}'.format(my_pokemon['hp']), end=', ')
    print('Attack = {}'.format(my_pokemon['attack']), end=', ')
    print('Defense = {}'.format(my_pokemon['defense']), end=', ')
    print('Special-Attack = {}'.format(my_pokemon['special-attack']), end=', ')
    print('Special-Defense = {}'.format(my_pokemon['special-defense']), end=', ')
    print('Speed = {}'.format(my_pokemon['speed']))

    choice = input('\nWould you like your opponent to choose your battle stat? Yes or No: ').lower()

    if choice == 'yes':
        stats = ["id", "height", "weight", "hp", "attack", "defense", "special-attack", "special-defense", "speed"]
        stat_choice = random.choice(stats)
        print('\nYour opponent has chosen a stat for your battle! This stat is:', stat_choice)

    if choice == 'no':
        stat_choice = input(
            '\nWhich stat do you want to use? (ID, height, weight, HP, attack, defense, special-attack, special-defense, speed): ').lower()
    # .lower to ensure that input is lower case or won't get result

    opponent_pokemon = random_pokemon()
    print('\nThe opponent chose {}'.format(opponent_pokemon['name'].capitalize()))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        print('Their stat is {}'.format(opponent_stat))
        print('\nYou win!')
        my_score += 1
        return my_score
    elif my_stat < opponent_stat:
        print('Their stat is {}'.format(opponent_stat))
        print('\nYou lose!')
        opponent_score += 1
        return opponent_score
    else:
        print('Their stat is {}'.format(opponent_stat))
        print('\nIt is a draw!')


def replay():
    play_again = input('\nWould you like to play again? Yes or No: ').lower()
    if play_again == 'yes':
        play_game()
    elif play_again == 'no':
        print('\nThanks for playing!')


def play_game():
    run()
    print('\nThe score is {} : {}'.format(my_score, opponent_score))
    replay()


play_game()
