# Exercise 2: File Handling

filename = "notes.txt"

try:
    message = input("Enter a short note/message: ")

    with open(filename, "w") as file:
        file.write(message + "\n")

    print("\nSaved successfully!")

    print("\nReading file...")
    with open(filename, "r") as file:
        print(file.read())

    new_message = input("\nEnter another note: ")

    with open(filename, "a") as file:
        file.write(new_message + "\n")

    print("\nAppended successfully!")

    print("\nUpdated content:")
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found!")