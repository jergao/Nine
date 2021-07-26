#!/usr/bin/env python
import pickle
import datetime
import random


def duplicateID(ID):
    for key in notes:
        if ID == key:
            return True
    return False


def randomID(length=11):
    ID = ""
    while duplicateID(ID):
        ID = ""
        for i in range(length):
            ID = ID + str(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"))
    return ID


class Note:
    def __init__(self, information):
        self.content = information  # instance variable unique to each instance
        self.time = datetime.datetime.now()
        self.ID = randomID()


try:
    pickle_in = open("notes.pickle", "rb")
    notes = pickle.load(pickle_in)
except (FileNotFoundError, EOFError) as e:
    print("No previous save found.")
    notes = {}


def printnote(noteid, verbose=1):
    if verbose == 0:
        print(notes[noteid].content)
    if verbose == 1:
        print(str(notes[noteid].time.strftime("%c")) + "  |" + notes[noteid].content + "\n")
    if verbose == 2:
        print(notes[noteid].content + "  |" + str(notes[noteid].time.strftime("%c")) + " @" + str(notes[noteid].ID))


for ID in notes:
    printnote(ID)

x = ""
while x != "QUIT":
    x = str(input(str(datetime.datetime.now().strftime("%c")) + "  |"))
    if x == "QUIT":
        break
    current = Note(x)
    notes[current.ID] = current
    pickle.dump(notes, open("notes.pickle", "wb"))

print(notes)
