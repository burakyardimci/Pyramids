with open("map1.txt","r") as file:
    list=[]
    for line in file:
        stripped=line.strip()
        splitted=stripped.split(" ")
        list.append(splitted)
    a=[]
    b=[]
    for element in range(len(list)):
        for char in range(len(list)):
            if list[element][char]>list[element][char-1] and list[element][char]>list[element][char+1]:
                if list[element][char]>list[element-1][char] and list[element][char]>list[element-1][char]:
                    a.append(list[element][char])
                    b.append(list[element][char])
                    a.append(element)
                    a.append(char)
    x=len(b)
    toplam=[]
    for karakter in b:
        toplam.append((int(karakter)))
    c=sum(toplam)
    print("",a[:3],"\n",a[3:6],"\n",a[6:9],"\n",a[9:12])
    print(f" average height: {c/x}m")





