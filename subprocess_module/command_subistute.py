import subprocess
p1=subprocess.run(['cat','output.txt'],capture_output=True,text=True)
p2=subprocess.run(['grep','-in', 'output'],capture_output=True, text=True, input=p1.stdout)
print(p2.stdout)
