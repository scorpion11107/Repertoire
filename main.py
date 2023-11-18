def load(path):
    import json

    try:
        f = open(path, "r")
    except:
        print("No file at path:", path)
        exit()
    
    try:
        data = json.loads(f.read())
    except:
        print("Wrong format for file at path:", path)
        f.close()
        exit()
    
    f.close()

    return data


def save(database, path):
    import json

    try:
        data = json.dumps(database)
    except:
        print("Wrong format in database")
        exit()
    
    try:
        open(path)
    except:
        print("No file at path:", path)
        exit()
    
    f = open(path, "w")
    f.write(data)
    f.close()


def search(database, name):
    try:
        return "Number: " + database[name]
    except:
        return "Contact not found"


def add(database, contact):
    if search(database, contact[0]) != "Contact not found":
        print("Contact already existing")
        return
    database[contact[0]] = contact[1]
    print("Contact added\n")


def remove(database, name):
    try:
        database.pop(name)
        print("Contact deleted\n")
    except:
        print("Contact not in database")


def main():
    path = "repertoire.txt"
    database = load(path)

    entry = -1

    while entry != "0":
        if entry == "1":
            name = input("Name:\n- ")
            print(search(database, name))
            entry = -1
            continue

        if entry == "2":
            name = input("Name (0 to quit):\n- ")
            if name == "0":
                entry = -1
                continue
            number = input("Number:\n- ")
            contact = [name, number]
            add(database, contact)
            save(database, path)
            continue

        if entry == "3":
            name = input("Name:\n- ")
            remove(database, name)
            save(database, path)
            entry = -1
            continue

        if entry not in [-1, "0", "1", "2", "3"]:
            print("Please enter a valid option.")

        print("0: quit | 1: search | 2: add | 3: remove")
        entry = input("- ")


main()