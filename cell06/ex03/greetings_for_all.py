def greetings(name="noble stranger"):
    if type(name) == str:
        print(f"Hello, {name}.")
    else:
        print("Error! It not a name.")

def main():
    greetings('Alexandra')
    greetings('Wil')
    greetings()
    greetings(42)

main()