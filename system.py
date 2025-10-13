# python exercise generator
# has 3 levels easy to hard
import random
import time

easy = [
    {
        "EASY": "> Even or Odd Checker",
        "instruction": "➤ Ask the user for a number and print if it's even or odd"
    },
    {
        "EASY2": "> Sum of Numbers",
        "instruction": "➤ Let the user enter 5 numbers, then print their total"
    },
    {
        "EASY3": "> Name Repeater",
        "instruction": "➤ Ask for your name and print it 5 times using a for loop"
    },
    {
        "EASY4": "> Simple Calculator",
        "instruction": "➤ Perform +, -, ×, ÷ operations based on user input"
    },
    {
        "EASY5": "> Multiplication Table",
        "instruction": "➤ Show the multiplication table of any number"
    },
    {
        "EASY6": "> Temperature Converter",
        "instruction": "➤ Convert Celsius to Fahrenheit and vice versa"
    },
    {
        "EASY7": "> Largest Number Finder",
        "instruction": "➤ Ask the user for three numbers and print the largest"
    },
    {
        "EASY8": "> Vowel Counter",
        "instruction": "➤ Count how many vowels are in a user-entered word or sentence"
    }   
]
medium = [
    {
        "MEDIUM": "> Palindrome Checker",
        "instruction": "➤ Check if a word or phrase reads the same backward"
    },
    {
        "MEDIUM": "> Grade Calculator",
        "instruction": "➤ Ask for 5 subjects’ grades and calculate average + remarks (pass/fail)"
    },
    {
       "MEDIUM": "> Guess the Number Game",
        "instruction": "➤ Generate a random number and let the user guess until correct" 
    },
    {
        "MEDIUM": "> Word Frequency Counter",
        "instruction": "➤ Generate a random number and let the user guess until correct" 
    },
    {
        "MEDIUM": "> To-Do List App (Console)",
        "instruction": "➤ Let the user add, view, and remove tasks from a list" 
    },
    {
        "MEDIUM": "> Fibonacci Sequence Generator",
        "instruction": "➤ Print the first n numbers of the Fibonacci sequence"
    },
    {
        "MEDIUM": "> Anagram Checker",
        "instruction": "➤ Check if two words are anagrams of each other"
    },
    {
        "MEDIUM": "> Simple Login System",
        "instruction": "➤ Create a small system that asks for username and password, and checks if they match stored data"
    }
]
print("""
===============PYTHON EXERCISE GENERATOR============
""")
print("""
1. Easy level
2. Medium level
3. Hard level
4. Exit
""")
while True:
    options = input("Enter which level you want: ")
    if options == 4:
        break
    random.shuffle(easy)
    match options:
        case "1":
            flag = False
            while not flag:
                for i in easy:
                    for key in i:
                        if key.startswith("EASY"):
                            title = i[key]


                            print(f"Easy level: \n{title}")
                    while True:
                        wow = input("Press enter to see the instruction: ")
                        if wow != "":
                            print("Please press enter to see the instruction")
                        else:
                            print(i["instruction"])
                        wow1 = input(f"\nDo you want to continue on easy level? (y/n): ").lower()
                        if wow1 == "n":
                            flag = True
                            print("Exiting easy level\n")
                            time.sleep(1)
                            break
                        elif wow1 == "y":
                            break
                    if flag:
                        break
                                                
        case "2":
            flag = False
            while not flag:
                for i in medium:
                    for key in i:
                        if key.startswith("MEDIUM"):
                            title = i[key]


                            print(f"Medium level: \n{title}")
                    while True:
                        wow = input("Press enter to see the instruction: ")
                        if wow != "":
                            print("Please press enter to see the instruction")
                        else:
                            print(i["instruction"])
                        wow1 = input(f"\nDo you want to continue on easy level? (y/n): ").lower()
                        if wow1 == "n":
                            flag = True
                            print("Exiting easy level\n")
                            time.sleep(1)
                            break
                        elif wow1 == "y":
                            break
                    if flag:
                        break
# Not yet done
            
                    
            
                
    


    

   
    

