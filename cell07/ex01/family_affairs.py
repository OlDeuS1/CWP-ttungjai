def find_the_redheads(family):
    
    return [key for key, value in family.items() if value == "red"]

def main():

    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }

    print(find_the_redheads(dupont_family))

main()
