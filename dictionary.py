#enpity dictionary
# empity_dict={}  
# dog={'name':"bob",'bread':'no','legs':4,'age':5}
student={'f_name':'abebe',
         'l_name':'kebede',
         'gender':'male','age':20,
         'martial_status':"no",
         'skills':['java','python','javascript','nodejs','angular'],
         'country':"Ethiopa",'city':'adiss Ababa',
         'adderss':{'street_no':100,'zip_code':1000}}
#the length of the dictionary
print(len(student))
#print the values of skills
# print(student['skills'])
#the type of skills
# print(type(student['skills']))
#modify the skills values

# key_list=student.keys()
# print(key_list)
# values_list=student.values()
# print(values_list)
# changed=student.items()
# print(changed)
#delete the dictionary
# del student
#casting the dictionary in to the tuple
print(tuple(student))
print(student)
#select numeric item in a tupl
# mixed=('apple',21,56,'banana')
# numeric=tuple(item for item in mixed if isinstance(item,(int,float)))
# print(numeric)