#Ashmin Jayson S4 DS Roll No : 14
#Experiment No : 19 Probability of random variable in binomial distribution
#Date : 22/06/22

def fact(n):
    if n == 0 or n == 1:
        return 1
    
    return n * fact(n - 1)

def combi(n,r):
    return fact(n)/(fact(r)*fact(n - r))

def bnp(n, p, x):
    return combi(n, x)*(p ** x)*((1 - p) ** (n - x))

n = 6
p = 0.25

print("No of trials : ", n)
print("Probability of Success : ", p)

e4 = bnp(n, p, 4)
a1 = 1 - bnp(n, p, 0)
print("Probability of exactly 4 success : ", round(e4,4));
print("Probability of atleast 1 success : ", round(a1,4));



