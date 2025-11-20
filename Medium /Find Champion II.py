/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var findChampion = function (n, edges) {
    let hasIncomingEdge = new Array(n).fill(0);

    for (let edge of edges) {
        let to = edge[1];

        // from ---> to
        hasIncomingEdge[to]++;
    };

    let champ = -1;
    let count = 0;
    for (let i = 0; i < n; i++) {
        if (hasIncomingEdge[i] === 0) {
            champ = i;
            count++;
            if (count > 1) {
                return -1;
            }
        };
    };
    return champ;
};
