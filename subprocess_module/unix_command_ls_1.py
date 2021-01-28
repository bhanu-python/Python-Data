import subprocess
a=subprocess.run('ls -lrt /c/Users/bhanupratap.mehta/UnixPractice',shell=True) #here we are making shell=true so we can pass the command as a string else we have to pass command in list
print(a)
