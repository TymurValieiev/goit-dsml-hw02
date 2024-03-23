from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://tymurvalieiev:Mysecretpassword123@cluster0.f1i8c5r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client.ds2
collection = db['cats']

# Додавання кота
def add_cat(name, age, features):
    cat_data = {
        "name": name,
        "age": age,
        "features": features
    }
    collection.insert_one(cat_data)

# Вивести всі записи
def get_all_cats():
    return list(collection.find())

# Вивести інформацію про кота за ім'ям
def get_cat_by_name(name):
    return collection.find_one({"name": name})

# Оновити вік кота за ім'ям
def update_cat_age(name, new_age):
    collection.update_one({"name": name}, {"$set": {"age": new_age}})

# Додати нову характеристику кота за ім'ям
def add_feature_to_cat(name, feature):
    collection.update_one({"name": name}, {"$push": {"features": feature}})

# Видалити запис про кота за ім'ям
def delete_cat_by_name(name):
    collection.delete_one({"name": name})

# Видалити всі записи з колекції
def delete_all_cats():
    collection.delete_many({})

if __name__ == "__main__":

    #Додавання

    add_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])

    # Читання
    
    # print("Усі коти:")
    # print(get_all_cats())
    # print()

    # print("Інформація про кота за ім'ям:")
    # print(get_cat_by_name("barsik"))
    # print()

    # Оновлення

    # update_cat_age("barsik", 4)
    # print("Оновлений вік кота:")
    # print(get_cat_by_name("barsik"))
    # print()

    # add_feature_to_cat("barsik", "ловить мишей")
    # print("Оновлені характеристики кота:")
    # print(get_cat_by_name("barsik"))
    # print()

    # Видалення

    # delete_cat_by_name("barsik")
    # print("Кількість котів після видалення:")
    # print(len(get_all_cats()))
    # print()

    # delete_all_cats()
    # print("Кількість котів після видалення всіх записів:")
    # print(len(get_all_cats()))