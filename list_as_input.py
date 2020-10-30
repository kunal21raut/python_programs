lst=[]
dict={}
name=str(input())
for i in range(0,3):
    ele=int(input())
    lst.append(ele)
for k in lst:
    print(k)
dict["name"]=name
dict["marks"]=lst
print(dict)

