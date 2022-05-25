import numpy as np
import random
def additional_vector(X):
    a = np.empty((X.shape[0],))
    a[::2] = 0
    a[1::2] = 1
    
    #a is the list of alternaxtin 1 and 0
    return np.column_stack((X,np.array(a)))
