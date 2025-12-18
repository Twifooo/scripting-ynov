import subprocess
import getpass

username = "admin"
password = getpass.getpass("Enter MySQL password: ")  # Hidden input
database = "test_db"
query = "SELECT * FROM users;"

# Build command
command = ['mysql', '-u', username, f'-p{password}', database, '-e', query]

result = subprocess.run(command, capture_output=True, text=True)

if result.returncode == 0:
    print("Query successful!")
    print(result.stdout)
else:
    print("Error:", result.stderr)