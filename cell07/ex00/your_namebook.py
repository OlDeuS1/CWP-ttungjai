def array_of_names(persons):
    
    return [f"{key.capitalize()} {value.capitalize()}" for key, value in persons.items()]


def main():

    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }

    print(array_of_names(persons))

main()
