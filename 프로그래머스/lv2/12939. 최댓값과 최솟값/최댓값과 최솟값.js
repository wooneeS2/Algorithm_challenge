function solution(s) {
    var answer = [];
    s = (s.split(' '))
    
    answer.push(String(Math.min(...s)));
    answer.push(String(Math.max(...s)));
    
    
    return answer.join(' ')
}