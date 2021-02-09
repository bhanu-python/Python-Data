from datetime import datetime

mytime=datetime(2021,2,18,13,26,45) #it will give date + time

print(mytime)

#if i haved to replayce the year

print(mytime.replace(year=2020))

#perform airthmetic operation with date
#real life you want to know total  time spend in office  login and logout

login=datetime(2021,2,18,13,26,45)
logout=datetime(2021,2,19,7,0,0)
spend=logout-login

print(type(spend))
print(spend)

