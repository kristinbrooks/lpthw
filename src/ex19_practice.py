def catLove(num_cats, type):
    print(f"I love {num_cats} {type} cats! They're wonderful!\n")


catLove(13, "short haired")

catLove(3 + 37, "fluffy")

tons_of_cats = 51351879
catLove(tons_of_cats, "stripey grey")

catLove(tons_of_cats - 57234, "mouse chasing")

catLove(3, "naughty")

catLove(tons_of_cats + tons_of_cats, "polydactyl")

print("What type of cat is my favorite?")
favorite_cat = input(">")
catLove(29, favorite_cat)

catLove(tons_of_cats - 53463636 + 3456, "trilling")

print("How many cats do you love?")
loved_cats = input(">")
catLove(loved_cats, "sneaky")

print("I love a secret number of cats more than you. You tell me how many you love and then I'll"
      " tell you how many I love so you can figure it out!\n")
print("How many do you love?")
less_cats_than_me = int(input(">"))
catLove(less_cats_than_me + 1, "adorable")
