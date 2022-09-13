function solution(phone_number) {
    let number=phone_number.split('')
    const hideNumber = [];
    for(let i=0; i<phone_number.length-4; i++){
        hideNumber.push('*')
    }
    for(let i=phone_number.length-4; i<phone_number.length; i++){
        hideNumber.push(number[i])
    }
    return hideNumber.join("");
}