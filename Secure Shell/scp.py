import paramiko
import os
from stat import S_ISDIR

def scp_command(ip, user, password, remote_path, local_path):
    try:
        # Initialize the SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=user, password=password)

        sftp = client.open_sftp()

        # Print paths to verify correctness
        print(f"Remote path: {remote_path}")
        print(f"Local path: {local_path}")

        # If the remote path is a directory, download recursively
        if S_ISDIR(sftp.stat(remote_path).st_mode):
            download_dir(remote_path, local_path)
        else:
            # If it's a file, just download it directly
            sftp.get(remote_path, os.path.join(local_path, os.path.basename(remote_path)))

        sftp.close()
        client.close()

        print(f"Files from {remote_path} have been copied to {local_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
scp_command('192.168.169.47', 'sutro', 'sutro', '/home/sutro/image1.jpg', 'D:/')
