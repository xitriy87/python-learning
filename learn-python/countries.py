import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
countries_file = os.path.join(dir_path, 'countries.json')

with open(countries_file, 'r') as file_json:
	countries = json.load(file_json)


def get_sea(countries):
	for country in countries.values():
		if country['sea'] == 'True':
			print(country['name'])

def get_population(countries, population):
	for country in countries.values():
		if country['population'] >= int(population):
			print(country['name'])

def get_location(countries, location):
	for country in countries.values():
		Location_is_i = country['Location']
		if Location_is_i.lower() == location.lower():
			print('Country {0} is in {1}'.format(country['name'],country['Location']))

def add_country(name = '', sea = 'False', population = 0, Location = '' ):
	countries[name] = {'name': name, 'sea': sea, 'population': population, 'Location': Location }

def write_counties():
	with open(countries_file, 'w') as json_file:
		json.dump(countries, json_file)

while True:
	print("""
	S - Show all countries have sea

	P - Enter population, and show countries have population more than entered count

	L - Enter locaton, show countries lacation eq entered location

	A - Add new country

	W - write changes

	E - Exit
	
	""")

	choice = input('Enter your choice: ')

	if choice.lower() == 's':
		get_sea(countries)
		input("Enter any bottom! ")
	elif choice.lower() == 'p':
		population = input('Enter count of population: ')
		get_population(countries, population)
		input("Enter any bottom! ")
	elif choice.lower() == 'l':
		location = input('Enter location: ')
		get_location(countries, location)
		input("Enter any bottom! ")
	elif choice.lower() == 'a':
		name = input('Enter country name: ')
		sea = input("Enter sea, (True, False): ")
		population = input('Enter population: ')
		location = input('Enter country location: ')
		add_country(name,sea,population,location)
		input("Enter any bottom! ")
	elif choice.lower() == 'w':
		write_counties()
		input('Enter any bottom! ')
	elif choice.lower() == 'e':
		break
	else:
		print('You entered wrong value - {0}'.format(choice))

