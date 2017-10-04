import hashlib  # Generate MD5 hashes

__version__ = "0.1"

def generateHash(data):
    hash = hashlib.md5(data.encode())
    return hash.hexdigest()

def verifyChecksum():
    filePath = input("Please enter the path of the file: ")
    checksum = input("Please enter the checksum of the file: ")
    try:
        print("Verifying checksum...")
        with open(filePath) as fileObject:
            fileData = fileObject.read()
            generatedChecksum = generateHash(fileData)
            if generatedChecksum == checksum:
                print("Checksum verified")
            else:
                print("Checksum does not match!")
    except:
        print("There was an issue while verifying the checksum")

def generateChecksum():
    filePath = input("Please enter the path of the file: ")
    try:
        print("Verifying checksum...")
        with open(filePath) as fileObject:
            fileData = fileObject.read()
            checksum = generateHash(fileData)
            print("Checksum for file: "+filePath+ " is: "+checksum)
    except:
        print("There was an issue while generating the checksum")

print("ChecksumVerifier "+__version__)
while True:
    print("1. Generate checksum") 
    print("2. Verify checksum")
    option = input("Please choose an option: ")
    if option == "1":
        generateChecksum()
    elif option == "2":
        verifyChecksum()
    else:
        print("Please choose a valid option")
        

    
