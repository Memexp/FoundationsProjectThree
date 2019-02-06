# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.president = None
        self.club_member = []


    def assign_president(self, person):
        
        self.president = person        


    def recruit_member(self, person):
        self.club_member.append(person)


    def print_member_list(self):
        print ("Mmbers: " )
        total = 0
        for i in self.club_member:
            text = "- " + i.name + " " + str(i.age) + "years old" + (", President)" if i==self.president else ")")
            print (text)

            total += i.age
        average = total / len(self.club_member)
        print ("Average age in this club: %dyr" % average)

            



