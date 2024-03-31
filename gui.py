import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from ttkbootstrap import Style
from backup_app import BackupApp
from PIL import Image, ImageTk
import datetime
import os
import time


class BackupAppGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Backup Application")
        self.root.geometry("400x400")

        self.style = Style('vapor')
        self.style.theme_use('vapor')
        self.style.configure('Curved.TButton', borderwidth=2, relief='raised', padding=10, borderradius=100)


        # Top Bar
        self.top_bar = tk.Frame(self.root, bg="#85C1E9")
        self.top_bar.pack(fill=tk.X)
        self.app_name_label = tk.Label(self.top_bar, text="Task Scheduler Application", font=("Helvetica", 24, "bold"), fg="white", bg="#011345")
        self.app_name_label.pack(pady=10)


        # Home Frame
        self.home_frame = tk.Frame(self.root, bg="#2C3E50")
        self.home_frame.pack(fill=tk.BOTH, expand=True)

        # Home Widgets
        self.create_home_widgets()

        # Backup Frame
        self.backup_frame = tk.Frame(self.root, bg="#2C3E50")
        self.create_backup_widgets()

        # Maintenance Frame
        self.maintenance_frame = tk.Frame(self.root, bg="#2C3E50")
        self.create_maintenance_widgets()

        # Open Application Frame
        self.open_app_frame = tk.Frame(self.root, bg="#2C3E50")
        self.create_open_app_widgets()



        # Initially show the home frame
        self.show_frame(self.home_frame)


    def show_frame(self, frame):
        # Hide all frames and then show the specified frame
        for f in [self.home_frame, self.backup_frame, self.maintenance_frame, self.open_app_frame]:
            f.pack_forget()
        frame.pack(fill=tk.BOTH, expand=True)

    def create_welcome_message(self):
        image = Image.open("p11.jpg")
        image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.background_image = ImageTk.PhotoImage(image)
        welcome_message = tk.Label(self.home_frame, text="Welcome to Task Scheduler Application!\n\nThis application helps you manage your tasks efficiently.\n\nYou can use the following features:\n\n1. Backup: Schedule backups of your important files.\n2. Maintenance: Schedule maintenance tasks.\n3. Open Application: Schedule opening of applications.\n\nSimply click on the respective buttons to access these features and follow the instructions.\n\nEnjoy organizing your tasks!", font=("Helvetica", 14), bg="white", fg="black", image=self.background_image,compound="none")
        welcome_message.place(x=0, y=0, relwidth=1, relheight=1)


        

    def create_home_widgets(self):
        
        self.create_welcome_message()
        # Home Widgets
        # Home Widgets
        welcome_message = tk.Label(self.home_frame, text="Welcome to Task Scheduler Application!\n\nThis application helps you manage your tasks efficiently.\n\nYou can use the following features:\n\n1. Backup: Schedule backups of your important files.\n2. Maintenance: Schedule maintenance tasks.\n3. Open Application: Schedule opening of applications.\n\nSimply click on the respective buttons to access these features and follow the instructions.\n\nEnjoy organizing your tasks!", font=("Helvetica", 14), bg="white", fg="black",background="#011345")
        welcome_message.pack(pady=20)
        backup_button = ttk.Button(self.home_frame, text="Backup", style="Curved.TButton", command=lambda: self.show_frame(self.backup_frame))
        backup_button.pack(pady=10)

        maintenance_button = ttk.Button(self.home_frame, text="Maintenance", style="Curved.TButton", command=lambda: self.show_frame(self.maintenance_frame))
        maintenance_button.pack(pady=10)

        open_app_button = ttk.Button(self.home_frame, text="Open Application", style="Curved.TButton", command=lambda: self.show_frame(self.open_app_frame))
        open_app_button.pack(pady=10)



    def create_backup_widgets(self):
    # Backup Widgets

        self.backup_source_label = ttk.Label(self.backup_frame, text="Source Directory:", font=("Helvetica", 12))
        self.backup_source_label.pack(pady=10)
        self.backup_source_entry = ttk.Entry(self.backup_frame, font=("Helvetica", 12))
        self.backup_source_entry.pack()

        self.backup_source_browse_button = ttk.Button(self.backup_frame, text="Browse", command=self.browse_source)
        self.backup_source_browse_button.pack(pady=5)

        self.backup_dest_label = ttk.Label(self.backup_frame, text="Destination Directory:", font=("Helvetica", 12))
        self.backup_dest_label.pack(pady=10)
        self.backup_dest_entry = ttk.Entry(self.backup_frame, font=("Helvetica", 12))
        self.backup_dest_entry.pack()

        self.backup_source_browse_button = ttk.Button(self.backup_frame, text="Browse", command=self.browse_backup)
        self.backup_source_browse_button.pack(pady=5)

        self.backup_time_label = ttk.Label(self.backup_frame, text="Backup Time (HH:MM):", font=("Helvetica", 12))
        self.backup_time_label.pack(pady=10)
        self.time_entry = ttk.Entry(self.backup_frame, font=("Helvetica", 12))  # Set background and foreground color
        self.time_entry.pack()


        self.backup_button = ttk.Button(self.backup_frame, text="Run Backup", style="success.TButton", command=self.start_backup)
        self.backup_button.pack(pady=10)

        self.backup_home_button = ttk.Button(self.backup_frame, text="Back to Home", style="info.TButton", command=lambda: self.show_frame(self.home_frame))
        self.backup_home_button.pack(pady=10)

    def browse_source(self):
        source_dir = filedialog.askdirectory()
        if source_dir:
            self.backup_source_entry.delete(0, tk.END)
            self.backup_source_entry.insert(0, source_dir)

    def browse_backup(self):
        backup_dir = filedialog.askdirectory()
        if backup_dir:
            self.backup_dest_entry.delete(0, tk.END)
            self.backup_dest_entry.insert(0, backup_dir)
    
    


    def create_maintenance_widgets(self):
        # Maintenance Widgets
        self.maintenance_time_label = ttk.Label(self.maintenance_frame, text="Maintenance Time (HH:MM):", font=("Helvetica", 12))
        self.maintenance_time_label.pack(pady=10)
        self.maintenance_time_entry = ttk.Entry(self.maintenance_frame, font=("Helvetica", 12))
        self.maintenance_time_entry.pack()

        self.maintenance_button = ttk.Button(self.maintenance_frame, text="Run Maintenance", style="danger.TButton", command=self.start_maintenance)
        self.maintenance_button.pack(pady=10)

        self.maintenance_home_button = ttk.Button(self.maintenance_frame, text="Back to Home", style="info.TButton", command=lambda: self.show_frame(self.home_frame))
        self.maintenance_home_button.pack(pady=10)

    def create_open_app_widgets(self):
        # Open Application Widgets
        self.app_path_label = ttk.Label(self.open_app_frame, text="Application Path:", font=("Helvetica", 12))
        self.app_path_label.pack(pady=10)
        self.app_path_entry = ttk.Entry(self.open_app_frame, font=("Helvetica", 12))
        self.app_path_entry.pack()

        self.app_path_browse_button = ttk.Button(self.open_app_frame, text="Browse", command=self.browse_application)
        self.app_path_browse_button.pack(pady=5)


        self.open_app_time_label = ttk.Label(self.open_app_frame, text="Opening Time (HH:MM):", font=("Helvetica", 12))
        self.open_app_time_label.pack(pady=10)
        self.open_app_time_entry = ttk.Entry(self.open_app_frame, font=("Helvetica", 12))
        self.open_app_time_entry.pack()

        self.open_app_button = ttk.Button(self.open_app_frame, text="Open Application", style="info.TButton", command=self.run_application)
        self.open_app_button.pack(pady=10)

        self.open_app_home_button = ttk.Button(self.open_app_frame, text="Back to Home", style="info.TButton", command=lambda: self.show_frame(self.home_frame))
        self.open_app_home_button.pack(pady=10)
    def browse_application(self):
        application_path = filedialog.askopenfilename(title="Select Application")
        if application_path:
            self.app_path_entry.delete(0, tk.END)
            self.app_path_entry.insert(0, application_path)

          # Status message
        self.status_var = tk.StringVar()
        self.status_label = ttk.Label(self.root, textvariable=self.status_var, font=("Helvetica", 12))
        self.status_label.pack()

    def start_backup(self):
        source_dir = self.backup_source_entry.get()
        backup_dir = self.backup_dest_entry.get()
        backup_time = self.time_entry.get()

        if not source_dir or not backup_dir or not backup_time:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not self.validate_time_format(backup_time):
            messagebox.showerror("Error", "Invalid backup time format. Please use HH:MM.")
            return

        confirmation = messagebox.askyesno("Confirmation", f"Do you want to start the backup process for '{source_dir}' to '{backup_dir}' at {backup_time}?")
        if confirmation:
            app = BackupApp(source_dir, backup_dir, backup_time)
            app.run_backup()
            self.status_var.set("Backup completed.")
        else:
            self.status_var.set("Backup process cancelled.")

    def validate_time_format(self, time_str):
        try:
            datetime.datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False

    def run_application(self):
        application_path = self.app_path_entry.get()
        if not application_path:
            messagebox.showerror("Error", "Please specify the application path.")
            return

        opening_time = self.open_app_time_entry.get()
        if not self.validate_time_format(opening_time):
            messagebox.showerror("Error", "Invalid opening time format. Please use HH:MM.")
            return

        confirmation = messagebox.askyesno("Confirmation", f"Do you want to open the application '{application_path}' at {opening_time}?")
        if confirmation:
            schedule_opening(application_path, opening_time)
            self.status_var.set(f"Application scheduled to open at {opening_time}.")
        else:
            self.status_var.set("Application opening cancelled.")

    def run(self):
        self.root.mainloop()

    def start_maintenance(self):
        maintenance_time = self.maintenance_time_entry.get()

        if not maintenance_time:
            messagebox.showerror("Error", "Please enter the maintenance time.")
            return

        if not self.validate_time_format(maintenance_time):
            messagebox.showerror("Error", "Invalid maintenance time format. Please use HH:MM.")
            return

        confirmation = messagebox.askyesno("Confirmation", f"Do you want to perform maintenance at {maintenance_time}?")
        if confirmation:
            schedule_maintenance(maintenance_time)
            self.status_var.set(f"Maintenance scheduled at {maintenance_time}.")
        else:
            self.status_var.set("Maintenance scheduling cancelled.")

    def validate_time_format(self, time_str):
        try:
            datetime.datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False

    def run(self):
        self.root.mainloop()
    
def schedule_opening(application_path, opening_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == opening_time:
            os.system(f'start "" "{application_path}"')
            print(f"Application opened at {opening_time}.")
            break
        time.sleep(60)  # Check every minute if it's time to open the application


def schedule_maintenance(maintenance_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == maintenance_time:
            os.system("cleanmgr")
            print(f"Maintenance performed at {maintenance_time}.")
            break
        time.sleep(60)  # Check every minute if it's time to perform maintenance    