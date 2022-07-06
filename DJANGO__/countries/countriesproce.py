from json import *

with open("countries.json",encoding="utf-8") as f:
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

india_languages=[country["languages"] for country in data if country["name"].lower()=="india"]
print(india_languages)

