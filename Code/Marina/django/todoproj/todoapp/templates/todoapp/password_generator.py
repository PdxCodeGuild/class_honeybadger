def password():
    password_dict = {
        "lowercase" : list(string.ascii_lowercase),
        "uppercase" : list(string.ascii_uppercase),
        "number" : list(string.digits),
        "special" : list(string.punctuation),
        }

    password = ""

    for key in password_dict:
        length = input(f"How many {key} characters would you like your password to have?\n")
        length = int(length)
        password += password_part(length, password_dict[key])
        print(f"Test: {password}")

    password = list(password)
    print(password)
    random.shuffle(password)
    print(password)
    password = "".join(password)
    print(password)

    # return print(password)

password()
