function solution(n)
{


    let nums= String(n).split('')
    const result = nums.reduce((sum,value)=>{return parseInt(sum)+parseInt(value)},0)
    return result
    
}