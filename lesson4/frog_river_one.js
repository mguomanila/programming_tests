// task score: 100%
function soln1(X,A){
    let steps = new Set()
    for(let i=0; i<A.length; i++){
        if(check_step(X, steps, A[i])){
            return i
        }
    }
    return -1
}

function check_step(X, steps, step){
    steps.add(step)
    if(steps.size == X){
        return true
    } 
}

function random(end, start=0){
    range = Math.floor(end - start)
    return (Math.ceil(range * Math.random()) + start)
}

// test
;( () => {
    let A = []
    A[0] = 1
    A[1] = 3
    A[2] = 1
    A[3] = 4
    A[4] = 2
    A[5] = 3
    A[6] = 5
    A[7] = 4
    X =  5
    console.log(soln1(X,A))
})

// maximum tests
// N and X are integers within the range [1..100,000];
// A = [1..X]
;( () => {
    console.time('test')
    let A = []
    let Nmax = 1e5
    let Nmin = 1
    let X = random(Nmax,Nmin)
    for(let i=Nmin; i<Nmax; i++){
        A.push(random(X,Nmin))
//         console.log(A[i-1])
    }
    let value = soln1(X,A)
    console.timeEnd('test')
    console.log(value)
})()
