#cal the diff of sum of no that are div by 6 and not div by 6 in the range of first 30 no(accenture ques)
sum1=0
sum2=0
for i in range(1,31):
    if(i%6==0):
        sum1=sum1+i
    elif(i%6!=0):
        sum2=sum2+i
diff=sum2-sum1
print(diff)
