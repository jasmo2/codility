function solution(A=0, B=0, K=1) {
    // write your code in JavaScript (Node.js 8.9.4)
    const arr = [];
    const range = B - A;
    if (range === 0) {
        arr.push(A);
    } else {
        for(let i = 0; i < range; i+=1) {
            arr.push(B+i);
        }
    }

    // array is now created;
    // const result = [];
    let result = 0;
    for(let i = 0; i < range; i+=1) { 
        const number = A+i;
        const residual = (number % K);
        if (residual === 0) {
            // result.push(number);
            result += 1;
        }
    }
    console.log(result);
  
    return result;
}

module.exports = function () {
    const A = 10;
    const B = 10;
    const K = 1;
    solution(A, B, K);
}
