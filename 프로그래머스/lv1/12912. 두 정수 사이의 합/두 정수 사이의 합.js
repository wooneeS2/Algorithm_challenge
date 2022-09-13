function solution(a, b) {
    let answer = 0;
    const max = Math.max(a,b)
    const min = Math.min(a,b)
    const nums = []
    for(let i=min; i<=max; i++){
        nums.push(i)
    }
    answer = nums.reduce((prev,curr)=>prev+curr)
    return answer;
}