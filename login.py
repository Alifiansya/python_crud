import json, hashlib, getpass

# login attempt
def login():
    with open("data.json", 'r') as f:
        login_data = json.load(f)["admin_login"]
        print([x["uname"] for x in login_data])
        ava_uname = [x["uname"] for x in login_data]  
        # checking the username and password validity
        while(True):
            login_uname = input("admin login: ")
            pswd = hashlib.sha256(getpass.getpass("password: ").encode("utf-8")).hexdigest()
            if(login_uname not in ava_uname):
                print("Login incorrect\n")
                continue
            pswd_id = ava_uname.index(login_uname)
            if(pswd != login_data[pswd_id]["password"]):
                print("Login incorrect\n")
                continue
            else:
                print(f"\nWelcome {login_uname}")
                break