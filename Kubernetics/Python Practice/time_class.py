class Time():
    def __init__(self,hour,mint):
        self.hour=hour
        self.mint=mint
    
    def add_time(self,t1,t2):
        t3=t1+t2
        return f'{int(t3/60)} hour and {t3 % 60} minute'
    def minute(self):
        return self.hour * 60 + self.mint

   # hour=int(input('enter the hour')) 
   # mint=int(input('enter the minute'))
    
time=Time(4,20) 
t1=time.minute()
print('Total minute:{}'.format(t1))
time=Time(3,10)
t2=time.minute()
print('Total minute:{}'.format(t2))
total=time.add_time(t1,t2)
print(total)

