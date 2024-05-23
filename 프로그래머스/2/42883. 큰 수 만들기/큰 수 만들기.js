function solution(number, k) {
    const stack = []
    for(n of number){
        while(k > 0 && stack[stack.length - 1] < n){
            stack.pop()
            k--;
        }
        stack.push(n)
    }
    stack.splice(stack.length - k, k)
    return stack.join('');
}