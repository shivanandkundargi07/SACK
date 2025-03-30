import json
import os
order1= [87, 0, 52, 58, 44, 91, 68, 97, 51, 15,
19, 65, 23, 94, 89, 78, 76, 45, 69, 12,
73, 75, 53, 61, 14, 48, 56, 93, 8, 13,
66, 59, 95, 96, 28, 92, 46, 98, 22, 54,
85, 20, 34, 27, 38, 86, 40, 4, 29, 26,
71, 49, 72, 33, 88, 31, 36, 17, 99, 41,
80, 67, 64, 5, 35, 90, 21, 70, 9, 2,
62,7, 16, 6, 60, 3, 81, 32, 74, 25,
30, 79, 83, 57, 18, 55, 50, 77, 84, 10,
1, 43, 39, 63, 37, 24, 42, 47, 11, 82]

order2 = [87, 0, 52, 58, 44, 91, 68, 97, 51, 15,
 66, 2, 22, 14, 53, 28, 39, 35, 60, 48,
 95, 9, 88, 82, 71, 65, 24, 67, 32, 84,
74, 1, 77, 59, 19, 31, 75, 6, 94, 37,
 18, 45, 73, 61, 13, 98, 99, 46, 81, 17,
78, 34, 62, 20, 36, 42, 92, 93, 76, 72,
 21, 26, 49, 23, 47, 70, 83, 33, 40, 38,
86, 57, 30, 7, 63, 50, 8, 55, 69, 89,
 64, 10, 11, 12, 96, 79, 29, 3, 41, 85,
   43, 16, 80, 5, 25, 56, 27, 90, 4, 54]

order3 = [87, 0, 52, 58, 44, 91, 68, 97, 51, 15,
            48, 10, 90, 17, 54, 92, 31, 73, 40, 71,
            29, 76, 60, 37, 14, 11, 77, 1, 53, 81,
            98, 63, 70, 59, 2, 45, 33, 85, 88, 22,
            9, 95, 86, 16, 41, 8, 43, 47, 74, 93,
            64, 50, 75, 62, 3, 89, 56, 34, 39, 84,
            20, 78, 7, 12, 57, 42, 21, 55, 35, 65,
            32, 72, 66, 6, 99, 94, 25, 18, 27, 46,
            61, 36, 23, 79, 69, 49, 96, 28, 83, 19,
            67, 26, 38, 80, 13, 30, 24, 82, 4, 5]
exp3 = [87,  0, 52, 58, 44, 91, 68, 97, 51, 15,
                        94, 92, 10, 72, 49, 78, 61, 14,  8, 86,
                        84, 96, 18, 24, 32, 45, 88, 11,  4, 67,
                        69, 66, 77, 47, 79, 93, 29, 50, 57, 83,
                        17, 81, 41, 12, 37, 59, 25, 20, 80, 73,
                        1, 28,  6, 46, 62, 82, 53,  9, 31, 75,
                         38, 63, 33, 74, 27, 22, 36,  3, 16, 21,
                         60, 19, 70, 90, 89, 43,  5, 42, 65, 76,
                         40, 30, 23, 85,  2, 95, 56, 48, 71, 64,
                         98, 13, 99,  7, 34, 55, 54, 26, 35, 39]
Imagenet_r_classes = [
    "goldfish", "great white shark", "hammerhead", "stingray", "hen", "ostrich", "goldfinch", "junco",
    "bald eagle", "vulture", "newt", "axolotl", "tree frog", "iguana", "African chameleon", "cobra",
    "scorpion", "tarantula", "centipede", "peacock", "lorikeet", "hummingbird", "toucan", "duck",
    "goose", "black swan", "koala", "jellyfish", "snail", "lobster", "hermit crab", "flamingo",
    "american egret", "pelican", "king penguin", "grey whale", "killer whale", "sea lion",
    "chihuahua", "shih tzu", "afghan hound", "basset hound", "beagle", "bloodhound",
    "italian greyhound", "whippet", "weimaraner", "yorkshire terrier", "boston terrier",
    "scottish terrier", "west highland white terrier", "golden retriever", "labrador retriever",
    "cocker spaniels", "collie", "border collie", "rottweiler", "german shepherd dog", "boxer",
    "french bulldog", "saint bernard", "husky", "dalmatian", "pug", "pomeranian", "chow chow",
    "pembroke welsh corgi", "toy poodle", "standard poodle", "timber wolf", "hyena", "red fox",
    "tabby cat", "leopard", "snow leopard", "lion", "tiger", "cheetah", "polar bear", "meerkat",
    "ladybug", "fly", "bee", "ant", "grasshopper", "cockroach", "mantis", "dragonfly",
    "monarch butterfly", "starfish", "wood_rabbit", "porcupine", "fox squirrel", "beaver",
    "guinea pig", "zebra", "pig", "hippopotamus", "bison", "gazelle", "llama", "skunk", "badger",
    "orangutan", "gorilla", "chimpanzee", "gibbon", "baboon", "panda", "eel", "clown fish",
    "puffer fish", "accordion", "ambulance", "assault rifle", "backpack", "barn", "wheelbarrow",
    "basketball", "bathtub", "lighthouse", "beer glass", "binoculars", "birdhouse", "bow tie",
    "broom", "bucket", "cauldron", "candle", "cannon", "canoe", "carousel", "castle",
    "mobile phone", "cowboy hat", "electric guitar", "fire engine", "flute", "gasmask",
    "grand piano", "guillotine", "hammer", "harmonica", "harp", "hatchet", "jeep", "joystick",
    "lab coat", "lawn mower", "lipstick", "mailbox", "missile", "mitten", "parachute",
    "pickup truck", "pirate ship", "revolver", "rugby_ball", "sandal", "saxophone", "school_bus",
    "schooner", "shield", "soccer ball", "space shuttle", "spider web", "steam locomotive", "scarf",
    "submarine", "tank", "tennis ball", "tractor", "trombone", "vase", "violin", "military aircraft",
    "wine bottle", "ice cream", "bagel", "pretzel", "cheeseburger", "hotdog", "cabbage", "broccoli",
    "cucumber", "bell pepper", "mushroom", "Granny_Smith", "strawberry", "lemon", "pineapple",
    "banana", "pomegranate", "pizza", "burrito", "espresso", "volcano", "baseball player",
    "scuba diver", "acorn"
]


def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")


def get_values_from_json(json_file, indexes):
    # Open and read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Get the keys of the dictionary
    keys = list(data.keys())

    # Retrieve values based on the list of indexes
    selected_values = [data[keys[i]] for i in indexes if i < len(keys)]
    # selected_values = [data[i] for i in indexes]

    return selected_values

# Example usage
json_file = '/home/shivank2/gokhale_user/shivanand/mammoth/concept_sets/gpt3_init_dict/imagenet_core_concepts.json'  # Replace with your actual JSON file path
# indexes = [87,  0, 52, 58, 44, 91, 68, 97, 51, 15]  # List of indexes you want to retrieve values from

n_exp = 20
cifar10 = list(range(10))
cifar100=list(range(100))
cub200=list(range(200))
Imagenet_r=list(range(200))
for i in range(len(Imagenet_r)//n_exp):
    curr_lst=[]
    curr_lst.append(Imagenet_r[0:(i+1)*n_exp])
    print("Current list:", curr_lst)
    selected_values = get_values_from_json(json_file, curr_lst[0])
    # print("Selected values:", selected_values)
    file_path = f"/home/shivank2/gokhale_user/shivanand/mammoth/concept_sets/OG_order_Imagenet_R_concepts/new_exp{i+1}_filtered_new.txt"
    folder_path=file_path.split("/")[0:-1]
    folder_path="/".join(folder_path)
    # print("File path:", "/".join(file_path))
    # ensure_folder_exists("/".join(file_path))   
    ensure_folder_exists(folder_path)
    with open(file_path, "a") as file:
        for sublist in selected_values:
            for element in sublist:
                file.write(f"{element}\n")









# print(f"All elements have been appended to {file_path}.")

# selected_values = get_values_from_json(json_file, exp3)
# print("Selected values:", selected_values)

# # List of lists
# list_of_lists = selected_values

# # Filepath to the .txt file
# file_path = "/home/shivank2/gokhale_user/shivanand/icarl-pytorch/data/concept_sets/order1_cifar100_concepts/new_exp10_filtered_new.txt"

# # Append each element of all lists to the file
# with open(file_path, "a") as file:
#     for sublist in list_of_lists:
#         for element in sublist:
#             file.write(f"{element}\n")

# print(f"All elements have been appended to {file_path}.")



# goldfish,
# great_white_shark,
# hammerhead,
# stingray,
# hen,
# ostrich,
# goldfinch,
# junco,
# bald_eagle,
# vulture,
# newt,
# axolotl,
# tree_frog,
# iguana,
# African_chameleon,
# cobra,
# scorpion,
# tarantula,
# centipede,
# peacock,
# lorikeet,
# hummingbird,
# toucan,
# duck,
# goose,
# black_swan,
# koala,
# jellyfish,
# snail,
# lobster,
# hermit_crab,
# flamingo,
# american_egret,
# pelican,
# king_penguin,
# grey_whale,
# killer_whale,
# sea_lion,
# chihuahua,
# shih_tzu,
# afghan_hound,
# basset_hound,
# beagle,
# bloodhound,
# italian_greyhound,
# whippet,
# weimaraner,
# yorkshire_terrier,
# boston_terrier,
# scottish_terrier,
# west_highland_white_terrier,
# golden_retriever,
# labrador_retriever,
# cocker_spaniels,
# collie,
# border_collie,
# rottweiler,
# german_shepherd_dog,
# boxer,
# french_bulldog,
# saint_bernard,
# husky,
# dalmatian,
# pug,
# pomeranian,
# chow_chow,
# pembroke_welsh_corgi,
# toy_poodle,
# standard_poodle,
# timber_wolf,
# hyena,
# red_fox,
# tabby_cat,
# leopard,
# snow_leopard,
# lion,
# tiger,
# cheetah,
# polar_bear,
# meerkat,
# ladybug,
# fly,
# bee,
# ant,
# grasshopper,
# cockroach,
# mantis,
# dragonfly,
# monarch_butterfly,
# starfish,
# wood_rabbit,
# porcupine,
# fox_squirrel,
# beaver,
# guinea_pig,
# zebra,
# pig,
# hippopotamus,
# bison,
# gazelle,
# llama,
# skunk,
# badger,
# orangutan,
# gorilla,
# chimpanzee,
# gibbon,
# baboon,
# panda,
# eel,
# clown_fish,
# puffer_fish,
# accordion,
# ambulance,
# assault_rifle,
# backpack,
# barn,
# wheelbarrow,
# basketball,
# bathtub,
# lighthouse,
# beer_glass,
# binoculars,
# birdhouse,
# bow_tie,
# broom,
# bucket,
# cauldron,
# candle,
# cannon,
# canoe,
# carousel,
# castle,
# mobile_phone,
# cowboy_hat,
# electric_guitar,
# fire_engine,
# flute,
# gasmask,
# grand_piano,
# guillotine,
# hammer,
# harmonica,
# harp,
# hatchet,
# jeep,
# joystick,
# lab_coat,
# lawn_mower,
# lipstick,
# mailbox,
# missile,
# mitten,
# parachute,
# pickup_truck,
# pirate_ship,
# revolver,
# rugby_ball,
# sandal,
# saxophone,
# school_bus,
# schooner,
# shield,
# soccer_ball,
# space_shuttle,
# spider_web,
# steam_locomotive,
# scarf,
# submarine,
# tank,
# tennis_ball,
# tractor,
# trombone,
# vase,
# violin,
# military_aircraft,
# wine_bottle,
# ice_cream,
# bagel,
# pretzel,
# cheeseburger,
# hotdog,
# cabbage,
# broccoli,
# cucumber,
# bell_pepper,
# mushroom,
# Granny_Smith,
# strawberry,
# lemon,
# pineapple,
# banana,
# pomegranate,
# pizza,
# burrito,
# espresso,
# volcano,
# baseball_player,
# scuba_diver,
# acorn