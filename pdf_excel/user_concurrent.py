#read fil line by line and strore in list 

import subprocess
import csv

with open('user.txt','w') as files:
    p1=subprocess.run(['grep','-oP',"'(?<=userList=).*(?=;)'",'concurrent_user_incident.log'],text=True,stdout=files) #userlist
    #p2=subprocess.run(['tr','-d',"';'"],text=True,input=p1.stdout,stdout=files)
with open('max.txt','w') as f1:
    p3=subprocess.run(['grep','-oP',"'(?<=maxUserCount=).*?(?=,)'",'concurrent_user_incident.log'],text=True,stdout=f1) #maximum user
with open('date.txt','w') as f2:    
    p4=subprocess.run(['grep','-oP',"'(?<=startTime=).*?(?=,)'",'concurrent_user_incident.log'],text=True,stdout=f2) #date


#storing the file in list format

with open('user.txt','r') as f, open('max.txt','r' ) as f3, open('date.txt','r') as f4:
    users=f.read().splitlines()
    maxs=f3.read().splitlines()
    dates=f4.read().splitlines()
    excep=[ ]
    for i in maxs:
        if int(i) > 15:
            excep.append('User exceeded')
        else:
            excep.append('user not exceede')
    for j in range(0,len(users)):
        datas=list(zip(dates,excep,maxs,users))
    
    file_out=open('concurent_user.csv',encoding='utf-8',mode='w+',newline='')
    csv_writer=csv.writer(file_out,delimiter=',')
    for k in datas:
        csv_writer.writerow(k)
    
    
        

    


   
    
