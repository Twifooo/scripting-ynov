import tempfile
import time

# Create a temporary file
with tempfile.NamedTemporaryFile(
    mode='w+t',           # File mode (text, read/write)
    prefix='tempFile_',      # Filename prefix
    suffix='.txt',        # Filename suffix
    dir='/home/malek/Documents/projects/scripting-ynov/Maleks-quests/chapter-2/',           # Directory location
    delete=True           # Auto-delete when closed
) as temp:
    print(temp.name) 
    # Write to it
    temp.write('Hello, temporary world!\n')
    
    # Go back to the beginning
    temp.seek(0)
    
    # Read from it
    print(temp.read())  # prints: Hello, temporary world! 

    # Wait for a moment before the file is deleted
    time.sleep(30)

# File is automatically deleted after the 'with' block