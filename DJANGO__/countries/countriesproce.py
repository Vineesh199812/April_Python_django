from json import *

with open("countries.json","r",encoding="utf-8") as f:
    data=(load(f))
print(data[0])

#country=[country["name"] for country in data if country["alpha3code"]=="TKM"]
#print(country)

#print capital of china
country_detail=[country.get("capital") for country in data if country["name"]=="China"]
print(country_detail)

#print population of china
population=[country.get("population") for country in data if country["name"]=="China"]
print(population)

#currency of ukrain
ukraine_currency_data=[country["currencies"] for country in data if country["name"].lower()=="ukraine"]
country_currency=[country.get("currencies") for country in data if country["name"]=="Ukraine"]
print(country_currency)
print(ukraine_currency_data.pop().pop().get("name"))

#languages of india
#borders of ukraine
#print highest populated country

india_languages=[country["languages"] for country in data if country["name"].lower()=="india"].pop()
print(india_languages)

language_name=[lan["name"] for lan in india_languages]
print(language_name)
#OR  ==> all in a single for loop
language=[lan["name"]for country in data for lan in country["languages"] if country["name"].lower()=="india"]
print(language)

borders_ukraine=[country["borders"] for country in data if country["name"].lower().startswith("ukraine")][0] #to avoid the list in o/p
#print(borders_ukraine)
borders=[country["name"] for country in data if country["alpha3Code"] in borders_ukraine]
print(borders)

population=max(data,key=lambda country:country["population"])
print(population.get("name"))
print(population.get("population"))

#print countries whose languages is english

english_countries=[country["name"] for country in data for lan in country["languages"] if lan["name"].lower()=="english"]
print(english_countries)