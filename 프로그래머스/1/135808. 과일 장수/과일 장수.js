function solution(k, m, score) {
    var answer = 0;
    score.sort().reverse()
    var idx = 0;
    while (idx <= score.length){
        var slicedScore = score.slice(idx, idx + m);
        if (slicedScore.length != m) break;
        else{
            answer += slicedScore[slicedScore.length - 1] * m
        }
        idx += m
    }
    return answer;
}