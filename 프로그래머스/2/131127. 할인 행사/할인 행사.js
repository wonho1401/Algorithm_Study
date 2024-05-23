function solution(want, number, discount) {
    var answer = 0;
    const sum = number.reduce((acc,cur) => acc + cur, 0)
    for(let i = 0; i <= discount.length - sum; i++){
        const dic = []
        for(let j = i; j < sum + i; j++){
            if(dic[discount[j]]){
                dic[discount[j]] += 1
            } else{
                dic[discount[j]] = 1
            }
        }
        let flag = true
        want.forEach((w, idx) => {
            if(!(dic[w] == number[idx])){
                flag = false
            }
        })
        if(flag) answer += 1
    }
    return answer;
}