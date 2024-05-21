function solution(begin, target, words) {
    var answer = 0;
    if(!words.includes(target)) return 0
    
    let stack = []
    stack.push(begin)
    let visited = Array(words.length).fill(false)
    
    while(stack.length > 0){
        nw = stack.pop()
        answer += 1
        if(nw == target) return answer-1
        
        for(let i = 0; i < words.length; i++){
            let cnt = 0
            for(let j = 0 ; j < words[i].length; j++){
                if (words[i][j] != nw[j]){
                    cnt += 1
                }
            }
            if(cnt == 1 && !visited[i]){
                stack.push(words[i])
                visited[i] = true
            }
        }
    }
    
    return 0;
}