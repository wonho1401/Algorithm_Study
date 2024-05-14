function inRange(x, y, maps){
    return 0 <= x && x < maps.length && 0 <= y && y < maps[0].length
}

function solution(maps) {
    var answer = 0;
    let dx = [1, 0, -1, 0]
    let dy = [0, 1, 0, -1]
    let visited = Array.from({length: maps.length}, () => Array(maps[0].length).fill(false))
    let q = []
    visited[0][0] = true
    q.push([0,0])
    while(q.length > 0){
        let [x, y] = q.shift()
        for(let i = 0; i < 4; i++){
            let nx = x + dx[i]
            let ny = y + dy[i]
            if(inRange(nx,ny,maps) && !visited[nx][ny] && maps[nx][ny] == 1){
                visited[nx][ny] = true
                maps[nx][ny] = maps[x][y] + 1
                q.push([nx,ny])
            }
        }
    }
    return maps[maps.length-1][maps[0].length - 1] > 1 ? maps[maps.length - 1][maps[0].length - 1] : -1
}