function solution(n) {
    // let answer = [];
    // for(let i=0; i<n; i++){
    //     i%2==0? answer.push('수'):answer.push('박')
    // }
    // return answer.join('')
    let answer = '수박'.repeat(n).slice(0,n)
    return answer
}