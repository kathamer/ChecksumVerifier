import hashlib  # Generate MD5 hashes

__version__ = "0.1"

supportedHashes = ["sha256", "md5"]

def generateHash(data, hashtype):
    if hashtype == "md5":
        hash = hashlib.md5(data)
    elif hashtype == "sha256":
        hash = hashlib.sha256(data)
    else:
        raise ValueError
    return hash.hexdigest()

def verifyChecksum(hashtype):
    filePath = input("Please enter the path of the file: ")
    checksum = input("Please enter the checksum of the file: ")
    try:
        print("Verifying checksum...")
        with open(filePath, "rb") as fileObject:
            fileData = fileObject.read()
            generatedChecksum = generateHash(fileData, hashtype)
            if generatedChecksum == checksum:
                print("Checksum verified")
            else:
                print("Checksum does not match!")
    except:
        print("There was an issue while verifying the checksum")

def generateChecksum(hashtype):
    filePath = input("Please enter the path of the file: ")
    try:
        print("Verifying checksum...")
        with open(filePath, "rb") as fileObject:
            fileData = fileObject.read()
            checksum = generateHash(fileData, hashtype)
            print("Checksum for file: "+filePath+ " is: "+checksum)
    except:
        print("There was an issue while generating the checksum")

print("ChecksumVerifier "+__version__)
while True:
    print("1. Generate checksum") 
    print("2. Verify checksum")
    option = input("Please choose an option: ")
    for i, hashtype in enumerate(supportedHashes):
        print(str(i + 1) + ". " + hashtype)
    hashtype = input("Please choose a hash type: ")
    if hashtype in supportedHashes:
        if option == "1":
            generateChecksum(hashtype)
        elif option == "2":
            verifyChecksum(hashtype)
        else:
            print("Please choose a valid option")
    else:
        print("Unsupported hashtype!")

    
