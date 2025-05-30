import random

def get_random_caption():
    captions = [
        "When you finally fix one bug and another appears",
        "Me: I'll just fix this one thing... 3 hours later",
        "It works on my machine",
        "I have no idea what I'm doing",
        "That feeling when your code runs perfectly first try"
    ]
    return random.choice(captions)