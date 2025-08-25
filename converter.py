def to_decimal(num_str, base):
    try:
        return int(num_str, base)
    except ValueError:
        print("❌ Invalid number for the given base!")
        return None

def from_decimal(num, base):
    if base == 2:
        return bin(num)[2:]
    elif base == 8:
        return oct(num)[2:]
    elif base == 10:
        return str(num)
    elif base == 16:
        return hex(num)[2:].upper()
    else:
        return None

def converter():
    while True:
        print("\n=== Universal Number Converter ===")
        print("1. Binary → Others")
        print("2. Octal → Others")
        print("3. Decimal → Others")
        print("4. Hexadecimal → Others")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "5":
            print("Goodbye 👋")
            break

        num_str = input("Enter the number: ")

        if choice == "1":
            dec = to_decimal(num_str, 2)
        elif choice == "2":
            dec = to_decimal(num_str, 8)
        elif choice == "3":
            dec = to_decimal(num_str, 10)
        elif choice == "4":
            dec = to_decimal(num_str, 16)
        else:
            print("❌ Invalid choice!")
            continue

        if dec is not None:
            print("\n✅ Conversions:")
            print("Binary      :", from_decimal(dec, 2))
            print("Octal       :", from_decimal(dec, 8))
            print("Decimal     :", from_decimal(dec, 10))
            print("Hexadecimal :", from_decimal(dec, 16))

converter()
