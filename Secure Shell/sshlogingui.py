import customtkinter as ctk
import paramiko

# Function to execute an SSH command
def ssh_command(ip, user, password, command):
    try:
        # Initialize the SSH client
        client = paramiko.SSHClient()

        # Automatically add the server's SSH key (not recommended for production)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SSH server
        client.connect(ip, username=user, password=password)

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)

        # Read the output from stdout
        output = stdout.read().decode()

        # Print the output
        result_label.configure(text=output)

        # Close the connection
        client.close()

    except Exception as e:
        result_label.configure(text=f"An error occurred: {e}")

# Function to execute the SSH command when the button is clicked
def execute_command():
    user = username_entry.get()
    ip = ip_entry.get()
    password = password_entry.get()
    command = command_entry.get()
    
    ssh_command(ip, user, password, command)

# Initialize customtkinter
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Create the main window
root = ctk.CTk()
root.title("SSH Command Executor")
root.geometry("400x500")

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

# Command Entry
command_label = ctk.CTkLabel(root, text="Command:")
command_label.pack(pady=5)
command_entry = ctk.CTkEntry(root)
command_entry.pack(pady=5)

# Execute Button
execute_button = ctk.CTkButton(root, text="Execute", command=execute_command)
execute_button.pack(pady=20)

# Result Label
result_label = ctk.CTkLabel(root, text="")
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
