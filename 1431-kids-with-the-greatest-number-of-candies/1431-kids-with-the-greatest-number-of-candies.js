/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    
    let result = []
    let maxCandies = Math.max(...candies)
    
    for(let i=0; i<candies.length; i++){
        result.push(candies[i]+extraCandies >= maxCandies)
    }
    return result;
    
    
};