try:
    file = open("module19/example.txt","r")

    content = file.read()

    print("Content : ",content)
except FileNotFoundError:
    print("Given file not exists")
except Exception:
    print("Unknown error , Please try again")