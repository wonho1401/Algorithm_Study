function solution(keymap, targets) {
    var answer = [];
    const dic = {};
    
    for(key in keymap){
        for(let i = 0; i < keymap[key].length; i++){
            if(keymap[key][i] in dic){
                if(dic[keymap[key][i]] > i){
                    dic[keymap[key][i]] = i + 1
                }
            } else{
                dic[keymap[key][i]] = i + 1
            }
        }
    }
    for (target of targets){
        let tmp = 0;
        for (t in target){
            tmp += dic[target[t]]
        }
        if (tmp > 0){
            answer.push(tmp)            
        } else{
            answer.push(-1)
        }
    }
    return answer;
}