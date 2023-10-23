import requests

# Replace 'india' with the name of the country for which you want to retrieve information
country_name = input("Enter a country: ")

# Make a GET request to the REST Countries API
response = requests.get(f"https://restcountries.com/v2/name/{country_name}")

if response.status_code == 200:
    data = response.json()
    country_data = data
    # Access and print data
    for country in country_data:
        print("Name:", country["name"])
        print("Top-Level Domain:", country["topLevelDomain"][0])
        print("Alpha-2 Code:", country["alpha2Code"])
        print("Alpha-3 Code:", country["alpha3Code"])
        print("Calling Codes:", ", ".join(country["callingCodes"]))
        print("Capital:", country["capital"])
        print("Subregion:", country["subregion"])
        print("Region:", country["region"])
        print("Population:", country["population"])
        print("Demonym:", country["demonym"])
        print("Area:", country["area"])
        print("Gini:", country["gini"])
        print("Timezones:", ", ".join(country["timezones"]))
        # print("Borders:", ", ".join(country["borders"]))
        print("Native Name:", country["nativeName"])
        print("Numeric Code:", country["numericCode"])
        
        # Access and print flags
        print("SVG Flag:", country["flags"]["svg"])
        print("PNG Flag:", country["flags"]["png"])
        
        # Access and print currencies
        for currency in country["currencies"]:
            print("Currency Code:", currency["code"])
            print("Currency Name:", currency["name"])
            print("Currency Symbol:", currency["symbol"])
        
        # Access and print languages
        for language in country["languages"]:
            print("Language ISO 639-1:", language["iso639_1"])
            print("Language ISO 639-2:", language["iso639_2"])
            print("Language Name:", language["name"])
            print("Native Name:", language["nativeName"])
        
        # Access and print translations
        for key, value in country["translations"].items():
            print(f"Translation ({key}):", value)
        
        # Access and print regional blocs
        for bloc in country["regionalBlocs"]:
            print("Regional Bloc Acronym:", bloc["acronym"])
            print("Regional Bloc Name:", bloc["name"])
        
        print("CIOC:", country["cioc"])
        print("Independent:", country["independent"])
        print("-" * 40)  # Separator for each country
    
else:
    print(f"Failed to retrieve data for {country_name}")
