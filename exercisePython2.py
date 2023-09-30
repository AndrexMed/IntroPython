users = []
passwords = []

#-----------------------------------------------
def welcomeUser(user):
    print("\n*** Bienvenido", user ,"***\n")

#------------------------------------------------
def searchUser(user,password):
    foundedUser = False
    foundedPass = False
    for item in users:
        if item == user:
            foundedUser = True
    for item in passwords:
        if item == password:
            foundedPass = True

    if foundedPass == True and foundedUser == True:
        welcomeUser(user)       
    else:
        print("\n*** User Invalid ***\n")      

#-----------------------------------------------------------
def register():
    user = input("Enter username: ")
    users.append(user)
    password = input("Enter password")
    passwords.append(password)
    print("\n *** Registro exitoso ***\n")

def login():
    userToLogin = input("Enter username")
    passToLogin = input ("Enter password")
    searchUser(userToLogin,passToLogin)

# -------------------------------------------------------
flag = True
while flag:
    print("\n*** System of users ***\n")
    print("1. Register")
    print("2. Login")
    print("3. Exit\n")
    opcion = int(input("*** Seleccione una opcion: "))

    if opcion == 1:
        register()
    elif opcion == 2 :
        login()
    elif opcion == 3:
        print("*** Good Bye ***")
        flag = False

