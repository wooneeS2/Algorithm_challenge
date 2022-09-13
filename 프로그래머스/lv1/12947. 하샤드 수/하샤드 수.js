function solution(x) {
    let nums= String(x).split('');
    const sum = nums.reduce((prev,curr)=>parseInt(prev)+parseInt(curr))
    return x%sum===0;
}