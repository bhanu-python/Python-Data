import zipfile

#zip the individual files

#here we created two files

f1=open('file_one.txt','w+')
f1.write('file one')
f1.close()

f2=open('file_two.txt','w+')
f2.write('file two')
f2.close()

#now we are compressing the file

comp_f=zipfile.ZipFile('test_z.zip','w')
comp_f.write('file_one.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_f.write('file_two.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_f.close()

#unzip the file

comp_unz=zipfile.ZipFile('test_z.zip','r')
#comp_unz.extract() if i want any specefic file
comp_unz.extractall('extract_cont')  # it will extract all the files inside extrac_cont
