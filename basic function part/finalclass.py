import xlrd
import numpy as np
import col_maxfre
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.cross_validation import train_test_split  

data = xlrd.open_workbook('C:\\Users\\Spock\\Desktop\\final\\SkillCraft1_Dataset.xls')
table = data.sheets()[0]   
print(table)  

va=19
Newt=[[] for i in range(va)]
for i in range(1,20):
    Newt[i-1]=table.col_values(i)
    Newt[i-1].remove(Newt[i-1][0])
#print(Newt)


'''clean
'''

for col in Newt: 
    maxf=""
    for i in range(0,len(col)):
        if (col[i]=="?" and maxf==""):
                col[i]=col_maxfre.col_maxfre(col)
        if (col[i]=="?" and maxf!=""): 
                col[i]=maxf
    print(col)


'''
    classification
'''
for i in range(0,len(Newt[0])):
    if (Newt[0][i]<=2): Newt[0][i]=0
    elif(Newt[0][i]<6 and Newt[0][i]>2): Newt[0][i]=1
    elif(Newt[0][i]<8 and Newt[0][i]>=6): Newt[0][i]=2
    elif(Newt[0][i]==8):Newt[0][i]=3

x=np.array(Newt[1:len(Newt)])  
y=np.array(Newt[0])
#x.shape=(3395,len(Newt)-1)
x=np.transpose(x)
print(len(x)); print(len(y));


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

print(x_train)  
print(x_test)  
modle=RandomForestClassifier(n_jobs=1000)
print(modle)
modle.fit(x_train, y_train)    
#joblib.dump(modle, "train_model.m")

answer = modle.predict(x_test)  

#print(answer)
#print(y_test)
print(np.mean( answer == y_test)) 


'''
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)  
modle=AdaBoostClassifier(n_estimators=100,learning_rate=0.001)
modle.fit(x_train, y_train)  
#joblib.dump(modle, "train_model.m")

#print(modle)
answer = modle.predict(x_test)  
print(answer)
print(y_test)
print(np.mean( answer == y_test)) 
'''


cou=[0 for i in range(4)]
dic={}
for i in range(len(answer)):
    if y_test[i] in dic:
        dic[y_test[i]]=dic[y_test[i]]+1
    else: dic[y_test[i]]=1
    
    if answer[i]==y_test[i]:
        cou[answer[i]]=cou[answer[i]]+1

print(cou)
print(dic)
for i in range(len(cou)):
    if i in dic:
        print(float(cou[i])/float(dic[i]))


