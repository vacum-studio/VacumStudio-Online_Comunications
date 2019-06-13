# Author: Arrow6
# Version: 1.1
# Errors: on getContactData(Cn)
import socket

import sys

seperator = "--------------------------------------------------------------"
myhost = "127.0.0.1"
myport = 8080


def loadContacts():
    return open("contact.contacts", "r").read()


contacts = loadContacts()


def getContactData(Cn):
    found = False
    contact = open("contact.contacts", "r")

    while found is not False:
        read = contact.readline()
        if read == "{":
            read = contact.readline()
            if read[1] == "[":
                contactname = read[1:-1]
                if contactname == Cn:
                    found = True
                    return contact.readline()[1:-1], int(contact.readline()[1:-1])
        if read == "}":
            continue


def writeIpFile():
    f = open("IP.ip", "w")
    f.write(socket.gethostbyname(socket.getfqdn()))
    f.close()


def printIp():
    print "My ip = " + socket.gethostbyname(socket.getfqdn())


def newContact():
    f = open("contact.contacts", "w")

    f.write(contacts + "\n")
    f.write("{\n" + "[" + raw_input("") + "]\n")
    f.write("[" + raw_input() + "]\n")
    f.write("[" + input() + "]\n}")


def newParty():
    server(myhost, myport)


def joinParty():
    print "type -contacts to see all your Contacts"

    host = raw_input("Party's IP address: ")
    port = input("Party's port: ")
    client(host, port)


def settings():
    f = open("settings.settings", "w")

    f.write()


def server(host, port):
    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    a = 0
    print "Connection found from" + str(addr)
    while a < 500:
        a += 1
        data = c.recv(1024)
        d = data
        if not d:
            break
        print "from user:" + str(d)
        send = raw_input("-> ")
        #print "sending to user:" + str(data)
        c.send(send)
    c.close()
    sys.exit(0)


def client(host, port):
#    host = "127.0.0.1"
#    port = 6000

    s = socket.socket()
    s.connect((host, port))

    message = raw_input("-> ")
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        print "Server-> " + str(data)
        message = raw_input("->")
    s.close()


def afc():
    print "Open a new party by typing -new party."
    print "Join a party by typing -join party."
    print "Call a friend by typing -call."
    print "Change settings by typing -settings."
    print seperator


def run():
    afc()


run()
