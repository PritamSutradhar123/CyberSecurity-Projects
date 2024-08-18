import customtkinter as ctk
import paramiko
import os
from stat import S_ISDIR

# Initialize customtkinter
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

def scp_command(ip, user, password, remote_path, local_path):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=user, password=password)

        sftp = client.open_sftp()

        if S_ISDIR(sftp.stat(remote_path).st_mode):
            def download_dir(remote_dir, local_dir):
                if not os.path.exists(local_dir):
                    os.makedirs(local_dir)
                for item in sftp.listdir_attr(remote_dir):
                    remote_item = remote_dir + '/' + item.filename
                    local_item = os.path.join(local_dir, item.filename)
                    if S_ISDIR(item.st_mode):
                        download_dir(remote_item, local_item)
                    else:
                        sftp.get(remote_item, local_item)

            download_dir(remote_path, local_path)
        else:
            sftp.get(remote_path, os.path.join(local_path, os.path.basename(remote_path)))

        sftp.close()
        client.close()
        result_label.configure(text=f"Files from {remote_path} have been copied to {local_path}")

    except Exception as e:
        result_label.configure(text=f"An error occurred: {e}")

def execute_command():
    user = username_entry.get()
    ip = ip_entry.get()
    password = password_entry.get()
    remote_path = remote_path_entry.get()
    local_path = local_path_entry.get()
    
    scp_command(ip, user, password, remote_path, local_path)

# Create the main window
root = ctk.CTk()
root.title("SCP GUI")
root.geometry("400x350")

# Username Entry
username_label = ctk.CTkLabel(root, text="Username:")
username_label.pack(pady=5)
username_entry = ctk.CTkEntry(root)
username_entry.pack(pady=5)

# IP Address Entry
ip_label = ctk.CTkLabel(root, text="IP Address:")
ip_label.pack(pady=5)
ip_entry = ctk.CTkEntry(root)
ip_entry.pack(pady=5)

# Password Entry
password_label = ctk.CTkLabel(root, text="Password:")
password_label.pack(pady=5)
password_entry = ctk.CTkEntry(root, show="*")
password_entry.pack(pady=5)

# Remote Path Entry
remote_path_label = ctk.CTkLabel(root, text="Remote Path:")
remote_path_label.pack(pady=5)
remote_path_entry = ctk.CTkEntry(root)
remote_path_entry.pack(pady=5)

# Local Path Entry
local_path_label = ctk.CTkLabel(root, text="Local Path:")
local_path_label.pack(pady=5)
local_path_entry = ctk.CTkEntry(root)
local_path_entry.pack(pady=5)

# Execute Button
execute_button = ctk.CTkButton(root, text="Execute", command=execute_command)
execute_button.pack(pady=20)

# Result Label
result_label = ctk.CTkLabel(root, text="")
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
