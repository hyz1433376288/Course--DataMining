import numpy as np
import itertools #组合
with open('data.in', 'r') as f:
    len_R = 7
    len_C = 10 + 1
    MIN_SUP = 4
    origin_data = f.readlines()
    matrix_data = np.zeros((len_R, len_C))
    list_data = []
    print(matrix_data)
    r = 0
    for ld in origin_data:
        vec = [int(x) for x in ld[0:-1].split('\t')]
        vec = sorted(vec)
        list_data.append(vec)
        for v in vec:
            matrix_data[r, v] = 1
        print(vec)
        r += 1

    '''
    calculate frequence 1 item 
    '''
    freq1 = {}
    list_freq1 = {}
    for i in range(len_R):
        for j in range(len_C):
            if matrix_data[i, j] == 1:
                j = tuple([j])
                if j in freq1.keys():
                    freq1[j] += 1
                else:
                    freq1[j] = 1
    for key in list(freq1.keys()):
        if freq1[key] < MIN_SUP:
            del freq1[key]
    print("frequent 1 itemsets",freq1)
    for k in freq1:
        key = k[0]
        if key in list_freq1.keys():
            list_freq1[key] += 1
        else:
            list_freq1[key] = 1

    '''
        calculate frequence 2 item 
    '''
    freq2 = {}
    for pending_freq2 in itertools.combinations(list_freq1.keys(), 2):
        for ld in list_data:
            if set(pending_freq2).issubset(tuple(ld)):
                if pending_freq2 in freq2.keys():
                    freq2[pending_freq2] += 1
                else:
                    freq2[pending_freq2] = 1
    for key in list(freq2.keys()):
        if freq2[key] < MIN_SUP:
            del freq2[key]
    print("frequent 2 itemsets",freq2)

    '''
        calculate frequence 3 item 
    '''
    freq3 = {}
    for freq2_key in freq2:
        for freq1_key in freq1:
            if not set(freq1_key).issubset(freq2_key):
                pending_freq3 = freq2_key + freq1_key # tuple3 = tuple2 + tuple1
                pending_freq3 = tuple(sorted(pending_freq3))# sorted the pending-key to duplicate removal , because the pending-key may appear as an another ordership before

                if pending_freq3 in freq3.keys():
                    continue

                for ld in list_data:
                    if set(pending_freq3).issubset(tuple(ld)):
                        if pending_freq3 in freq3.keys():
                            freq3[pending_freq3] += 1
                        else:
                            freq3[pending_freq3] = 1
    for key in list(freq3.keys()):
        if freq3[key] < MIN_SUP:
            del freq3[key]
    print("frequent 3 itemsets",freq3)
