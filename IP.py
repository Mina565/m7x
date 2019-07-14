print ("\033[1;31m                                ,-. ")
print ("\033[1;31m           ___,---.__          /'|`\          __,---,___ ")
print ("\033[1;31m        ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-. ")
print ("\033[1;31m      ,'        |           ~'\     /`~           |        `. ")
print ("\033[1;31m     /      ___//              `. ,'          ,  , \___      \ ")
print ("\033[1;31m    |    ,-'   `-.__   _         |        ,    __,-'   `-.    | ")
print ("\033[1;31m    |   /          /\_  `   .    |    ,      _/\          \   | ")
print ("\033[1;31m    \  |           \ \`-.___ \   |   / ___,-'/ /           |  / ")
print ("\033[1;31m     \  \           | `._   `\\  |  //'   _,' |           /  / ")
print ("\033[1;31m      `-.\         /'  _ `---'' , . ``---' _  `\         /,-' ")
print ("\033[1;31m         ``       /     \    ,='/ \`=.    /     \       '' ")
print ("\033[1;31m                 |__   /|\_,--.,-.--,--._/|\   __| ")
print ("\033[1;31m                 /  `./  \\`\ |  |  | /,//' \,'  \ ")
print ("\033[1;31m                /   /     ||--+--|--+-/-|     \   \ ")
print ("\033[1;31m               |   |     /'\_\_\ | /_/_/`\     |   | ")
print ("\033[1;31m                \   \__, \_     `~'     _/ .__/   / ")
print ("\033[1;31m                 `-._,-'   `-._______,-'   `-._,-' ")




import socket
import sys

#this script coded by: Mina7x

print('Coded By Mina7x')
print ('Enter Your DNSOr Target: ')
hostname = input()
ip=socket.gethostbyname(hostname)
print ('Host Name Is: ',hostname, '\n' 'Target Ip Is: ',ip)
