function solution(s) {
    const wordLen = s.length
    if(s.length%2==0){
        return s[(wordLen/2)-1]+s[(wordLen/2)]
    }

    return s[parseInt(wordLen/2)]
  
}