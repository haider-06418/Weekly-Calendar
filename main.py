from datetime import date

# defining function
def change_todo_list():
    #setting up dictionary with the days of the week
    todo_list = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": [], "saturday": [], "sunday": []}
    #taking number of entries
    n= int(input("How many entries do you want: "))
    print()
    #running loop(taking day,time and event)
    for count in range(n):
        Day = input("Please enter the day? ")
        Day = Day.lower()
        #validation of day
        while (Day not in ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]):
            print("Invalid entry - please enter a correct day of the week (like Monday or monday).")
            Day = input("Please enter the day? ")
            Day = Day.lower()
        if Day == "monday" or Day == "tuesday" or Day == "wednesday" or Day == "thursday" or Day == "friday" or Day == "saturday" or Day == "sunday":
            event = input("What would you like to add to " + Day + "'s to-do list ? ")
            time = int(input("What time would you like to do " + event+"(24-hour clock): " ))
            #validation of time
            while time<0 or time>=24 or type(time)!=int:
                print("Invalid entry - please enter a valid time in 24 hour clock.")
                time = int(input("What time would you like to do " + event))
            # format of output
            time=str(time)+str(":00")
            evnt=event+" at "+str(time)

            todo_list[Day].append(evnt)
            print()


    print("YOUR PERSONAL TO DO LIST IS READY")
    today = date.today()
    print("Today's date:", today)

    print()
    #vertical printing of the dictionary
    for day, event in todo_list.items():
        print(day, ":", event)


#calling the function
change_todo_list()
print()
print("ENJOY YOUR WEEK")
