function solution(numbers) {
    var answer = [];
    for (idx1 in numbers){
        let sum = 0;
        for(idx2 in numbers){
            if(idx1 == idx2) continue
            sum = numbers[idx1] + numbers[idx2]
            if(!(answer.includes(sum))){
                answer.push(sum)
            } 
        }
    }
    answer.sort((a, b) => a - b)
    return answer;
}