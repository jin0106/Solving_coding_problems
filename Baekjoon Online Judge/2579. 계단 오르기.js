let [N, ...arr] = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n")
	.map((v) => +v);

const dist = new Array(N).fill(0);
dist[0] = arr[0];
dist[1] = Math.max(arr[0] + arr[1], arr[1]);
dist[2] = Math.max(arr[0] + arr[2], arr[1] + arr[2]);
function solution(arr) {
	for (let i = 3; i < N; i++) {
		dist[i] = Math.max(arr[i] + arr[i - 1] + dist[i - 3], arr[i] + dist[i - 2]);
	}
	return dist[N - 1];
}

console.log(solution(arr));
