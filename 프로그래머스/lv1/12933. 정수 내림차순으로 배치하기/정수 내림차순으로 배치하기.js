function solution(n) {
    let answer = 0;
    nums = String(n).split('');
    nums= nums.map((val)=>parseInt(val)).sort((prev,curr)=>curr-prev)
    return parseInt(nums.join(''));
}