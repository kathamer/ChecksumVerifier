import hashlib  # Generate MD5 hashes
import click    # Make beautiful command line interfaces

__version__ = "0.2"

"""Generate an MD5 hash"""
def generateHash(data):
    hash = hashlib.md5(data)
    return hash.hexdigest()

"""Verify an MD5 checksum"""
def verifyChecksum():
    filePath = input("Please enter the path of the file: ")
    checksum = input("Please enter the checksum of the file: ")
    try:
        click.echo("Verifying checksum...")
        with open(filePath, "rb") as fileObject:
            fileData = fileObject.read()  # Read binary data
            generatedChecksum = generateHash(fileData)  # Generate an MD5 hash for the binary data
            if generatedChecksum == checksum:  # If checksums match
                click.secho("Checksum verified!", fg = "green")
            else: 
                click.secho("Checksum does not match!", fg = "red")
    except:
        click.secho("There was an issue while verifying the checksum", fg = "red")

"""Generate an M55 checksum"""
def generateChecksum():
    filePath = input("Please enter the path of the file: ")
    try:
        click.echo("Verifying checksum...")
        with open(filePath, "rb") as fileObject:
            fileData = fileObject.read()  # Read binary data
            checksum = generateHash(fileData)  # Generate an MD5 hash for binary data
            click.echo("Checksum for file: " + click.style(filePath, fg = "green") + " is: " + click.style(checksum, fg = "green"))
    except:
        print("There was an issue while generating the checksum")

def main():
    click.echo("ChecksumVerifier "+__version__)
    while True:
        click.echo("1. Generate checksum") 
        click.echo("2. Verify checksum")
        option = input("Please choose an option: ")
        if option == "1":
            generateChecksum()
        elif option == "2":
            verifyChecksum()
        else:
            click.echo("Please choose a valid option")
        
if __name__ == "__main__":
    main()    
