spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # spicy_foods is a dictionary with a LIST of items that should be iterated through
    spicy_list = [item["name"] for item in spicy_foods]
    return spicy_list

def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest

result=get_spiciest_foods(spicy_foods)
print(result)
    


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print('{} ({}) | Heat Level: {}' .format(food["name"] , food["cuisine"], food["heat_level"] * "🌶"))
        # return food_items
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
print(get_spicy_food_by_cuisine(spicy_foods, "cuisine"))


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
           print('{} ({}) | Heat Level: {}' .format(food["name"] , food["cuisine"], food["heat_level"] * "🌶"))
result=print_spiciest_foods(spicy_foods)
print(result)

def get_average_heat_level(spicy_foods):
    sum_heatlevel= sum(food["heat_level"] for food in spicy_foods)
    avg_heatlevel = sum_heatlevel/len(spicy_foods)
    return avg_heatlevel
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods




