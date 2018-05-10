function residual (A, i, K, result) {

    const number = A+i;
    const residual = (number % K);
    if (residual === 0) {
        // result.push(number);
        result += 1;
    }
    return result;
}

function solution(A=0, B=0, K=1) {
    // write your code in JavaScript (Node.js 8.9.4)
    var t0 = process.hrtime();

    // const range = B - A;
    let result = 0;
    if (B - A === 0) {
        result = residual(A, 0, K, result)
    } else {
        for(let i = A; i <= B; i+=1) {
            result = residual(A, i, K, result);
        }
    }
    // array is now created;
    var t1 = process.hrtime(t0);

    console.log("result: ", result, ", time: ", ((t1[1]/1000000000) + " seconds"));
  
    return result;
}

module.exports = function () {
    const A = 101;
    const B = 123000000;
    const K = 10000;
    solution(A, B, K);
}
