let [N, ...arr] = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");
N = +N;
arr = arr[0].split(" ").map((v) => +v);

function solution(arr) {
	dist = [];
	for (let i = 0; i < N; i++) {
		dist[i] = 1;
		for (let j = 0; j < i; j++) {
			if (arr[j] < arr[i]) {
				dist[i] = Math.max(dist[i], dist[j] + 1);
			}
		}
	}
	return Math.max(...dist);
}
console.log(solution(arr));
