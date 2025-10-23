
import pandas as pd
data={'Name':['ayush','bhanu','chaitanya','aryan','harshit'],'Class':['2','2','3','2','2'],'Grade':['O','B','B','A','A']}
od=pd.DataFrame(data)
print("the data that we have got: \n",od)
G=['O','A','B']
print("number 1 refers to topper and number 3 refers to average \n")
E=[]
for i in data['Grade']:
    if i in G:
        E.append(G.index(i)+1)
    else:
        pass
data['state_of_marks']= E
od=pd.DataFrame(data)    
print("after processing data: \n",od)