function solution(number, k) {
    const stack = []
    for(n of number){
        while(k > 0 && stack[stack.length - 1] < n){
            stack.pop()
            k--;
        }
        stack.push(n)
    }
    if(k == 0){
        return stack.join("");
    } else{
        return stack.slice(0, -k).join("")
    }
}