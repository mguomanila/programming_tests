// '''
// BinaryGap
// Find longest sequence of zeros in binary representation of an integer.
//
// A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
//
// For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
//
// Write a function:
//
// def solution(N)
//
// that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
//
// For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
//
// Write an efficient algorithm for the following assumptions:
//
// N is an integer within the range [1..2,147,483,647].
// '''
// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');
const print = console.log

function decToBinary1(N){
    return (N >>> 0).toString(2)
}

function decToBinary2(N){
    let a = ''
    if (N>1){
        a = decToBinary2(Math.floor(N/2))
    }
    return (N%2).toString() + a.toString()
}
function rev_decToBinary2(text){
    let bin = ''
    for (let i = n.length-1; i >= 0; i--){
        bin += n[i]
    }
}

function soln2(N){
    let bin = decToBinary(N)
}

function soln1(N) {
    // write your code in JavaScript (Node.js 8.9.4)
    let arr = ret_bin(N)
    for (let i = 1; i < arr.length-1; i++){
        length = arr[i].length
        if (length>0){
            arr.push(arr[i].length)
        }
    }
    return Math.max(...arr)
}

function test(N){
    let arr = ret_bin(N)
    let length
    for(let i = 1; i < arr.length-1; i++){
        length = arr[i].length
        if (length>0){
            print(length)
        }
    }
}

// test
function test_soln1(){
    let max = 2147483647
    // let max = 10e5
    console.time('test_soln1')
    let n = decToBinary2(max)

    print(bin)
    //test(i)
    console.timeEnd('test_soln1')
}
