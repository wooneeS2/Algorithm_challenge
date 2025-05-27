/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    
    let result = 0;


   for( let i = 0; i < flowerbed.length; i++){
    if((flowerbed[i-1]??0)===0&&flowerbed[i]===0&&(flowerbed[i+1]??0)===0){
        result++;
        flowerbed[i]=1
        i++;
    }


   }



   if(result>=n){
    return true;
   }


    return false;

};