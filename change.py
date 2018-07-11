import sys

utxos = [
    {
        "val": 2,
        "date": 5
    },
    {
        "val": 5,
        "date": 9
    },
    {
        "val": 9,
        "date": 10
    },
    {
        "val": 24,
        "date": 11
    },
    {
        "val": 12,
        "date": 12
    }
]

# note: python 3.6.1
# edge cases: non-valid UTXOS, ties
def calc_change(utxos, value) :
    # remainder = value

    # have some kind of flag here 
    flag = False
    memo = {}
    i = 0
    while (i < len(utxos)) :
        sum = 0
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
        some_str = str(i) + ":" + str(temp)


        storage = sum - value
        # remainder
        if (storage >= 0) :
            flag = True
            memo[some_str] = storage
        else :
            memo[some_str] = sys.maxsize
        i += 1

    if (flag) :
        sorted_by_value = sorted(memo.items(), key=lambda kv: kv[1])
        print('sorted_by_value', sorted_by_value)
        result = sorted_by_value[0][0].split(":")
        num_utxos = int(result[1]) - int(result[0]) + 1
        beginning = utxos[int(result[0])]["date"]
        end = utxos[int(result[1])]["date"]
        elapsed_time = end - beginning
        change = sorted_by_value[0][1]

        print ('Amount sent:', value)
        print ('Change:', change)
        print ('# UTXOs included:', num_utxos)
        print ('Range start:', beginning)
        print ('Range end:', end)
        print ('Time elapsed:', elapsed_time)


        print(type(utxos))
        # check for all negatives
        # tie_breaker(sorted_by_value)
        
    else :
        print("Insufficient funds.")

def tie_breaker(sorted_by_value) :
    i = 0
    tiebreaker = []
    min_change = sorted_by_value[0][1]

    while (i < len(sorted_by_value)) :
        # avoid non-min change date-ranges
        if (min_change != sorted_by_value[i][1]) :
            break
        else :
            tiebreaker.append(sorted_by_value[i])
        # increment
        i += 1

    print(tiebreaker)

    diff = sys.maxsize
    tracker = tiebreaker[0]
    for x in tiebreaker : 
        min_range = x[0]
        print('min range', min_range)
        range_arr = min_range.split(":")
        temp = int(range_arr[1]) - int(range_arr[0]) 

        if (temp <= diff) : 
            diff = temp
            tracker = list(map(int, range_arr))

    print ('# UTXOs included:', diff + 1)
    print ('Change:', min_change)
    print ('Beginning:', utxos[tracker[0]]["date"])
    print ('End:', utxos[tracker[1]]["date"])
    print ('Time elapsed:', utxos[tracker[1]]["date"] - utxos[tracker[0]]["date"])

print(utxos)
# utxos.sort(key=lambda x: x["val"], reverse=True)
calc_change(utxos, 51)

# assumptions: all utxos in a date range must be used -- crucial
# utxos come presorted in order of date
# strategy: start at beginning/end of list of utxos;