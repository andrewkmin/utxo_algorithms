utxos = [
    {
        "val": 2,
        "date": 1
    },
    {
        "val": 4,
        "date": 2
    },
    {
        "val": 6,
        "date": 3
    },
    {
        "val": 8,
        "date": 4
    },
    {
        "val": 10,
        "date": 5
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
        remainder = value
        temp = 0

        j = i 
        while (j < len(utxos)) :
            if (utxos[j]["val"] <= remainder) :
                flag = True
                remainder -= utxos[j]["val"]
            else :
                temp = j - 1
                break

            j += 1

        temp = j - 1
        some_str = str(i) + ":" + str(temp)
        memo[some_str] = remainder
        i += 1

    if (flag) :
        sorted_by_value = sorted(memo.items(), key=lambda kv: kv[1])
        tie_breaker(sorted_by_value)
        
    else :
        print("No valid utxos")

def tie_breaker(sorted_by_value) :
    print("yo", sorted_by_value)
    # do tie-breakers here in case change is equal
    i = 0
    tiebreaker = set()

    # alternative method (to prevent duplicate additions to set): 
    # keep track of min change. add all entries with that same min change. when 
    # you reach one with a different min change (aka a greater one), stop
    while (i < len(sorted_by_value)) :
            # if we reached the end of the range
            if ((i+1) == len(sorted_by_value)) : 
                break
            elif (sorted_by_value[i][1] == sorted_by_value[i+1][1]) :
                # if consecutive 
                tiebreaker.add(sorted_by_value[i])
                tiebreaker.add(sorted_by_value[i+1])

            # increment
            i += 1

        # store amount change separately so we can 
        # create a new dictionary

print(utxos)
# utxos.sort(key=lambda x: x["val"], reverse=True)
calc_change(utxos, 7)

# assumptions: all utxos in a date range must be used -- crucial
# utxos come presorted in order of date
# strategy: start at beginning/end of list of utxos;