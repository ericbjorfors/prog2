import random
import numpy as np
import matplotlib.pyplot as plt
import math
import concurrent.futures as future
import time
from time import perf_counter as pc





def appr_pi(n):
    in_circ = 0
    cor_ilist = []
    cor_olist = []
    
    for _ in range(n):
        cor = [random.uniform(-1, 1) for _ in range(2)]
        if np.sqrt(cor[0]**2 + cor[1]**2) <= 1:
            in_circ += 1
            cor_ilist.append(cor)
        else:
            cor_olist.append(cor)
    
    cor_ilist = np.array(cor_ilist)
    cor_olist = np.array(cor_olist)
    
    plt.scatter(cor_ilist[:, 0], cor_ilist[:, 1], color='red', label='Inside Circle', s=5)
    plt.scatter(cor_olist[:, 0], cor_olist[:, 1], color='blue', label='Outside Circle', s=5)
    plt.legend()
    plt.axis('equal')  # Set the aspect ratio to make it a circle
    plt.show()
    
    return 4 * (in_circ / n)

# for i in [10**x for x in range(3, 6)]:
#     print(appr_pi(i))


def appr_vol(n,d):
    start = pc()
    in_hsphere = 0
    
    for i in range(n):
        cor = [random.uniform(-1,1) for _ in range(d)]
        if sum(list(map(lambda x: x**2 , cor))) <= 1:
            in_hsphere += 1
    V = 2**d*(in_hsphere/n)
    V_exact = (np.pi**(d/2))/math.gamma(d/2+1)
    end = pc()
    t = end-start
    return (V, V_exact,t)
#print(appr_vol(100000,2)) #(3.14992, 3.141592653589793, 0.5572315830000001)

#print(appr_vol(100000,11)) #(1.80224, 1.8841038793898994, 2.0678888330000005)




def _appr_vol(args):
    n = args[0]
    d = args[1]
    in_hsphere = 0
    try:
        for i in range(n):
            cor = [random.uniform(-1,1) for _ in range(d)]
            if sum(list(map(lambda x: x**2 , cor))) <= 1:
                in_hsphere += 1
    except ValueError:
        raise ValueError('')
    return in_hsphere

def appr_vol_parallell(n,d,p):
    
    start = pc()
    tries = [[round(n/p),d] for _ in range(p)]
    
    with future.ProcessPoolExecutor() as ex:  
        results = list(ex.map(_appr_vol, tries))
    V = 2**d*(sum(results)/n)
    V_exact = (np.pi**(d/2))/math.gamma(d/2+1)
    end = pc()
    t = end-start
    return (V, V_exact,t)

def main():
    # Your main code goes here
    for i in [10**x for x in range(3, 6)]:
        print(appr_pi(i))
    print(appr_vol(1000000,11))
    print(appr_vol_parallell(100000,11,10))
    #(1.8436096, 1.8841038793898994, 211.970472333)
    #(1.886208, 1.8841038793898994, 9.342677667000004)
    pass
   
if __name__ == "__main__":
    main()



