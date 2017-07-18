#coding: utf-8from math import sqrt
abc = {14:[1.68,1.24,1.4],34:[1.92,1.07,1.53],46:[1.44,1.056,1.278]}
def multipl(a,b): sumofab=0.0 for i in range(len(a)):  temp=a[i]*b[i]  sumofab+=temp return sumofab
 
def corrcoef(x,y): n=len(x)
    #求和 sum1=sum(x) sum2=sum(y)
    #求乘积之和 sumofxy=multipl(x,y)
    #求平方和 sumofx2 = sum([pow(i,2) for i in x]) sumofy2 = sum([pow(j,2) for j in y]) num=sumofxy-(float(sum1)*float(sum2)/n)
    #计算皮尔逊相关系数 den=sqrt((sumofx2-float(sum1**2)/n)*(sumofy2-float(sum2**2)/n)) return num/den
result = {}for person1 in abc: distances = [] for person2 in abc:  if person1 != person2:   # print "p1,p2:",person1,person2   dist = corrcoef(abc[person1], abc[person2])   d = {}   d[person2] = dist   # print "dist:",dist    distances.append(d) result[person1] = distances
print result

