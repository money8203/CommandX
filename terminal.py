import os
import shutil
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

command_help = {
    "hey": "Greets the user",
    "hello": "Greets the user",
    "hi": "Greets the user",
    "home": "Navigates to the home directory",
    "how are you": "Inquires about the assistant's well-being",
    "good": "Acknowledges a positive response",
    "fine": "Acknowledges a positive response",
    "great": "Acknowledges a positive response",
    "open": "Opens a file or application",
    "cd": "Navigates to a specific directory",
    "goto": "Navigates to a specific directory",
    "ls": "Lists files and directories in the current directory",
    "list": "Lists files and directories in the current directory",
    "back": "Navigates to the parent directory",
    "search": "Performs a Google search",
    "where": "Displays the current directory",
    "calculate": "Performs calculations",
    "clear": "Clears the screen and command history",
    "cls": "Clears the screen and command history",
    "chat history": "Displays the chat history",
    "exit": "Exits the program"
}

current_directory = os.getcwd()
command_prompt = "CommandX"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def open_folder(path):
    try:
        os.startfile(path)
    except OSError:
        print("Failed to open the folder.")

def navigate_to_directory(directory):
    global current_directory, command_prompt
    new_directory = os.path.abspath(os.path.join(current_directory, directory))
    if os.path.isdir(new_directory):
        current_directory = new_directory
        command_prompt = os.path.basename(current_directory) if current_directory else "CommandX"
    else:
        print("Directory not found.")
        
def display_help():
    print("Available commands:")
    for cmd, description in command_help.items():
        print(f"- {cmd}: {description}")

def create_item(item_name, item_type):
    item_path = os.path.join(current_directory, item_name)
    try:
        if item_type == "folder":
            os.mkdir(item_path)
            print("Folder created successfully.")
        elif item_type == "file":
            open(item_path, 'a').close()
            print("File created successfully.")
        else:
            print("Invalid item type.")
    except FileExistsError:
        if item_type == "folder":
            print("Folder already exists.")
        elif item_type == "file":
            print("File already exists.")
    except OSError:
        if item_type == "folder":
            print("Failed to create the folder.")
        elif item_type == "file":
            print("Failed to create the file.")

def delete_item(item_name, item_type):
    item_path = os.path.join(current_directory, item_name)
    if os.path.exists(item_path):
        try:
            if item_type == "folder":
                shutil.rmtree(item_path)
            elif item_type == "file":
                os.remove(item_path)
            print("Item deleted successfully.")
        except OSError:
            print("Failed to delete the item.")
    else:
        print("Item not found.")

def rename_item(old_name, new_name, item_type):
    old_path = os.path.join(current_directory, old_name)
    new_path = os.path.join(current_directory, new_name)
    if os.path.exists(old_path):
        try:
            if item_type == "folder":
                shutil.move(old_path, new_path)
            elif item_type == "file":
                os.rename(old_path, new_path)
            print("Item renamed successfully.")
        except OSError:
            print("Failed to rename the item.")
    else:
        print("Item not found.")

def copy_item(item_name, item_type):
    source_path = os.path.join(current_directory, item_name)
    if os.path.exists(source_path):
        destination_folder = input("Enter the destination folder: ")
        destination_path = os.path.join(current_directory, destination_folder, item_name)
        try:
            if item_type == "folder":
                shutil.copytree(source_path, destination_path)
            elif item_type == "file":
                shutil.copy(source_path, destination_path)
            print("Item copied successfully.")
        except OSError:
            print("Failed to copy the item.")
    else:
        print("Item not found.")

def paste_item(item_name, item_type):
    source_path = os.path.join(current_directory, item_name)
    if os.path.exists(source_path):
        destination_folder = current_directory
        destination_path = os.path.join(destination_folder, item_name)
        try:
            if item_type == "folder":
                shutil.copytree(source_path, destination_path)
            elif item_type == "file":
                shutil.copy(source_path, destination_path)
            print("Item pasted successfully.")
        except OSError:
            print("Failed to paste the item.")
    else:
        print("Item not found.")                                                

# Set the path for the command history file
command_history_file = "command_history.txt"

# Function to read command history from the file
def read_command_history():
    if os.path.exists(command_history_file):
        with open(command_history_file, "r") as file:
            return file.read().splitlines()
    else:
        return []

# Function to append a command to the command history file
def append_command_to_history(command):
    history = read_command_history()
    if command not in history:
        with open(command_history_file, "a") as file:
            file.write(command + "\n")

# Read the command history from the file when the terminal is activated
chat_history = read_command_history()


while True:
    command = input(f"{command_prompt} ~ ")

    append_command_to_history(command)  # Append the command to the history file

    if command in chat_history:
       chat_history.remove(command)  # Remove duplicate command from chat history

    chat_history.append(command)  # Store the command in chat history
    
    parts = command.lower().split()

    if not parts:
        continue

    cmd = parts[0]
    args = parts[1:]

    if cmd == "exit":
        print("Thanks for trying CommandX. Hope you like it, have a great day :)")
        with open(command_history_file, "w") as file:
            file.write("")  # Clear the command history file
            break

    elif cmd in ["hey", "hello", "hi"]:
        print("Hi there!")

    elif cmd in ["help", "?"]:
        display_help()

    elif cmd == "home":
        current_directory = os.getcwd()
        command_prompt = "CommandX"    

    elif cmd == "how" and "are" in args and "you" in args:
        print("I'm good, how about you?")

    elif cmd in ["good", "fine", "great"]:
        print("Awesome, how can I help you?")    

    elif cmd in ["launch", "start", "open"]:
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
                # Check if it's a directory
                folder_path = os.path.join(current_directory, file_or_app)
                if os.path.isdir(folder_path):
                    open_folder(folder_path)
                else:
                    print("File, application, or folder not found.")
        else:
            print("Please provide a single file, application name, or use 'open' to open the current directory.")
        continue  # Skip the default response for the "open" command

    elif cmd in ["cd", "goto"]:
                if len(args) == 0:
                    print("Please provide a directory name.")
                else:
                    directory = " ".join(args)
                    navigate_to_directory(directory)

    elif cmd in ["ls", "list"]:
        try:
            files = os.listdir(current_directory)
            for file in files:
                print(file)
        except FileNotFoundError:
            print("Directory not found.")

    elif cmd == "back":
        current_directory = os.path.dirname(current_directory)
        command_prompt = os.path.basename(current_directory) if current_directory else "CommandX"

    elif cmd == "search":
        if len(args) >= 1:
            query = " ".join(args)
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
        else:
            print("Please provide a search query.")
    
    elif cmd in ["where", "cdp"]:
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

    elif cmd in ["clear", "cls"]:
        clear_screen()
        chat_history = []  # Clear the chat history

        # Append the "clear" command to the history
        append_command_to_history(command)

    elif cmd == "chat" and "history" in args:
        for i, chat in enumerate(read_command_history(), start=1):
            print(f"{i}. {chat}")


    elif cmd in ["mkdir", "new"]:
        if len(args) == 1:
            create_item(args[0], "folder")
        else:
            print("Please provide a folder name.")
    
    elif cmd in ["touch", "createf"]:
        if len(args) == 1:
            create_item(args[0], "file")
        else:
            print("Please provide a file name.")
    
    elif cmd in ["delete", "remove", "rm"]:
        if len(args) == 1:
            delete_item(args[0], "folder" if args[0] in os.listdir(current_directory) and os.path.isdir(os.path.join(current_directory, args[0])) else "file")
        else:
            print("Please provide a file or folder name.")
    
    elif cmd == "rename":
        if len(args) == 2:
            item_type = "folder" if args[0] in os.listdir(current_directory) and os.path.isdir(os.path.join(current_directory, args[0])) else "file"
            rename_item(args[0], args[1], item_type)
        else:
            print("Please provide old and new file or folder names.")
    
    elif cmd == "copy":
        if len(args) == 1:
            item_type = "folder" if args[0] in os.listdir(current_directory) and os.path.isdir(os.path.join(current_directory, args[0])) else "file"
            copy_item(args[0], item_type)
        else:
            print("Please provide a file or folder name.")
    elif cmd == "paste":
        if len(args) == 0:
            item_type = "folder" if "clipboard" in os.listdir(current_directory) and os.path.isdir(os.path.join(current_directory, "clipboard")) else "file"
            paste_item("clipboard", item_type)
        else:
            print("Paste command does not require any arguments.")                       
            
    else:
        print("Hey there, how can I help you ?")

        # Append the command to the history
        append_command_to_history(command)
