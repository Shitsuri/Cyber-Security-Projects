# Password Strength Checker
# By: YourNameHere
# A simple tool to check if your password sucks or not

# I heard imports go at the top? Not sure why but everyone does this
import re  # no idea what this does but stackoverflow said I need it
import time  # for the fake "scanning" effect
from pyfiglet import Figlet  # makes fancy text
from termcolor import colored  # colors!! because black and white is boring

# ============================================
# This function guesses how long to crack password
# I copied the math from some blog post lol
# ============================================
def estimate_crack_time(password):
    # First count how long the password is
    length = len(password)
    
    # Check if password has different stuff in it
    has_lower = re.search(r'[a-z]', password)  # like 'a'
    has_upper = re.search(r'[A-Z]', password)  # like 'A'
    has_num = re.search(r'[0-9]', password)  # like '4'
    has_special = re.search(r'[^a-zA-Z0-9]', password)  # like '@' (magic regex)
    
    # Super technical password strength algorithm (trust me)
    if length < 8:
        return "Instant (Weak af)"
    elif length >= 12 and (has_lower and has_upper and has_num and has_special):
        return "Like a million years (Good job!)"
    elif length >= 10 and (has_lower and has_upper and has_num):
        return "Few years (Not bad)"
    else:
        return "Few days (My grandma could crack this)"

# ============================================
# Checks password and gives tips
# (I wrote this at 2AM while eating ramen)
# ============================================
def check_strength(password):
    feedback = []  # this will store all the messages
    length = len(password)
    
    # Rule 1: Longer passwords are better I think?
    if length < 8:
        feedback.append(colored("❌ Too short (hackers love short passwords)", "red"))
    else:
        feedback.append(colored(f"✅ Length: {length} chars (decent)", "green"))
    
    # Checking for different character types
    checks = {
        "Lowercase letters": re.search(r'[a-z]', password),
        "Uppercase letters": re.search(r'[A-Z]', password),
        "Numbers": re.search(r'[0-9]', password),
        "Special chars": re.search(r'[^a-zA-Z0-9]', password)  # black magic
    }
    
    # Add check results to feedback
    for name, check in checks.items():
        if check:
            feedback.append(colored(f"✅ Has {name}", "green"))
        else:
            feedback.append(colored(f"❌ Missing {name}", "yellow"))
    
    return feedback

# ============================================
# Main thing that runs when you start the program
# ============================================
def main():
    # Fancy title because why not
    f = Figlet(font='slant')
    print(colored(f.renderText('PASSWORD CHECKER 9000'), 'cyan'))
    print(colored("(Now with 100% more security!)", "yellow"))
    print("\n" + "="*50)
    print("Warning: This isn't real security advice")
    print("I just learned Python last month")
    print("="*50 + "\n")
    
    # Keep running until user quits
    while True:
        password = input("\nTest a password (or type 'quit'): ").strip()
        
        # Exit if user types quit
        if password.lower() == 'quit':
            print("\n" + "="*50)
            print(colored("Thanks for using my janky program!", "magenta"))
            print("Follow me on GitHub @YourUsernameHere")
            print("="*50 + "\n")
            break
        
        # Fake "scanning" effect to look professional
        print("\n" + "-"*40)
        print(colored("\n🔍 Analyzing password...", "blue"))
        time.sleep(1.5)  # pause to look like it's doing something hard
        print(colored("🤖 Asking my hacker friends...", "blue"))
        time.sleep(0.5)
        print(colored("📊 Calculating...", "blue"))
        time.sleep(0.3)
        
        # Get the results
        feedback = check_strength(password)
        crack_time = estimate_crack_time(password)
        
        # Show results
        print("\nRESULTS:")
        print("\n".join(feedback))
        print(colored(f"\n⏳ Time to crack: {crack_time}", "magenta"))
        print("-"*40 + "\n")

# This makes the program run (I think?)
if __name__ == "__main__":
    main()