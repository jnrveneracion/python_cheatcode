# Printing
def una():
    print("Hello guys")
    print('Hi guys!')
    print(21)
    print(14.01)


# Input + Variables + Printing
def pangalawa():
    name = "Janrie"
    surname = "Veneracion"
    age = 20
    location = "Caloocan City"

    print(f"hi, I'm {name} {surname}. I'm {age} years old and I'm from {location}.")
    input1 = str(input("What about you, What's your name?..."))
    print(f"Hello {input1}, hope you're doing well.")

# ---------- loop ----------
want = ""
while want.upper != "Q":
    print("\nChoose a [NUM] to run: ")
    print("[1] Printing")
    print("[2] Variables + Printing")

    respond = int(input("\n>>>> "))

    if respond == 1:
        una()

    elif respond == 2:
        pangalawa()

    want = str(input("Press any key to continue... Press Q to not: "))
    if want.upper == "Q":
        print("ok thanks")
        break
