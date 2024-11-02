"""
write a script that will ask user for to enter yes or no as answer 
If the user answer is not either yes or no the script should keep asking for a valid entry.
and if the entry is yes or no, then it should display valid entry
"""

user_answer=""
while True:
    if user_answer not in ['yes', 'no']:
        user_answer=input("Do you want covid shot? please enter (yes or no): ").strip().lower()
    else:
        print("valid choice")
        break