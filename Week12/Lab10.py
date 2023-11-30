# Lab 10
# Author: Nate Harris

# Lab 10 will show demonstrate how Dictionary's work in Python.

import pandas as pd
from tabulate import tabulate

# 1. Create a dictionary called my_dict with the following key value pairs:
# Key: "name", Value: "John"
# Key: "age", Value: 30
# Key: "city", Value: "Trenton"
# Key: "state", Value: "New Jersey"

my_dict = {"name": "John", "age": 30, "city": "Trenton", "state": "New Jersey"}

# 2. Print out the dictionary.
print(my_dict)


# 3. Print out the value for the key "name".
print(my_dict["name"])

# 4. Lookup the key associated with the value "New Jersey" and print it out.
# Hint 1: You will need to loop through the dictionary.
# Hint 2: remember you can use the .items() method to get the key and value.

for key, value in my_dict.items():
    if value == "New Jersey":
        print(key)

# 5. Add a new key value pair to the dictionary.
# Key: "country", Value: "USA"

my_dict["Country"] = "USA"

# 6. Print out the dictionary.

print(my_dict)

# 7. Remove the key value pair with the key "city".

my_dict.pop("city")

# 8. Print out the dictionary.

# 9. Create a dictionary called cities with an key as the City name and values as a list that contains the state, population, and country.
# use the following data:
# Trenton, New Jersey, 84,913, USA
# New York City, New York, 8,336,817, USA
# Los Angeles, California, 3,979,576, USA
# Chicago, Illinois, 2,693,976, USA
# Houston, Texas, 2,320,268, USA
# Phoenix, Arizona, 1,680,992, USA
# Philadelphia, Pennsylvania, 1,584,138, USA
# San Antonio, Texas, 1,547,253, USA
# San Diego, California, 1,423,851, USA

cities = {
    "Trenton": {"State": "New Jersey", "Population": 84913, "Country": "USA"},
    "New York City": {"State": "New York","Population": 8336817, "Country": "USA"},
    "Los Angeles": {"State": "California", "Population": 3979576, "Country": "USA"},
    "Chicago": {"State": "Illinois", "Population": 2693976, "Country": "USA"},
    "Houston": {"State":"Texas", "Population": 2320268, "Country": "USA"},
    "Phoenix": {"State":"Arizona", "Population": 1680992, "Country": "USA"},
    "Philadelphia": {"State": "Pennsylvania", "Population": 1584138, "Country": "USA"},
    "San Antonio": {"State": "Texas", "Population": 1547253, "Country": "USA"},
    "San Diego": {"State": "California", "Population": 1423851, "Country": "USA"},
}

# 10. Print a table of the data using the pandas library.
# pip install pandas. This was put at the top of the file.

df = pd.DataFrame(cities).T
print("\n", df)

# 11. Use the tabulate library to print out the table. pip install tabulate this was put at the top of the file.

col_row_table= tabulate(df, headers="keys", tablefmt="psql")
print("\n", col_row_table)

# 12. Print out the population for the city of Chicago.

# 11. Print out the population for the city of Chicago.


# 13. **Extra** An alternative to converting a dictionary into a pandas df then tabulate, you can use dictionary unpacking and tabulate.
# Dictionary unpacking is a new feature in Python 3.9 and allows you to unpack a dictionary into a list of dictionaries.
# You can then use tabulate to print out the table.

# In our case, {"City": city, **info} creates a new dictionary that includes a "City" key with the city name and all the key-value pairs from the info dictionary.

# For example, if city is "Chicago" and info is {"state": "Illinois", "Population": 2693976, "Country": "USA"}, the new dictionary will be {"City": "Chicago", "state": "Illinois", "Population": 2693976, "Country": "USA"}. This is the same as {"City": city, **info}.
# The ** operator unpacks the info dictionary into the new dictionary

# Transform the data

new_cities = [{"City": city, **info} for city, info in cities.items()]

# Print the table using tabulate

print("\n", tabulate(new_cities, headers="keys", tablefmt="psql"))

# 12. How many cities have a population greater than 1 million? Use a for loop to iterate through the dictionary.

# 15.  How many cities are in the USA? Use .items() to get a list of tuples. Use a for loop to iterate through the list of tuples.
# Hint 1: You will need to use the second item in the tuple. The second item is a dictionary. IE. for city, info in cities.items():

count_cities = 0
for city, info in cities.items():
    if info["Country"] == "USA":
        count_cities += 1  
print("\n"f"Cities in the USA: {count_cities}")