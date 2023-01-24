


while True:
    country = input("Enter a Country : ")

    match country:
        case 'USA':
            print("Hello")
        case 'India':
            print("Namaste")
        case 'Germany':
            print("Hallo")

        case 'exit':
            break

print("Done!")
