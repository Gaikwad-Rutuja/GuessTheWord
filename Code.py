import random
class Word():
    def __init__(self,word3,word4,word5):
        self.word3=word3                      
        self.word4=word4
        self.word5=word5
    def list(self):
        self.word3=["CAT","DOG","THE","SUN","GOD","LEG","PIN","OWL"]
        self.word4=["LOGO","PINK","COOL","AREA","ACID","DESK","DOWN","MOON"]
        self.word5=["ADULT","HEART","ISSUE","LIMIT","SOUND","JERRY","STUMP","CARRY","RAISE"]
        letter =int(input(print("Enter the numbers of letters in the word (3/4/5)")))
        if(letter==3):
            word = random.choice(self.word3)
            correct = word
            n = len(word) #n stores the length of the string 
            li = list(word) #since string is immutable, 
                 #we make a list of the characters of the string 
            for i in range(0,n-1): #i is iterated from 0 to n-2
                pos = random.randint(i+1,n-1) #this function randint will produce a 
                               #random number ranging between i+1 and n-1
                li[pos],li[i] = li[i],li[pos] #exchanging li[pos] and li[i]
    
                res = "" 
            for i in range(n):
                res = res + li[i] #sequentially add the charters of the list 
                         #to the string
            print("Letters Are - ",res)
            ans=input("Enter your answer - ")
            if(ans==correct):
                print("Great!!Keep Going")
            else:
                print("OOPs! Try Something Different")
                print("The Correct Is - ",correct)
        elif(letter==4):
            word = random.choice(self.word4)
            correct = word
            n = len(word) #n stores the length of the string 
            li = list(word) #since string is immutable, 
                 #we make a list of the characters of the string 
            for i in range(0,n-1): #i is iterated from 0 to n-2
                pos = random.randint(i+1,n-1) #this function randint will produce a 
                               #random number ranging between i+1 and n-1
                li[pos],li[i] = li[i],li[pos] #exchanging li[pos] and li[i]
    
                res = "" 
            for i in range(n):
                res = res + li[i] #sequentially add the charters of the list 
                         #to the string
            print(res)
            ans=input("Enter your answer - ")
            if(ans==correct):
                print("Great!!Keep Going")
            else:
                print("OOPs! Try Something Different")
                print("The Correct Is - ",correct)
            
        elif(letter==5):
            word = random.choice(self.word5)
            correct = word
            n = len(word) #n stores the length of the string 
            li = list(word) #since string is immutable, 
                 #we make a list of the characters of the string 
            for i in range(0,n-1): #i is iterated from 0 to n-2
                pos = random.randint(i+1,n-1) #this function randint will produce a 
                               #random number ranging between i+1 and n-1
                li[pos],li[i] = li[i],li[pos] #exchanging li[pos] and li[i]
    
                res = "" 
            for i in range(n):
                res = res + li[i] #sequentially add the charters of the list 
                         #to the string
            print(res)
            ans=input("Enter your answer - \n")
            if(ans==correct):
                print("Great!!Keep Going\n")
            else:
                print("OOPs! Try Something Different")
                print("The Correct Is - ",correct)
        
            
obj=Word(0,0,0)
print("***WELCOME TO THE GAME***\n")
obj.list()
choice=int(input("Want to continue \n Enter 1 for YES \n Enter 2 for NO "))
while(choice==1):
    obj.list()
    choice=int(input("Want to continue \n Enter 1 for YES \n Enter 2 for NO "))




