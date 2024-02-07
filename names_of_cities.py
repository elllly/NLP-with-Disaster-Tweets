import geonamescache

def get_country_names():
    # Create an instance of the geonamescache GeonamesCache class
    gc = geonamescache.GeonamesCache()

    # Get a dictionary containing all countries and their information
    countries = gc.get_countries()

    # Extract country names from the dictionary
    country_names = [country_data['name'] for country_data in countries.values()]

    return country_names

def get_city_names():
    # Create an instance of the geonamescache GeonamesCache class
    gc = geonamescache.GeonamesCache()

    # Get a dictionary containing all cities and their information
    cities = gc.get_cities()

    # Extract city names from the dictionary
    city_names = [city_data['name'] for city_data in cities.values()]

    return city_names

def write_to_file(filename, data):
    # Open the file with the appropriate encoding (UTF-8)
    with open(filename, 'w', encoding='utf-8') as file:
        # Write data to the file
        for item in data:
            file.write(item + '\n')

# Specify the filenames where you want to write the country and city names
output_filename_countries = 'country_names.txt'
output_filename_cities = 'city_names.txt'

# Call the functions to get and write country and city names to the files
country_names = get_country_names()
city_names = get_city_names()

write_to_file(output_filename_countries, country_names)
write_to_file(output_filename_cities, city_names)

# Print a message indicating success
print(f'Country names have been written to {output_filename_countries}.')
print(f'City names have been written to {output_filename_cities}.')
