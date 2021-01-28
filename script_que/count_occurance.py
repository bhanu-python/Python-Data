st='aaa bbbbb cccccc'
b=set()
for i in st:
    a=str(st.count(i))

    if i == ' ':
        continue
    b.add(str(i+a))
for j in b:
    print(j,end='')
