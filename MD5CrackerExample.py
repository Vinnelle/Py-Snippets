import hashlib

def md5Crack(hash, password):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))

    if m.hexdigest() == hash:
        print("Password cracked!")
        print("Password is: " + password)

def main():
    hash = input("Enter the MD5 hash to crack: ")
    password = input("Enter the password to try: ")

    md5Crack(hash, password)

if __name__ == "__main__":
    main()
