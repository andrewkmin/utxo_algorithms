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