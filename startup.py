import os
import time
import psutil  # Import the psutil library

class Startup:
    def __init__(self):
        self.ampm = time.strftime("%p")
        self.name = "Rey"
        self.start()

    def start(self):
        print(f"Welcome back, {self.name}!")
        print("")
        print(f"Your system started at {time.strftime('%A %B %d, %Y')} {time.strftime('%H:%M:%S')} {self.ampm}")
        print("")
        self.overlay()

    def is_app_running(self, app_name):
        """
        Check if an application is already running.
        """
        # Iterate through all running processes
        for proc in psutil.process_iter(['name']):
            try:
                # Check if process name matches the app name
                if app_name.lower() in proc.info['name'].lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def overlay(self):
        start = input("Would you like to start your overlay, y or n? ")
        while start not in ["y", "n"]:
            start = input("Would you like to start your overlay, y or n? ")
        if start == "n":
            exit()
        elif start == "y":
            print("Gotcha!")
            print("Starting overlay in:")
            for i in range(3, 0, -1):
                print(i)
                time.sleep(1)

            # Check if Chrome is already running
            if not self.is_app_running("chrome.exe"):
                # Path to Chrome's executable; change it according to your installation
                chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
                try:
                    os.startfile(chrome_path)
                except OSError:
                    print("Failed to open Google Chrome")

            try:
                with open("I:/CodeProjects/Python/Startup/app_list.txt", "r") as file:
                    apps = file.readlines()
            except FileNotFoundError:
                print("File not found!")
                exit()

            for app in apps:
                app = app.strip()
                if not self.is_app_running(app):  # Check if the app is running
                    try:
                        os.startfile(app)
                    except OSError:
                        print(f"Failed to open {app}")

if __name__ == "__main__":
    Startup()
