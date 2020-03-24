n=input()
count1=0
count2=0
for i in n:
    if i == '1':
        count1+=1
        count2=0
        if count1 == 6 or count2 == 6:
            print('Sorry, sorry!')
            exit()
    else:
        count1=0
        count2+=1
        if count1 == 6 or count2 == 6:
            print('Sorry, sorry!')
            exit()
print('Good luck!')
