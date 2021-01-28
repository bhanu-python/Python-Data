import subprocess
with open("output.txt",'w') as f:
    a=subprocess.run('ls -lrt', stdout=f, shell=True)
    
