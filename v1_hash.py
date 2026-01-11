import hashlib
# text = "play"
# hash_object= hashlib.sha256(text.encode())
# hash_digest= hash_object.hexdigest()

# print(f"The sha-256 of {text} is " " ",hash_digest )


def encrypt_file (path):
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
           print (f"Error {e} Retry again check the file path")
           return 
    
def check_intergity (path1,path2):
    hash_one = encrypt_file(path1) 
    path = path2
    if hash_one is None or path is None:
        print("\nIntergity check fail!! cant compare none type.")
        return
    
    # print(f"\nThe sha-256 of {path1} is  {hash_one}")
    # print(f"\nThe sha-256 of {path2} is  {hash_two}")

    if hash_one == path:
        print("\nFile is safe the encryption is intact\n")
    else:
        print ("File is compromized probably unsafe!!!\n")

if __name__=="__main__":
    file_path = R"C:\Users\stephen\Downloads\tesseract-ocr-w64-setup-5.4.0.20240606.exe"
    file_hash = encrypt_file(file_path)
    if file_hash:
        print(f"\nThe sha-256 of {file_path} is  {file_hash}")
    else:
        print("An error occured!! no such path detected ")

    # check_intergity(R"C:\Users\stephen\Downloads\tesseract-ocr-w64-setup-5.4.0.20240606.exe"
    #                 ,"C885FFF6998E0608BA4BB8AB51436E1C6775C2BAFC2559A19B423E18678B60C9")
    
    # check_intergity(R"venv\scripts\modules\test2.text",
    #                 R"venv\scripts\modules\test3.txt")


