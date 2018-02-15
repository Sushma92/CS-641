import numpy as np  #import numpy to do scientific computing
import numpy.linalg as linalg
wa = np.random.rand(5,5)#giving a random 5x5 mstrix
w = np.sum(wa, axis = 0)#To make the sum of columns is equal to one
g = wa/w #this is the transitional probability matrix where sum of columns is equal to one
#h = np.matrix('1;1;1;1;1')

#function which takes matrix g and returns the pagerank vector
def pageranking(a):
        m = a
        n = np.ones(len(a)) #taking nonzero approximation

        while 1e-5 < np.sum(np.abs(m - n)) : #condition for error
            m = a.dot(n) #applying the power method until the condition is satisfied
            n=m
            return m

print (pageranking(g)) #gives the eigen vector of the matrix g
