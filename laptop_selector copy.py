import pandas as pd
data=pd.read_csv("laptop.csv")

import csv
f=open("laptop.csv","r")
creader = csv.reader(f)
f2=open("Available_Laptops.csv","w")
cwriter=csv.writer(f2)


def Select():
    price = int(input("Enter the max price you wish to spend on the laptop (in Euros)"))
    
    type = int(input("Enter what kind of laptop you would like.\n 1--> Notebook \n 2--> Gaming, \n 3--> Ultrabook, \n 4--> 2 in 1 Convertible. \n"))
    
    if type ==1:
        t="Notebook"
    elif type==2:
        t="Gaming"
    elif type==3:
        t="Ultrabook"
    elif type==4:
        t="2 in 1 Convertible"
    
    size = int(input("Enter max screen size of your laptop that you would like. \n 1-->10-13 inches \n 2-->13-16 inches \n 3--> 16 or more inches \n"))
    
    if size==1:
        l=0
        m=13
    elif size==2:
        l=13
        m=16
    elif size==3:
        l=16  
        m=10000
    
    cpu = int(input("Enter your preferred CPU company. \n 1-->Intel \n 2--> AMD \n 3-->Samsung \n"))
    
    if cpu==1:
        c="Intel"
    elif cpu==2:
        c="AMD"
    elif cpu==3:
        c="Samsung"
    
    ram = int(input("Enter your preferred RAM storage (out of 2,4,6,8,12,16,24,32,64). \n"))
    
    if ram!=1:
        r=ram
    
    gpu = int(input("Enter if you have any preferred GPU company. \n 1-->Intel \n 2-->AMD \n 3-->Nvidia\n4--> ARM\n"))
    
    if gpu==1:
        g="Intel"
    elif gpu==2:
        g="AMD"
    elif gpu==3:
        g="Nvidia"
    elif gpu==4:
        g="ARM"
    
    os = int(input("Enter your preferred OS.\n 1--> Windows \n 2--> macOS \n 3--> Chrome OS \n 4--> Android \n 5--> Linux \n 6--> No OS \n"))
    
    if os==1:
        o="Windows"
    elif os==2:
        o="macOS"
    elif os==3:
        o="Chrome OS"
    elif os==4:
        o="Android"
    elif os==5:
        o="Linux"
    elif os==6:
        o="No OS"
    
    weight = int(input("Enter your preferred weight for the laptop.\n1-->0-3kg. \n 2--> 3-4 kg. \n 3--> 4+ kg \n"))
    
    if weight==1:
        wm=3
        wl=0
    elif weight==2:
        wm=4
        wl=3
    elif weight==3:
        wl=4
        wm=55
    for i in creader:
        if (float(i[-1])<=price) and (i[2]==t) and (float(i[3])>=l and float(i[3])<=m) and (i[5]==c) and (int(i[8])==r) and (i[10]==g) and (i[12]==o) and (float(i[13])>=wl and float(i[13])<=wm):
            print(i)
            cwriter.writerow(i)
        else:
            continue
Select()
d2=pd.read_csv("Available_Laptops.csv")
print(d2)
