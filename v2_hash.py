import hashlib

def view_hash():
    words= input("Type the word  or sentence to see its sha-256 hash: ")
    hash_object= hashlib.sha256(words.encode())
    hash_digest= hash_object.hexdigest()

    return print(f"The sha-256 of {words} is " " ",hash_digest )


def hash_file (path=None):
    if not path : path = input("\nEnter the path of your file: ")
    h =  hashlib.sha256()
    try:
        with open(path,"rb") as file:
            while True:
                chunk = file.read(1024)
                if chunk == b"":
                    break
                h.update(chunk)
        return h.hexdigest()    
            
    except Exception as e:
           print (f"Error {e} Retry again check the file path or remove the speech marks")
           return 


def hash_your_file():
   hashed = hash_file()
   if hashed:
    print(f"\nHere is the sha-256 hash of your file:  {hashed}\n")
   else:
       return  

def check_integrity_file_and_file():
    path1= input("\nEnter the path of the first file: ")
    path2 = input("\nEnter the path of the second file: ")
    hash_one= hash_file(path1)
    hash_two=hash_file(path2)
    if hash_one is None or hash_two is None:
        print("\nDouble check the file paths\n")

    elif hash_one == hash_two:
        print("\nThe files are the same none is tamperd with \n")    

    else:
        print("\nThe files are not the same probaly one is compramised\n")
        

def check_integrity_file_and_hash():
    path = input("\nEnter the path of the file: ")
    hash_one = hash_file(path) 
    hash_256 = input("\nEnter the sha-256 hash provided by developers with no spaces: ")
    if hash_one is None or hash_256 is None:
        print("\nIntergity check fail!! cant compare none type.")
        return

    if hash_one == hash_256:
        print("\nFile is safe the hash  is intact\n")
    else:
        print ("\nFile is compromized probably unsafe!!!\n")

if __name__=="__main__":
    choices ={
    0:'Exit',
    1:view_hash,
    2:hash_your_file,
    3:check_integrity_file_and_hash,
    4:check_integrity_file_and_file
    }
    online=True
    print("\n=====Choose from the menu===== \n")
    print("1:Hash a text or word\n")
    print("2:Hash  a whole file\n")
    print("3:Verify integrity between file and a sha-256 hash of it\n")
    print("4:Verify integrity between two files\n")
    print("0:exit\n")
    while online:
        try:
            user_choice = int(input("\nEnter your desired option: "))
            if user_choice not in choices:
                print("\nInvalid option")
                break 
            elif user_choice == 0:
                print("\nGoodbye be safe out there\n")
                online = False

            else:
                choices[user_choice]()    

        except ValueError:
            print("Enter numerics only\n")
            break
