import json
import requests as r
import sys

##
# Static Api class that handles fetching data from 
# the Kiwi Locations Api
#
class Api:

  # Access url to the Api
  api_url = 'https://api.skypicker.com/locations?type=subentity&term=GB&locale=en-US&active_only=true&location_types=airport&limit=100&sort=name'

  ##
  # Get cities with airports from 
  # the Kiwi Locations Api
  #
  @staticmethod
  def get_cities():
    res = r.get(Api.api_url).content
    
    data = json.loads(res)
    
    cities = {}
    
    for airport in data['locations']:
      a_name = airport['name']
      a_city_name = airport['city']['name']

      if a_city_name not in cities.keys():
        cities[a_city_name] = [a_name]
      else:
        cities[a_city_name].append(a_name)

    cities = json.dumps(cities, indent=4, sort_keys=True)

    print(cities)

  ##
  # Get coordinations of airports in UK from 
  # the Kiwi Locations Api
  #
  @staticmethod
  def get_coords():
    res = r.get(Api.api_url).content
    
    data = json.loads(res)
    
    coords = {}
    
    for airport in data['locations']:
      a_name = airport['name']
      a_coords = [airport['location']['lat'], airport['location']['lon']]
      coords[a_name] = a_coords

    coords = json.dumps(coords, indent=4, sort_keys=True)
    print(coords)


  ##
  # Get IATA codes of airpors in UK from 
  # the Kiwi Locations Api
  #
  @staticmethod
  def get_iata():
    res = r.get(Api.api_url).content
    
    data = json.loads(res)
    
    iata = {}

    for airport in data['locations']:
      iata[airport['name']] = airport['id']

    iata = json.dumps(iata, indent=4, sort_keys=True)

    print(iata)
    pass


  ##
  # Get names of airports in UK from 
  # the Kiwi Locations Api
  #
  @staticmethod
  def get_names():
    res = r.get(Api.api_url).content
    
    data = json.loads(res)
    
    names = []
    
    for airport in data['locations']:
      a_name = airport['name']
      names.append(a_name)

    names = json.dumps(names, indent=4, sort_keys=True)

    print(names)


  ##
  # Get full info about airports in UK from 
  # the Kiwi Locations Api
  #
  @staticmethod
  def get_full():
    res = r.get(Api.api_url).content
    
    data = json.loads(res)
    
    full = {}

    for airport in data['locations']:
      full[airport['name']] = airport

    full = json.dumps(full, indent=4, sort_keys=True)

    print(full)


  ##
  # A special method to fetch combined data 
  # from the Kiwi Locations Api
  # (Based on the argumnents given in the executing command)
  #
  @staticmethod
  def get_mixed(args):
    options = {
      '--coords' : 'location',
      '--iata'   : 'id',
      '--names'  : 'name',
      '--cities' : 'city'
    }

    res = r.get(Api.api_url).content
    
    data = json.loads(res)
    
    mixed = {}

    for airport in data['locations']:
      a_name = airport['name']
      mixed[a_name] = {}
      for arg in args:
        if arg == '--cities': # Special case
          mixed[a_name][options[arg]] = airport[options[arg]]['name']
        else:
          mixed[a_name][options[arg]] = airport[options[arg]]


    mixed = json.dumps(mixed, indent=4, sort_keys=True)

    print(mixed)

