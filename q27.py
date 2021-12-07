list_elements =[1,1,1,2,3,4,5,6,6,7,7]
unique_elements=[]
for x in list_elements: 
    if x not in unique_elements: 
        unique_elements.append(x)
for x in unique_elements:
    print(x)
