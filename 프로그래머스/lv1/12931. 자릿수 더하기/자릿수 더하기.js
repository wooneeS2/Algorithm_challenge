function solution(n)
{
    let nums=[]

    while(n>0){
        nums.push(n%10)
        n=Math.floor(n/10)

    }
    const result =    nums.reduce((sum,value)=>{return sum+value},0)
    return result
    
}