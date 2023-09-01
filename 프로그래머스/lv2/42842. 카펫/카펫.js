function solution(brown, yellow) {
    let answer_list = [];
    let all = brown + yellow;
    
    for(let i = 1; i<= Math.sqrt(all); i++){
        if(all % i == 0) answer_list.push([all / i , i])
    }
    for(const item of answer_list){
        if(item[0]*2 + (item[1] - 2)* 2 == brown) return item
    }
}