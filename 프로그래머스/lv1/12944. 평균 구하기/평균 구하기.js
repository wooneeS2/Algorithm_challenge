function solution(arr) {
    let answer = 0;
    const sum = arr.reduce((previous,curr)=>previous+curr)
    answer = sum/arr.length
    return answer;
}