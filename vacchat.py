# Author: Arrow6
# Version: 1.2

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
    print "My ip = " + socket.gethostbyname(socket.gethostname())
    print seperator
    afc()


def newContact():
    f = open("contact.contacts", "w")

    f.write(contacts + "\n")
    f.write("{\n" + "[" + raw_input("") + "]\n")
    f.write("[" + raw_input() + "]\n")
    f.write("[" + input() + "]\n}")


def newParty():
    server(myhost, myport)
    print seperator
    afc()


def joinParty():
    print "type -contacts to see all your Contacts"

    host = raw_input("Party's IP address: ")
    port = input("Party's port: ")
    try:
        client(host, port)
    except:
        print "Conection Failed"
        command = raw_input("Do you want to retry? ")
        if command.upper() == "YES":
            joinParty()
        else:
            print seperator
            afc()


def settings():
    f = open("settings.settings", "w")

    #f.write()
    f.close()
    print "To change the default port type -port"

    command = raw_input("-> ")

    if command == "port":
        global port
        port = input("New port: ")
    afc()


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
    s.close()
    afc()


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

    afc()


def afc():
    print "Open a new party by typing -new party."
    print "Join a party by typing -join party."
    print "Call a friend by typing -call."
    print "Change settings by typing -settings."
    print "To get your IP address type -IP"
    print seperator

    command = raw_input("-> ").upper()

    if command == "NEW PARTY":
        newParty()
    elif command == "JOIN PARTY":
        joinParty()
    elif command == "SETTINGS":
        settings()
    elif command == "EXIT":
        sys.exit()
    elif command == "IP":
        printIp()
    else:
        afc()


def run():
    afc()


run()
