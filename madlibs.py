# # string concatenation
# # suppose we want to create a string that says "subscrive to ____"
# youtuber = "Lina"

# # a few ways to do this
# # print("subscribe to " + youtuber)
# # print("subscribe to {}".format(youtuber))
# # print(f"subscribee to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"computer programming is so {adj}! It makes me so exited all the time vecause \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)
