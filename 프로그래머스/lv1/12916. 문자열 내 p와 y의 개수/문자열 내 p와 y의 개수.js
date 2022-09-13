function solution(s){
    str = String(s).trim().split('')
    let countP=0
    let countY=0
    for(let i=0; i<=str.length;i++){
        if(str[i]==='p'|| str[i]==='P'){
            countP+=1;
        }
        else if(str[i]==='y'|| str[i]==='Y'){
            countY+=1;
        }
    }

    

    return countY===countP;
}