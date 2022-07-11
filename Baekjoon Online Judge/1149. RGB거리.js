let [N, ...arr] = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

N = +N;
arr = arr.map((value) => value.split(" ").map(Number));

function solution(N, arr) {
	for (let i = 1; i < N; i++) {
		arr[i][0] = Math.min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0];
		arr[i][1] = Math.min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1];
		arr[i][2] = Math.min(arr[i - 1][1], arr[i - 1][0]) + arr[i][2];
	}
	return Math.min(arr[N - 1][0], arr[N - 1][1], arr[N - 1][2]);
}

console.log(solution(N, arr));
