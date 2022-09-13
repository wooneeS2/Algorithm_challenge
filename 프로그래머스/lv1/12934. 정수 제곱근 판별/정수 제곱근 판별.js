function solution(n) {
    let answer = -1;
    
    for(let i=1;i<=n;i++){
        if(i**2==n){
            return (i+1)**2
        }
        
    }
    return answer;
}