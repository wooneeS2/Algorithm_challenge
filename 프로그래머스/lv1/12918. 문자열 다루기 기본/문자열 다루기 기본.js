function solution(s) {
    let result = parseInt(s)
    if((s.length==4||s.length==6) && result==s){
        return true
    }
    return false;
}