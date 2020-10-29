def read_file():
    """
    This function opens and reads the file containg usernames and passwords.
    """
    # Create a file object called login_details, and give option to read file
    login_details = open("login_details.txt","r")
    # Create a list containing each line of login_details. List is called contents
    contents = login_details.readlines()
    login_details.close()
    return contents


def get_choice():
    """
    This function asks user if they are logging in or registering
    """
    choice = input("Would you like to login/register: ")
    return choice


def details_not_matching():
    """
    This function tells a user attempting to login
    that either the username or password,
    or both, were wrong.
    """
    print("login details don't match.")
   

def check_valid_option(choice):
    if (choice.lower().split(" ")[0] == "login"):
        return "login"
    if(choice.lower().split(" ")[0] == "register"):
        return "register"
    else:
        print("That is not a valid option.")
        return "invalid"
   
    
def check_registration_details(username, password):
    """
    This function checks if the username being entered 
    exists in the text file. While taken usernames are
    being entered, the user is prompted for a new one.
    Only details with  unique username are added to the text file.
    """
    contents = read_file()
    while ((username + '\n') in contents):
        print("Sorry! This username is taken..")
        username = get_username()
        password = get_password()
        
    add_details(username, password)


def login_username():
    username = input("Please enter your username: ")
    return username


def login_password():
    password = input("Please enter your password: ")
    return password


def get_username():
    username = input("Please enter a unique username: ")
    return username


def get_password():
    password = input("Please enter a unique password: ")
    return password


def add_details(username, password):
    """
    This function adds correct details to the text file
    """
    login_details = open("login_details.txt","a")
    login_details.write(username + "\n" + password + "\n")
    login_details.close()
    welcome_user(username)
    start()


def do_login():
    contents = read_file()
    username = login_username()
    password = login_password()
    #print(password)
    #print(username)
    if len(contents) == 0:
        print("Start an account and be our first member!")
        start()
   
    if((username + '\n') in contents):
        if(contents[contents.index(username + '\n')+1] == (password + '\n')):
            print("Welcome back " + username + "!")
            
        else:
            details_not_matching()
            start()
        
    else:
        details_not_matching()
        start()
        
    
       
    
        
        

                
      
def do_register():
    username = get_username()
    password = get_password()
    check_registration_details(username,password)


def welcome_user(username):
    print("Welcome " + username + "! You are successfully registered on StayMzansi.")


def start():
    """
    The main login and registration setup
    """
    choice = get_choice()
    choice = check_valid_option(choice)
       
    
    if choice == "login":
        contents = read_file()
        #print((contents))
        if len(contents) == 1:
            print("Start an account and be our first member!")
            start()
        else:
        #print("got here")
            do_login()
        
     
    if choice == "register":
        username = get_username()
        password = get_password()
        check_registration_details(username,password)

    elif(choice=="invalid"):
        start()


start()
