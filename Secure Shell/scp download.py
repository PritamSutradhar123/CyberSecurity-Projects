import customtkinter as ctk
import subprocess
import threading

def execute_scp_command():
    username = username_entry.get()
    ip_address = ip_entry.get()
    source_location = source_entry.get()
    destination_location = destination_entry.get()
    if username and ip_address and source_location and destination_location:
        command = f"scp {username}@{ip_address}:~{source_location} {destination_location}"
        disable_buttons()
        thread = threading.Thread(target=run_command, args=(command,))
        thread.start()
        root.after(100, check_thread, thread)

def run_command(command):
    # Run SCP command
    full_command = f"powershell -Command \"{command}\""
    subprocess.run(full_command, shell=True)

def check_thread(thread):
    if thread.is_alive():
        root.after(100, check_thread, thread)
    else:
        enable_buttons()

def disable_buttons():
    execute_button.configure(state=ctk.DISABLED)

def enable_buttons():
    execute_button.configure(state=ctk.NORMAL)

# Create customtkinter window
root = ctk.CTk()
root.title("Execute SCP Command")
root.geometry("400x400")  # Adjust size as needed
root.configure(bg="#1e1e1e")  # Set background color to black

# Create username and IP address entry fields
username_label = ctk.CTkLabel(root, text="Username:", bg_color="#1e1e1e", fg_color="#ffffff")
username_label.pack(pady=5)
username_entry = ctk.CTkEntry(root, placeholder_text="Enter username")
username_entry.pack(pady=5, padx=20, fill='x')

ip_label = ctk.CTkLabel(root, text="IP Address:", bg_color="#1e1e1e", fg_color="#ffffff")
ip_label.pack(pady=5)
ip_entry = ctk.CTkEntry(root, placeholder_text="Enter IP address")
ip_entry.pack(pady=5, padx=20, fill='x')

# Create source and destination entry fields
source_label = ctk.CTkLabel(root, text="Source Location:", bg_color="#1e1e1e", fg_color="#ffffff")
source_label.pack(pady=5)
source_entry = ctk.CTkEntry(root, placeholder_text="Enter source location")
source_entry.pack(pady=5, padx=20, fill='x')

destination_label = ctk.CTkLabel(root, text="Destination Location:", bg_color="#1e1e1e", fg_color="#ffffff")
destination_label.pack(pady=5)
destination_entry = ctk.CTkEntry(root, placeholder_text="Enter destination location")
destination_entry.pack(pady=5, padx=20, fill='x')

# Create execute button
execute_button = ctk.CTkButton(root, text="Execute", command=execute_scp_command)
execute_button.pack(pady=20)

# Run the customtkinter main loop
root.mainloop()
