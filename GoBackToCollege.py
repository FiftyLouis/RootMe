
import socket, time, os, math

def pingpong():
    while 1:
        junk=""
        junk = irc.recv(7000)
        print(junk)
        beg = junk.find("PING")
        print(beg)
        if beg>-1:
            junk=junk[:beg]
            if junk[5:].find(" ")>0:
                junk=junk[:(junk[5:].find(" "))+4]+b"\r\n"

            junk = junk.replace("PING","PONG")
            irc.send(junk)
            irc.send(junk)
            break


def main():
    irc.send(b"PRIVMS candy :!ep1\r\n")
    while 1:
        junk = b""
        junk = irc.recv(7000)
        print(junk)
        if junk.find("/")>-1:
            try:
                junk = junk.split(":")
                junk = junk[1]
                print(junk)
                nb1 = int(junk.split("/")[0])
                nb2 = int(junk.split("/")[1])
                result = round(math.sqrt(nb1)*nb2, 2)
                result = bytes(str(result)).decode("ASCII")
                irc.send("PRIVMSG "+bot+b" :!ep1 -rep "+ result+"\r\n")
                print(irc.recv(7000))
                irc.send("QUIT :By3 By3!")
                break
            except:
                print("waiting for challenge") 

server = "irc.root-me.org"
channel = b"#root-me_challenge"
bot = "candy"
port = 6667

try:
    print("[+] Creating socket")
    irc = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    print("[+] Connecting with %s:%d"%(server,port))
    irc.connect((server,port))
except:
    print("[!] Can't connect!")
else:
    print("[+] Sending nickname")
    irc.send("NICK FiftyLouis\r\n")
    print("[+] Sending USER command")
    irc.send("USER FiftyLouis irc.root-me.org root-me :ChallengeBot")
    print("[+] Join",channel)
    irc.send("JOIN" + channel)
    #print("[+] Playing PING PONG to impose our bot presence")
    #pingpong()
    print("execute main")
    main()

print("finsih")

irc.close()



