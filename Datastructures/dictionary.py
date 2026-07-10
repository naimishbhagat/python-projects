#dictionary is collection of key value pairs
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict["name"])

people1 = {"John":32,"Rob":40,"Tim":20}
print(people1["Tim"])
people1["Rob"] = 45
print(people1)

people_id = {1:"Ford", 2:"Walton", 3: "Parker"}
print(people_id[2])

people = dict(
    john=32,
    rob=45,
    tim=20
)
people['mike']=30
del people["tim"]
print(people)

print(people['john'])
#dictionary functions
print(people.get("rob"))

prices={'iphone':500,'ipad':400}
a = prices.pop('ipad')
new_prices={'iphone':600,'imac':1500}
prices.update(new_prices)
print(prices)

print(prices.keys())
print(prices.values())
print(prices.items())