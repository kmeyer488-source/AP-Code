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


workouts={




}

def main():
    done = False
    while not done:
        actch=input("""
                    
    Welcome to Workout Generator!
    In Workout Generator, you can:
C: Create a daily workout
D: Display your saved daily workouts                       
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
        elif actch == 'Q':
            break

def create(wtype):
    if wtype == 'U':
            reps=input("Would you like to do a strength workout (S) or an endurance workout (E)?").strip().upper()
            num=int(input("How many exercises would you like to do? (Typically 4-8)"))
            #start AI
            work = upper(reps,num)
            #end AI
    elif wtype == 'L':
            reps=input("Would you like to do a strength workout (S) or an endurance workout (E)?").strip().upper()
            num=int(input("How many exercises would you like to do? (Typically 4-8)"))
            #start AI
            work = lower(reps,num)
            #end AI
    elif wtype == 'T':
            reps=input("Would you like to do a strength workout (S) or an endurance workout (E)?").strip().upper()
            num=int(input("How many exercises would you like to do? (Typically 4-8)"))
            #start AI
            work = total(reps,num)
            #end AI
    elif wtype == 'C':
            time=int(input("How long do you want your core workout to be? (Typically 5, 10, or 15): "))
            reps=int(input("How many exercises would you like to do? Typically 4-8.)"))
            #start AI
            work = core(time, reps)
            #end AI
    else:
            print("Invalid input. Please try again.")
    save= input ("Would you like to save your workout? (Y/N)").upper().strip()
    if save == 'Y':
            name= input("What would you like to name this workout?")
            workouts [name]=work
    else:
            print("Workout not saved.")
            
def display():
    print("Displaying Workouts:")
    print()
   #start AI
    for i, j in workouts.items():
        print(f"{i}:")
        for k in j:
            print(f"{k}")
        print()
    #end AI
def core(time, reps):
    work=[]
    num=int(time/reps*2)
    for i in range (reps):
        work.append(random.choice(corel))
    #start AI
    work.append(f"Repeat all exercises for 30 seconds {num} time(s)")
    #end AI
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
    #start AI
    while len(work)<num:
        choice=(random.choice(random.choice(upperl)))
        while choice not in work:
            work.append(choice)
    #end AI
    if  reps=='E':
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
    #start AI
    while len(work) < num:
        choice = random.choice(random.choice(lowerl))
        if choice not in work:
            work.append(choice)
    #end AI
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
    #start AI
    while len(work)<num:
        choice=(random.choice(random.choice(random.choice(totall))))
        while choice not in work:
            work.append(choice)
    #end AI
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
