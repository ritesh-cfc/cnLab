from os import system as sys

sys("ifconfig")
sys("sudo ifconfig eth0 down")
sys("sudo ifconfig eth0 192.168.41.33") #original ip is 192.168.43.130
sys("sudo idconig eth0 up")
