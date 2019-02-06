# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Maram"
my_age = 23
my_bio = "Hi me, I love you. LOL."
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    print ("Would you like to: ")
    print ("1) Create a new club. ")
    print ("2) Browse and join clubs. ")
    print ("3) View existing clubs. ")
    print ("4) Display members of a club. ")
    print ("-1) Close application. ")

    flag = False
    option = int(input ())
    while option != -1:
        if option == 1:
            create_club()
        elif option == 2:
            view_clubs() 
            join_clubs(myself)
        elif option == 3:
            view_clubs()
        elif option ==4:
            view_clubs()
            choice = input("Enter the name of the club whose members you'd like to see: ").lower()
            while True:
                for club in clubs:
                    if choice == club.name.lower():
                        view_club_members(club)
                        flag = True
                    if flag == True:
                        break
                if flag == True:
                    break
                if flag == False:
                    choice = input("Please enter a valid chioce: ").lower()
        else:
            option = input ("Invalid option, enter your option again: ")
            option = int(option)
        option = input("Enter your option or type -1 to exit.")
        option = int(option)
 

def create_club():
    new_club = input("Pick a name for your awesome new club: ")
    des_club = input("What is your club about? ")

    myclub = Club(new_club, des_club)

    myclub.recruit_member(myself)
    myclub.assign_president(myself)

    print ("Enter the number of people you would like to recruit to your new club (-1 to stop)")

    for index, r in enumerate(population):
        print ("[ %02d ] %s" % (index+1, r.name))

    id_number = int(input())
    length = len(population)
    while id_number != -1:
        if length >= id_number and id_number > 0:
            myclub.recruit_member(population[id_number - 1])
        else:
            print ("You heve entered a wrong number, type -1 if you finished.")
        id_number = int(input())

    print ("Here is your club: \n%s \n%s" % (myclub.name, myclub.description))
    view_club_members(myclub)
    clubs.append(myclub)   


def view_clubs():

    for club in clubs:
        print ("NAME: %s" % club.name)
        print ("DESCRIPTION: %s" % club.description)
        print ("MEMBERS: %s \n" % len(club.club_member))
    

def view_club_members(club_name):
    club_name.print_member_list()

def join_clubs(person):
    choice = input("Enter the name of the club that you'd like to join: ").lower()
    flag = False
    while True:
        for club in clubs:
            if choice == club.name.lower():
                club.recruit_member(person)
                print ("%s just joined %s" % (my_name, choice))
                flag = True
            if flag == True:
                break
        if flag == True:
            break
       
        if flag == False:
            choice = input("Please enter a valid chioce:").lower()
    

def application():
    introduction()
    options()
    
