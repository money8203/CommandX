import os
import webbrowser
import subprocess

app_paths = {
    "Discord": r"C:\Path\to\discord.link",
    "Slack": r"C:\Path\to\slack.link",
    "spotify": r"C:\Path\to\whatsapp.exe",
    "whatsapp": r"C:\Path\to\whatsapp.exe",
    "myfile": r"C:\Path\to\myfile.txt",
    "myfolder": r"C:\Path\to\myfolder",
    "twitter": "https://www.twitter.com/",
    "youtube": "https://www.youtube.com/",
    "chrome": "https://www.google.com/",
    "code": "https://code.visualstudio.com/",
    "facebook": "https://www.facebook.com/",
    "instagram": "https://www.instagram.com/",
    "linkedin": "https://www.linkedin.com/",
    "github": "https://www.github.com/",
    "netflix": "https://www.netflix.com/",
    "primevideo": "https://www.primevideo.com/",
}

current_directory = os.getcwd()
command_prompt = "Ask Money"

chat_history = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def open_folder(path):
    try:
        os.startfile(path)
    except OSError:
        print("Failed to open the folder.")

while True:
    command = input(f"{command_prompt} ~ ")
    chat_history.append(command)  # Store the command in chat history
    
    parts = command.lower().split()

    if not parts:
        continue

    cmd = parts[0]
    args = parts[1:]

    if cmd == "exit":
        print("Have a good day :)")
        break

    elif cmd in ["hey", "hello", "hi"]:
        print("Hi there!")

    elif cmd == "home":
        current_directory = os.getcwd()
        command_prompt = "Ask Money"    

    elif cmd == "how" and "are" in args and "you" in args:
        print("I'm good, how about you?")

    elif cmd in ["good", "fine", "great"]:
        print("Awesome, how can I help you?")    

    elif cmd == "open":
        if len(args) == 0:
            open_folder(current_directory)
        elif len(args) == 1:
            file_or_app = args[0]
            if file_or_app in app_paths:
                app_path = app_paths[file_or_app]
                if app_path.endswith(".lnk"):
                    subprocess.Popen([app_path], shell=True)
                elif app_path.startswith("https"):
                    webbrowser.open(app_path)
                else:
                    os.startfile(app_path)
            else:
                print("File or application not found.")
        else:
            print("Please provide a single file, application name, or use 'open' to open the current directory.")
        

    elif cmd == "cd":
        if len(args) == 0:
            print("Please provide a directory name.")
        else:
            directory = " ".join(args)
            if directory == "..":
                current_directory = os.path.dirname(current_directory)
                command_prompt = os.path.basename(current_directory) if current_directory else "Ask Money"
            else:
                new_directory = os.path.join(current_directory, directory)
                if os.path.isdir(new_directory):
                    current_directory = new_directory
                    command_prompt = os.path.basename(current_directory)
                else:
                    print("Directory not found.")

    elif cmd == "list":
        files = os.listdir(current_directory)
        for file in files:
            print(file)

    elif cmd == "back":
        current_directory = os.path.dirname(current_directory)
        command_prompt = os.path.basename(current_directory) if current_directory else "Ask Money"

    elif cmd == "search":
        if len(args) >= 1:
            query = " ".join(args)
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
        else:
            print("Please provide a search query.")
    
    elif cmd == "where":
        print(f"You are currently in: {current_directory}")
    
    elif cmd == "calculate":
        print("Enter your calculations. Type 'done' to exit the calculation portal.")
        while True:
            calculation = input("$ ")
            if calculation == "done":
                print("Tathastu")
                break
            try:
                result = eval(calculation)
                print(f"Result for {calculation} = {result}")
            except (SyntaxError, NameError):
                print("Invalid calculation.")  

    elif cmd == "clear":
        clear_screen()
        chat_history = []  # Clear the chat history

    elif cmd == "chat" and "history" in args:
        for i, chat in enumerate(chat_history, start=1):
            print(f"{i}. {chat}")                 
            
    else:
        print("Hey there, how can I help you ?")
