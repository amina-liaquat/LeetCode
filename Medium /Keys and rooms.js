/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function(rooms) {
    const n = rooms.length;
    const visited = new Array(n).fill(false);
    
    const dfs = (room) => {
        visited[room] = true;
        
        for (const key of rooms[room]) {
            if (!visited[key]) {
                dfs(key);
            }
        }
    };
    
    // Start DFS from room 0
    dfs(0);
    
    // Check if all rooms are visited
    return visited.every(room => room === true);
};
