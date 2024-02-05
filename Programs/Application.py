application = '''Respected Ma'am,
    I have an urgent piece of work
    at home.So, I cannot come to
    college. Kindly grant me leave
    for one day.
    
    Name: <Name>
    Class: <Class>
    Date: <Date>'''
    
name = input("Enter your name: ")
class_ = input ("Enter your class: ")
date = input ("Enter current date: ")

application = application.replace("<Name>", name)
application = application.replace("<Class>", class_)
application = application.replace("<Date>", date)

print(application)