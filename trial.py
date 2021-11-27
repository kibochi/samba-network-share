import os
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
    
    os.system("cp file.txt file.bak")

if __name__ == "__main__":
    editConf()