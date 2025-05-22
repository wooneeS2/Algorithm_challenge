/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    // let result ='';
    // for(let i=0; i<word1.length;i++){
    //     result +=word1[i]
    //     if(word2.length>i){
    //         result+=word2[i]
    //     }
    // }
    // if(word1.length<word2.length){
    //     result+=word2.slice(word1.length)
    // }
    // else{
    //     result+=word1.slice(word1.length)
    // }
    // return result


//     let result =[];
// let longerWord = word1.length>word2.length ? word1 : word2;
// for(i=0; i<longerWord.length ; i++){
//     result.push(word1[i])
//     result.push(word2[i])
// }
// result = result.filter(result=>result).join("")
// return result
    


    let result =[];

for(let i=0; i<Math.max(word1.length,word2.length) ; i++){
    if(word1[i])result.push(word1[i])
   if(word2[i]) result.push(word2[i])
}

return result.join("")



};