function solution(n) {
    let answer ;
    let nums=String(n).split('')
    answer = nums.reverse()
    return answer.map(val=> parseInt(val));
}