
import os



def checkRoot():
    user = os.getenv("SUDO_USER")
    if user is None:
        print("Damn!!!.Youre Not Root")
      
    else:
       addUser()


""" 
add user to  system
add user to smb with a password
give user ownership to shared path

"""

def addUser():
    global username
    global paths

    username = input("enter username to add =:")
    paths = input("enter volume/folder path to be shared =:")
    print(f'''[x]*****Adding {username} to system without shell\n 
            adding the user to smb \n 
            changing folder/volume ownership*****''')
    user = os.system(f"useradd {username} --shell /bin/false")
    os.system(f"smbpasswd -a {user}")
    os.system(f"chown {user} {paths}")
    print("[x]***** Done *****")
    editConf()


def editConf():
    content = [
        "[SharedFolder]",
        "\tpath = paths",
        "\tforce users = user",
        "\tread only = yes" , 
        "\tbrowseable = yes"
    ]

    backup()
    
    with open("file.txt","r+") as f:
        eof = f.read()
        if eof == "":
            f.writelines(";shared folder starts here" '\n')   
        for x in content:
            f.writelines(x+ '\n')




def backup():
    os.system("cp /etc/samba.conf /etc/samba.bak")


def restart():
    os.system("service smbd restart")

if __name__ == "__main__":
    checkRoot()
