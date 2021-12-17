from colorama import Fore
import colorama
import pyfiglet
import os


colorama.init()
print( Fore.RED + pyfiglet.figlet_format( "let's Samba", font = "bulbhead" ))


 
def checkRoot():
    user = os.getenv("SUDO_USER")
    if user is None:
        print(Fore.RED + "Damn!!!.Youre Not Root")
      
    else:
     username()



def username():
    global username
    username = input(Fore.GREEN + "enter username to add =:")
    print(Fore.WHITE + f"********checking if {username} is available********")
    checkUsers()
    
   


def newUser():
    os.system(f"sudo useradd {username}")
    print("[x]done")
    smb()



def smb():
    
    try:
        os.system(Fore.GREEN + f"sudo smbpasswd -a {username}")
        
      
        print(Fore.GREEN + "[x]***** Done *****")
        path()
        
    except:
        print(Fore.RED+ "[x] an error occured")
  
    


def checkIsDir():
    if  not os.path.isdir(paths):
        print(Fore.RED + "[-] Error!!!!! place the  correct path")
        path()
    else:
        os.system(f"sudo chown {username} {paths}")
        editConf()
        

def checkUsers():
   users = os.popen("awk -F':' '{print $1}' /etc/passwd ").read()
   if(username in users):
       print(Fore.RED + "[-]username already exists adding it to smb")
       smb()
   else:
       print(Fore.GREEN + f"[x]Adding {username} to system")
       newUser()
      

def path():
    global paths
    paths = input(Fore.GREEN + "enter volume/folder path to be shared =:") 
    checkIsDir()
      



def editConf():
    global sharename
    sharename = input(Fore.GREEN + "enter share name =:")
    content = [
        f"[{sharename}]",
        "\tpath = " f"{paths}",
        "\tread only = yes" , 
        "\tbrowseable = yes"
    ]

    backup()
    
    with open("/etc/samba/smb.conf","r+") as f:
        eof = f.read()
        if eof == "":
            f.writelines(";shared folder starts here" '\n')   
        for x in content:
            f.writelines(x+ '\n')
    restart()



def backup():
    os.system("cp /etc/samba/smb.conf /etc/samba/smb.bak")


def restart():
    os.system("service smbd restart")
    print(Fore.GREEN + "Done...Enjoy")

if __name__ == "__main__":
    checkRoot()
