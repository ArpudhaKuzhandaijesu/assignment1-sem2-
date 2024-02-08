#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter the number of student:"))
print("1.tamil\n2.english\n3.science\n4.social\n5.maths")
if n>0:
    for i in range(1,n+1):
        name=input("enter student name:")
        tam=int(input("enter tamil mark:"))
        eng=int(input("enter english mark:"))
        science=int(input("enter science mark:"))
        social=int(input("enter social mark:"))
        maths=int(input("enter maths mark:"))
        percent=(tam+eng+science+social+maths)/5
        print("name:",name,"\ntamil:",tam,"\nenglish:",eng,"\nscience:",science,"\nsocial:",social,"\nmaths:",maths,"\ngrade:",percent,"%")
        if percent<=100 and percent>=90:
            print("grade=O")
        elif percent<=89 and percent>=80:
            print("grade=A+")
        elif percent<=79 and percent>=70:
            print("grade=A")
        elif percent<=69 and percent>=60:
            print("grade=B+")
        elif percent<=59 and percent>=50:
            print("grade=B")
        elif percent<=49 and percent>=40:
            print("grade=c+")
        elif percent<=39 and percent>=35:
            print("grade=C")
        else:
            print("grade=u")
else:
    print("the number of students is given less than 1 , give the correct value")


# In[ ]:




