#Open the file
def restaurant_dictionary(file_name):
    my_file = open(file_name)
#Getting rid of white space and separating values
    restaurants = {}
    for line in my_file:
        line = line.rstrip()
        words = line.split(':')
#Define key and value
        name = words[0]
        rating = words[1]
#Make dictionary
        restaurants[name] = rating
    return restaurants

def restaurant_keys(restaurants): 
#Make a separate list of keys
    restaurant_keys = list(restaurants.keys())
#Sorting list
    restaurant_keys.sort()
    return restaurant_keys

#Calling back for key and value in list, then print
def print_restaurant_ratings(restaurant_keys, restaurants):
    for key in restaurant_keys:
        print "Restaurant: %s  Rating: %s" % (key, restaurants[key])
#Sort lines alphabetically and print

def main():
#Assigning outcome of restaurant_dictionary (the dictionary itself) to restaurants
    restaurants = restaurant_dictionary("scores.txt")
#Calling on sorted list from line 20
    sorted_restaurant_keys = restaurant_keys(restaurants)
    print_restaurant_ratings(sorted_restaurant_keys, restaurants)

if __name__ == "__main__":
    main()
#Your job is to write a program named 'sorted_data.py' reads the file, 
#then spits out the ratings in alphabetical order by restaurant
