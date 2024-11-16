student_data= {

'id1':{
    'name':['Karim'],
    'class':['8'],
    'subject_integration':['sports,english,math']

},

'id2':{
    'name':['Ahmed'],
    'class':['9'],
    'subject_integration':['science,english,math']

},

'id3':{
    'name':['Sara'],
    'class':['10'],
    'subject_integration':['arabic,english,math']

},
}



result= {} 

for key, value in student_data.items():
 if value not in result.values():
  result[key]= value
print(result)



 
 
 
          