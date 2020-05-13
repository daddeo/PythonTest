# https://towardsdatascience.com/python-power-tip-enumerated-types-9a1e606250a4

import sys
from enum import Enum, unique, IntEnum


@unique
class Suit(Enum):
    Club = 1
    Diamond = 2
    Heart = 3
    Spade = 4


s = Suit.Spade
# enum: Suit.Spade [name: Spade, value: 4]
print(f"enum: {s} [name: {s.name}, value: {s.value}]")

print(f"s == Suit.Spade --> {s == Suit.Spade}")
print(f"s == Suit.Heart --> {s == Suit.Heart}")
print(f"s != Suit.Heart --> {s != Suit.Heart}")

# .name and .value are read-only (immutable)
try:
    s.value = 7
except AttributeError as ex:
    # print(str(ex))
    print(f"s.value = 7 --> [ex: {ex}]")
    # print(ex.args)
    # print(ex.__cause__)
    # print(ex.__context__)
    # print(ex.__traceback__)
except:
    e = sys.exc_info()[0]
    print(e)

try:
    s.name = "Joker"
except Exception as ex:
    print(f's.name = "Joker" --> [ex: {ex}]')

try:
    Suit.Heart.value = 9
except Exception as ex:
    print(f"Suit.Heart.value = 9 --> [ex: {ex}]")


def react(suit):
    if suit == Suit.Club:
        print("Please do not beat me with that.")
    elif suit == Suit.Diamond:
        print("Now we are rich.")
    elif suit == Suit.Heart:
        print("I love you too.")
    elif suit == Suit.Spade:
        print("Thank you for the handy garden tool.")
    else:
        raise ValueError("Unknown card suit")


react(Suit.Diamond)
react(Suit.Heart)

color = {
    Suit.Heart: "red",
    Suit.Diamond: "red",
    Suit.Spade: "black",
    Suit.Club: "black",
}
print(f"color of club: {color[Suit.Club]}")

text = "Heart"
print(f"{text} --> {Suit[text]}")
print(f"3rd suit --> {Suit(3)}")

print("suits:")
for x in Suit:
    print(x)

l = list(Suit)
print(l)


@unique
class Animal(Enum):
    Dog = 1
    Cat = 2
    Llama = 3
    Octopus = 4


print(f"is a club a dog? --> {Suit.Club == Animal.Dog}")
print(f"is club == 1? --> {Suit.Club == 1}")
print(f"is club == 'one'? --> {Suit.Club == 'one'}")


class ImageFormat(IntEnum):
    PNG = 1
    JPEG = 2
    GIF = 3


print(f"ImageFormat.JPEG --> {ImageFormat.JPEG}")
print(f"ImageFormat.JPEG == 2 --> {ImageFormat.JPEG == 2}")
print(f"ImageFormat.JPEG + 1 --> {ImageFormat.JPEG + 1}")

try:
    Suit.Club + 1
except Exception as ex:
    print(f"Suit.Club + 1 --> [ex: {ex}]")

print(f"list(ImageFormat) --> {list(ImageFormat)}")
print(f"ImageFormat(3) --> {ImageFormat(3)}")
print(f"ImageFormat['PNG'] --> {ImageFormat['PNG']}")
