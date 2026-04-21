'''
Workout Generator
'''
import random


chest=["Barbell Bench Press", "Dumbbell Bench Press", "Weighted Push-ups"]
back=["Low-to-High Row", "Cable Lat Pulldown", "Bent Over Barbell Row"]
shoulders=["Overhead Presses", "Lateral Raises", "Rear Delt Flies"]
arms=["Bicep Curls", "Tricep Dips", "Shoulder Press", "Hammer Curls"]
upperl=[chest,back,shoulders,arms]

quads=["Squats", "Lunges", "Leg Presses", "Leg Extensions"]
hamstrings=["Romanian Deadlifts", "Hamstring Curls"]
glutes=["Hip Thrusts", "Bulgarian Split Squats", "Cable Kickbacks"]
calves=["Standing Calf Raises", "Seated Calf Raises"]
lowerl=[quads,hamstrings,glutes,calves]

totall=[upperl,lowerl]

corel=["Planks", "Dead Bugs", "Bird Dogs", "Russian Twists", "Leg Raises", "Glute Bridges", "Bicycle Crunches", "Cherry Pickers"]


workopts=["Light Cardio", "Upper Body", "Lower Body", "Full Body", "Cardio Intervals", "Light Cardio+Core", "Upper Body+Core", "Lower Body+Core", "Full Body+Core", "Cardio Intervals+Core"]
weekdays=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
workweek={
#dledk

}


dw=[]
workouts={




}

def main():
    done = False
    while not done:
        actch=input("""Welcome to Workout Generator!
    In Workout Generator, you can:
C: Create a daily workout
D: Display your saved daily workouts
P: Create a weekly workout plan based on what days you want to work out                         
Q: Quit
Which would you like to do?                                        
                      """).strip().upper()
        if actch=='C':
            wtype=input("""
    What muscle group are you targeting?
U: Upper
L: Lower
T: Total Body
C: Core                   
                    """).strip().upper()
            create(wtype)
        elif actch == 'D':
            display()
        elif actch == 'P':
            plan()
        elif actch == 'Q':
            break

def create(wtype):
    if wtype == 'U':
            reps=input("Would you like to do a strength workout (S) or an endurance workout (E)?").strip().upper()
            num=int(input("How many exercises would you like to do? (Typically 4-8)"))
            work = upper(reps,num)
    elif wtype == 'L':
            reps=input("Would you like to do a strength workout (S) or an endurance workout (E)?").strip().upper()
            num=int(input("How many exercises would you like to do? (Typically 4-8)"))
            work = lower(reps,num)
    elif wtype == 'T':
            reps=input("Would you like to do a strength workout (S) or an endurance workout (E)?").strip().upper()
            num=int(input("How many exercises would you like to do? (Typically 4-8)"))
            work = total(reps,num)
    elif wtype == 'C':
            time=int(input("How long do you want your core workout to be? (Typically 5, 10, or 15): "))
            reps=int(input("How many exercises would you like to do? Typically 4-8.)"))
            work = core(time, reps)
    else:
            print("Invalid input. Please try again.")
    save= input ("Would you like to save your workout? (Y/N)").upper().strip()
    if save == 'Y':
            name= input("What would you like to name this workout?")
            workouts [name]=work
    else:
            print()
            
def display():
   
    for i, j in workouts.items():
        print("Displaying Workouts:")
        print(f"{i}:")
        for k in j:
            print(f"{k}")
        print()
def plan():
    for i in weekdays:
        ans= input(f"do you want to work out on {i}? (Y/N)").strip().upper()
        if ans == "Y":
                workweek[i]=random.choice(workopts)
        else:
                workweek[i]='Rest'
    print()
    print("Displaying Weekly Plan:")
    for i, j in workweek.items():
        print(f"{i}: {j}")
    print()

def core(time, reps):
    work=[]
    num=int(time/reps*2)
    for i in range (reps):
        work.append(random.choice(corel))
    work.append(f"Repeat all exercises for 30 seconds {num} time(s)")
    if num>1:
        work.append("Rest for 30 seconds between each round")
    else:
        print("No rest needed.") 
    print ("Here is your core workout:")
    for i in work:
        print(i)
    return work

def upper(reps, num):
    work=[]
    for i in range (num) :
        #AI
        choice=(random.choice(random.choice(lowerl)))
        while choice in work:
            work.append(choice)
    if reps=='E':
         work.append("Repeat each exercise 8-12 times per round")
    elif reps=='S':
         work.append("Repeat each exercise 4-8 times per round")
    else:
         work.append("Repeat each exercise 4-12 times")
    print ("Here is your upper body workout:")
    for i in work:
        print(i)
    return work

def lower(reps,num):
    work=[]
    #AI
    while len(work) < num:
        choice = random.choice(random.choice(lowerl))
        if choice not in work:
            work.append(choice)
    if reps=='E':
         work.append("Repeat each exercise 8-12 times per round")
    elif reps=='S':
         work.append("Repeat each exercise 4-8 times per round")
    else:
         work.append("Repeat each exercise 4-12 times")
    print ("Here is your lower body workout:")
    for i in work:
        print(i)
    return work

def total (reps,num):
    work=[]
    for i in range (num) :
        #AI
        choice=(random.choice(random.choice(random.choice(totall))))
        while choice in work:
            work.append(choice)
    if reps=='E':
         work.append("Repeat each exercise 8-12 times per round")
    elif reps=='S':
         work.append("Repeat each exercise 4-8 times per round")
    else:
         work.append("Repeat each exercise 4-12 times")
    print ("Here is your total body workout:")
    for i in work:
        print(i)
    return work      
main()


def upper():
        work = [random.choice(chest), random.choice(back), random.choice(shoulders), random.choice(arms)]
        print ("Here is your upper body workout:")
        for i in work:
            print(i)
        '''
        if wreps == 'S':
            print("Custom Workout:")
            for i in work:
                print(i, "4-8 Reps")
            print("Repeat 3X")
        elif wreps == 'E':
            for i in work:
                print(i, "8-12+ Reps")
            print("Repeat 3X")
'''
