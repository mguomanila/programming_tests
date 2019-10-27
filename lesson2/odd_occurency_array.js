function soln1(A){
    let searched = []
    for(let i=0; i<A.length; i++){
        count(searched, A[i])
    }
    return odd_occurence(searched)
}

function count(searched,n){
    if(n>searched.length){
        for(let i=searched.length-1; i<n; i++){
            searched.push(0)
        }
        searched[n-1] += 1
    }
    else {
        searched[n-1] += 1
    }
}

function odd_occurence(searched){
//     console.log('s',searched.length)
    for(let i=0; i<searched.length; i++){
        if(searched[i] % 2 !== 0){
            return i+1
        }
    }
}

;( () => {
    let solution = soln1
    let A = []
    A[0] = 9,  A[1] = 3,  A[2] = 9
    A[3] = 3,  A[4] = 9,  A[5] = 7
    A[6] = 9
    console.log(solution(A))
})()


/**
 * 
 * Detected time complexity:O(N) or O(N*log(N))
 * score: 88% for soln1 , date 10-26 @3:27pm
 * todo: need to improve!
 * 
 */

