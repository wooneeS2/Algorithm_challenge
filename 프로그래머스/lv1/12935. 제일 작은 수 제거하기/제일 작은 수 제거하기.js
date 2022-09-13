function solution(arr) {
    var answer = [];
    if(arr.length<=1){
        answer.push(-1);
        return answer
    }
    answer = arr.filter(i=>i!== Math.min(...arr));
    
    return answer;
}