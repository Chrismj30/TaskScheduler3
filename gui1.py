import tkinter as tk
from tkinter import ttk,messagebox, filedialog
from backup_app import BackupApp
import datetime
import os
import time
from ttkbootstrap import Style
from PIL import Image, ImageTk


class BackupAppGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Backup Application")
        self.root.geometry("400x400")

        # Load the background image
        image = Image.open("p11.jpg")  # Replace "background_image.jpg" with your image file
        # Resize the image to fit the screen size
        image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.background_image = ImageTk.PhotoImage(image)

        # Create a label to display the background image
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Change 'darkmode' to a valid theme name
        # Set background color to dark mode

        self.style = Style('superhero')  # Change 'darkmode' to a valid theme name
        self.style.theme_use('superhero')  # Change 'darkmode' to a valid theme name
        self.root.configure(bg=self.style.colors.bg)  # Set background color to dark mode

        self.top_bar = tk.Frame(self.root, bg="#011345")
        self.top_bar.pack(fill=tk.X)

        # App name label
        self.app_name_label = tk.Label(self.top_bar, text="Task Scheduler Application", font=("Helvetica", 18, "bold"), fg="white", bg="#011345")
        self.app_name_label.pack(pady=10)


        # Source directory input
        self.source_label = ttk.Label(self.root, text="Source Directory:", font=("Helvetica", 12), background="#011345")
        self.source_label.pack(pady=10)
        self.source_entry = ttk.Entry(self.root, font=("Helvetica", 12))  # Set background and foreground color
        self.source_entry.pack()
        self.browse_source_button = ttk.Button(self.root, text="Browse", command=self.browse_source, cursor="hand2")
        self.browse_source_button.pack()

        # Backup directory input
        self.backup_label = ttk.Label(self.root, text="Backup Directory:", font=("Helvetica", 12),background="#011345")
        self.backup_label.pack()
        self.backup_entry = ttk.Entry(self.root, font=("Helvetica", 12))  # Set background and foreground color
        self.backup_entry.pack()
        self.browse_backup_button = ttk.Button(self.root, text="Browse", command=self.browse_backup, cursor="hand2")
        self.browse_backup_button.pack()

        # Backup time input
        self.time_label = ttk.Label(self.root, text="Backup Time (HH:MM):", font=("Helvetica", 12),background="#011345")
        self.time_label.pack()
        self.time_entry = ttk.Entry(self.root, font=("Helvetica", 12))  # Set background and foreground color
        self.time_entry.pack()



        # Run backup button
        self.run_backup_button = ttk.Button(self.root, text="Run Backup", style="success.TButton", command=self.start_backup, cursor="hand2")
        self.run_backup_button.pack(pady=15)

        self.maintenance_label = ttk.Label(self.root, text="Maintenance Time (HH:MM):", font=("Helvetica", 12),background="#011345")
        self.maintenance_label.pack()
        self.maintenance_entry = ttk.Entry(self.root, font=("Helvetica", 12))
        self.maintenance_entry.pack()

# Date input for maintenance


        # Run maintenance button
        self.run_maintenance_button = ttk.Button(self.root, text="Run Maintenance", style="danger.TButton", command=self.start_maintenance, cursor="hand2")
        self.run_maintenance_button.pack(pady=15)

        # Opening time input
        self.opening_time_label = ttk.Label(self.root, text="Application Opening Time (HH:MM):", font=("Helvetica", 12),background="#011345")
        self.opening_time_label.pack()
        self.opening_time_entry = ttk.Entry(self.root, font=("Helvetica", 12))  # Set background and foreground color
        self.opening_time_entry.pack()

        # Run application button
        self.run_app_button = ttk.Button(self.root, text="Run Application", style="info.TButton", command=self.run_application, cursor="hand2")
        self.run_app_button.pack(pady=15)

        # Status message
        self.status_var = tk.StringVar()
        self.status_label = ttk.Label(self.root, textvariable=self.status_var, font=("Helvetica", 12))
        self.status_label.pack()



    def browse_source(self):
        source_dir = filedialog.askdirectory()
        if source_dir:
            self.source_entry.delete(0, tk.END)
            self.source_entry.insert(0, source_dir)

    def browse_backup(self):
        backup_dir = filedialog.askdirectory()
        if backup_dir:
            self.backup_entry.delete(0, tk.END)
            self.backup_entry.insert(0, backup_dir)

    def start_backup(self):
        source_dir = self.source_entry.get()
        backup_dir = self.backup_entry.get()
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
        application_path = filedialog.askopenfilename(title="Select Application")
        if not application_path:
            return

        opening_time = self.opening_time_entry.get()
        if not self.validate_time_format(opening_time):
            messagebox.showerror("Error", "Invalid opening time format. Please use HH:MM.")
            return

        confirmation = messagebox.askyesno("Confirmation", f"Do you want to open the applicationhsl(224.12deg 97.14% 13.73%) '{application_path}' at {opening_time}?")
        if confirmation:
            schedule_opening(application_path, opening_time)
            self.status_var.set(f"Application scheduled to open at {opening_time}.")
        else:
            self.status_var.set("Application opening cancelled.")

    def run(self):
        self.root.mainloop()

    def start_maintenance(self):
        maintenance_time = self.maintenance_entry.get()

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