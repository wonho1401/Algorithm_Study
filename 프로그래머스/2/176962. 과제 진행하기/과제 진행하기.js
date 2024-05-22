function solution(plans) {
    var answer = [];
// [1]. plans 시간 순 정렬하기
    plans.sort((a, b) => {
        if(a[1].split(":")[0] == b[1].split(":")[0])
            return a[1].split(":")[1] - b[1].split(":")[1]
        else
            return a[1].split(":")[0] -b[1].split(":")[0]
    })
// [2]. 시 -> 분으로 변환
    const [ch, cm] = plans[0][1].split(":")
    
    for(plan of plans){
        plan[1] = parseInt(plan[1].split(":")[0] - ch) * 60 + parseInt(plan[1].split(":")[1])
        plan[1] = parseInt(plan[1]) - cm
        plan[2] = parseInt(plan[2])
    }
// [3]. plans[1][1] 부터 시작해서 plans[plans.length - 1][1] 까지 진행하면서 queue 만들었다 뺐다 진행
    const queue = []
    let time = 0
    let idx = 0
    let ndx = idx

    while(answer.length < plans.length){
// 종료 조건: answer의 길이가 plans와 같을 때
// answer 추가 조건: plans[i][2] 가 0이 되면 추가됨
        if(plans[ndx][2] == 0){
            answer.push(plans[ndx][0])

            if (queue.length >= 1){
                ndx = queue.pop()
            }
        }
        if(idx < plans.length - 1 && plans[idx + 1][1] == time){
            queue.push(ndx)
            idx += 1
            ndx = idx
        }
        plans[ndx][2] -= 1
        time += 1
    }
    return answer;
}