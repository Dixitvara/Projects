# Import Module
import ftplib

# Fill Required Information
HOSTNAME = "ftp.dlptest.com"
USERNAME = "dlpuser"
PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"

# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

# Enter File Name with Extension (First create text file and write content into text file)
filename = "demo.txt"

# Read file in binary mode
with open(filename, "rb") as file:
	#Command for Uploading the file "STOR filename"
	ftp_server.storbinary(f"STOR {filename}", file)

# Get list of files
ftp_server.dir()

#Download the File
with open(filename, "wb") as file:
    # Command for Downloading the file "RETR filename"
    ftp_server.retrbinary(f"RETR {filename}", file.write)

# Read content from File
file= open(filename, "r")
print('File Content:', file.read())
    
# Close the Connection
ftp_server.quit()
