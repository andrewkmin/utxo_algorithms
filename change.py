# Andrew Min
# Programming Blockchain Scholarship Application
# Note: python 3.6.1

import sys
from utxos import utxos

# EDGE CASES: 
# non-valid UTXOS: assume all are valid, 
# ties: pick any valid range, 
# insufficient funds: print error message,
# sending amount <= 0: assume this won't happen

def find_range(utxos, value) :
    # flag indicating whether we have a valid solution (i.e. one that doesn't result in negative change)
    flag = False

    # dictionary that maps from range of utxo indices to resulting amount of change
    memo = {}

    # total sum across all utxos
    total_sum = 0

    i = 0
    while (i < len(utxos)) :
        # sum for current range
        sum = 0

        total_sum += utxos[i]["val"]

        # variable used to denote the index at which our date range ends
        temp = 0

        j = i 
        while (j < len(utxos)) :
            if (sum < value) :
                sum += utxos[j]["val"]
            else :
                temp = j - 1
                break
            j += 1

        temp = j - 1
        range_str = str(i) + ":" + str(temp)
        change = sum - value

        if (change >= 0) :
            flag = True
            memo[range_str] = change
        else :
            # allowing negative change is not allowed and would make sorting 
            # from least to greatest amount of change difficult. 
            # instead, arbitrarily put max int
            memo[range_str] = sys.maxsize

        i += 1

    if (flag) :
        # sort by change from least to greatest
        sorted_by_value = sorted(memo.items(), key=lambda kv: kv[1])

        result = sorted_by_value[0][0].split(":")
        num_utxos = int(result[1]) - int(result[0]) + 1
        beginning = utxos[int(result[0])]["date"]
        end = utxos[int(result[1])]["date"]
        elapsed_time = end - beginning
        change = sorted_by_value[0][1]

        print("---------------------")
        print ("Start date:", beginning)
        print ("End date:", end)
        print ("Amount change:", change)
        print ("Time elapsed:", elapsed_time)
        print("---------------------")
        print("DETAILS -- ")
        print ("Net amount sent:", value)
        print ("# UTXOs included:", num_utxos)
        print ("UTXO(s):", utxos[int(result[0]) : int(result[1]) + 1])
        
    else :
        print("ERROR: INSUFFICIENT FUNDS")
        print("---------------------")
        print("Amount owned:", total_sum)
        print("Desired send amount:", value)

find_range(utxos, 81)