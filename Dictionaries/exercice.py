# Create a program to manage data of club partners allowing
# get info of the partners in a dictionarie to access by partner number.
# the data will be: number, name, last_name  insription date cuote up to day
# the program sart with the data of preload partners

from pickle import FALSE


def load_partners(partners):
    """
    load_partners
    """
    num=int(input("Partner number (0 to stop): "))
    while num!=0:
        name=input("Full name: ")
        date=input("Ingress Date (DDMMAAAA): ")
        payment=input("Payments up to day? y/n: ")
        partners[num]=[name,date,payment.lower()=="y"]
        num=int(input("Partner number (0 to stop1): "))
    return partners

def modify_date(partner, last_date, new_date):
    """
        modidy date
    """
    for data in partner.values():
        if data[1]==last_date:
            data[1]=new_date
    return partner

def partner_number(partner, name):
    """
        partner_number
    """
    for number,data in partner.items():
        if data[0].lower()==name.lower():
            return number
    return 0

def format_date(date):
    """
    format date
    """
    return date[:2]+"/"+date[2:4]+"/"+date[4:]

def print_list(partners):
    """
    print list
    """
    for number,data in partners.items():
        print("-Number:",number)
        print("-Name:",data[0])
        print("-Igress date:", format_date(data[1]))
        if data[2]:
            print("-Up to date")
        else:
            print("-not up tpo date")

active_users = {
    1:["Amanda Nuñez",  "15032020", False],
    3:["Lautaro Campos", "15062022", True]
}
print("1 Add user")
print("2 Number of users")
print("3 Register payment")
print("4 Modify ingress date")
print("5 Delete Partner")
print("0 End")
opc = int(input("Select an option "))
while opc != 0:
    if opc == 1:
        print("***Add user")
        active_users=load_partners(active_users)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        input("Press any key to continue: ")
    if opc == 2:
        print("The club has", len(active_users), "partners")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        input("Press any key to continue: ")

    if opc == 3:
        print("***Register payment")
        num=int(input("partner number: "))
        active_users[num][2]=True
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        input("Press any key to continue: ")

    if opc == 4:
        print("***Modify ingress date")
        active_users=modify_date(active_users, "13032018", "14032018")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        input("Press any key to continue: ")

    if opc == 5:
        print("***Delete Partner")
        name = input("Full Name: ")
        num = partner_number(active_users, name)
        if num in active_users:
            del active_users[num]
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        input("Press any key to continue: ")

    print_list(active_users)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1 Add user")
    print("2 Number of users")
    print("3 Register payment")
    print("4 Modify ingress date")
    print("5 Delete Partner")
    print("0 End")
    opc = int(input("Select an option "))
