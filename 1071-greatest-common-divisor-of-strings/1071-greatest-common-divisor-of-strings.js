/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {



function gcd(a, b) {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

let longerString = str1.length>str2.length ? str1 : str2
let shorterString = str1.length>str2.length? str2: str1

if(str1 + str2 !== str2 + str1){
    return ""
}



let gcdLen = gcd(longerString.length, shorterString.length);



return longerString.slice(0, gcdLen)



}
