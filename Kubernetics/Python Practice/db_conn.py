import cx_Oracle
import csv

#dsn_test=cx_Oracle.makedsn('localhost','1521',service_name='Bhanu')
cx_Oracle.init_oracle_client(lib_dir=r'D:\app\Bhanupratap.Mehta\product\12.2.0\dbhome_2\instantclient_12_2')
conn=cx_Oracle.connect('hr/bhanu1231@localhost:1521/Bhanu')
cur=conn.cursor()
cur.execute('select employee_id,first_name from employees')

employee_id=['EMPLOYEE_ID']
first_name=['FIRST_NAME']

for a,b in cur:
    employee_id.append(a)
    first_name.append(b)

data=list(zip(employee_id,first_name))
    
fcsv= open("data_abhi.csv",mode="w+",newline='')
wcsv=csv.writer(fcsv,delimiter=",")

for i in data:
    wcsv.writerow(i)

    
    