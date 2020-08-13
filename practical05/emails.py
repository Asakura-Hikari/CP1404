email_dir = {}
email = input("Email: ")

while email != '':
    full_name = email.split("@")
    full_name[0] = full_name[0].split(".")
    link = " "
    full_name[0] = link.join(full_name[0])

    check_name = input("Is your name {}?(Y/N)".format(full_name[0])).upper()
    if check_name == 'N':
        real_name = input("Name: ")
        email_dir[real_name] = email
    elif check_name == 'Y':
        email_dir[full_name[0]] = email
    else:
        print("Invalid input, please try again")

    email = input("Email: ")

print()
for name in email_dir:
    print("{}({})".format(name, email_dir[name]))
