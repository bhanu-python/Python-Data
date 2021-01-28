import csv

#open csv file

f=open('pyexcel.csv')

#f=open('pyexcel.csv',encoding='utf-8')

#read csv file

data=csv.reader(f)

#reformating csv file to pythn object if fil contans the special charecter then it will get error for that ypu have to use ecncoding key word with file encoding

data_line=list(data)

l=len(data_line)

for i in data_line:
    print(i)

data_line.append(['Rakhi','10','10'])


file_out=open('concurent_user.csv',mode='w',newline='\n')
csv_writer=csv.writer(file_out,delimiter=',')

for i in data_line:
    csv_writer.writerow(i)


