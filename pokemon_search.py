import requests

# requests the name of a pokemon to search
pokemon_name = input('What Pokemon do you want to find: ')

# defines the URL endpoint to connect with for pokemon 
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'

# get the data from the endpoint through a get request
response = requests.get(url)

#checks to see if the reponse comes back successful or not
if response.status_code == 200:
    # returned successful then extract the data into a json file named pokedata
    poke_data = response.json()
    
    # extact necessary data and pass to usable variables 
    name = poke_data['name']
    poke_type = [type['type']['name'] for type in poke_data['types']]
    poke_abilities = [ability['ability']['name'] for ability in poke_data['abilities']]
    
    # print reults to screen
    print(f'Name: {name}')
    print(f'Pokemon type: {poke_type}')
    print(f'Pokemon abilities: {", ".join(poke_abilities)}')
else:
    #print error message from site
    if response.status_code == 404:
        print(f"The Pokémon '{pokemon_name}' was not found.")
    else:    
        print('Error: ', response.json()['details'])