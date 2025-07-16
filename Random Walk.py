import random 
xn = 0 
exn = 0 #EXPECTATION 
n = 10**7 #SAMPLE SPACE
l = 0 #LEFT COUNTER
r = 0 #RIGHT COUNTER
p_l = 0 #PROBABILITY OF MOVING LEFT
p_r = 0 #PROBABILITY OF MOVING RIGHT 
for i in range(n):
    
    z = random.randint(1,2) #GENERATING 1 OR 2 RANDOMLY 
    
    #RANDOMLY WALKING LEFT OR RIGHT IF EITHER 1 OR 2 IS GENERATED RESPECTIVELY
    if z == 1:
        l += 1 #IF Z WAS 1, WE INCREMENT THIS VARIABLE 
        xn -= 1 #HERE WE MAKE THE PARTICLE MOVE TO THE LEFT
    else:
        r += 1 #IF Z WAS 2, WE INCREMENT THIS VARIABLE
        xn += 1 #HERE WE MAKE THE PARTICLE MOVE TO THE RIGHT

p_l = l / n 
p_r = 1 - p_l 

exn = (-1)*p_l + (1)*p_r #ESTIMATING EXPECTATION THAT IS '(-1)p + (1)(p-1)' WHERE 'p' IS THE PROBABILITY

var_x = 4*p_l - 4*p_l**2 #CALCULATING VARIANCE OF THE PARTICLE THAT IS E[x^2] - E[x]^2 OR '4^p - 4*(p)^2' where E[x] IS EXPECTATION AND 'p' IS THE PROBABILITY

#EXPECTED VALUE
print(f"\nThe expected position(Xn) of particle after walking randomly for {n} steps is {xn} and the expectation(E[x]) is {exn}\n")  

#VARIANCE
print(f"The variance[Var(x)] for the particle is {var_x}\n")