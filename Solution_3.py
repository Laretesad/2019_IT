import numpy as np
import math

def create_indices (N,batches,split_ratio):
    test_size=(N-1)//(batches+(1/split_ratio))
    if ((N-1)%(batches+(1/split_ratio))==0):
        test_size-=1
    test_size+=1
    start_test_data,start_test,end_test=0,0,0
    for i in range (batches):
        start_test=start_test_data+ test_size*(1/split_ratio)
        end_test=start_test+test_size
        if end_test<=N:
            yield list(map(math.floor,[start_test_data,start_test,end_test]))
        else :
            k=end_test-N
            yield list(map(math.floor,[start_test_data,start_test,end_test]))
        start_test_data+=test_size

test_gen = create_indices(100, 5, 0.2)

for indices in test_gen:
    print(indices)