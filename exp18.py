#Ashmin Jayson S4 DS Roll No : 14
#Experiment No : 20 Probability of random variable in poisson distribution
#Date : 22/06/22

def fact(n):
    if n == 1 or n == 0 :
        return 1
    
    return n * fact(n - 1)

def p(x, m):
    return round(((e ** -m)*(m ** x))/fact(x), 3)


mean = 3.4
x = 6
e = 2.7183


print("The mean of the distribution is : ", mean)
print("The required number of trials is : ", x)
print("The probability of P(X = 6) is : ", p(x, mean))


