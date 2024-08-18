import paramiko

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
        print(output)

        # Close the connection
        client.close()

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
ssh_command('192.168.169.47', 'sutro', 'sutro', 'ls')
