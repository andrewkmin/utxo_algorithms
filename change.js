utxos = [
    {
        val: 2,
        date: 1
    },
    {
        val: 4,
        date: 2
    },
    {
        val: 6,
        date: 3
    },
    {
        val: 8,
        date: 4
    },
    {
        val: 10,
        date: 5
    }
]

function main() {
    var hi = rec(16, utxos, utxos.length - 1, {})
    console.log(hi);
}

// is there a point to memoizing? what's the probability that values are repeated?
function rec(value, coins, index, memo) {
    var key = value + ":" + index;
    console.log('INSIDE')
    if (memo[key]) {
        console.log('inside')
        return memo[key];
    }

    if (value == 0) {
        return 1;
    } else if (value < 0) {
        return 0;
    } else if (index < 0) {
        return 0;
    } else if (value < coins[index].val) {
        var returnVal = rec(value, coins, index - 1, memo);
    } else {
        var returnVal = rec(value, coins, index - 1, memo) + 
        rec(value - coins[index].val, coins, index - 1, memo);
    }

    memo[key] = returnVal;
    return returnVal;
}

main();