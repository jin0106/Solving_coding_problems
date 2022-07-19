const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

const [M, N] = input.shift().split(" ").map(Number);
const arr = input.map((v) => v.trim().split(" ").map(Number));

const dp = Array.from(new Array(M), () => new Array(N).fill(-1));
const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];

function solution(r, c) {
	if (r === M - 1 && c == N - 1) {
		return 1;
	}

	if (dp[r][c] !== -1) {
		return dp[r][c];
	}
	let cnt = 0;
	for (let i = 0; i < 4; i++) {
		const ny = r + dy[i];
		const nx = c + dx[i];

		if (ny >= 0 && ny < M && nx >= 0 && nx < N) {
			if (arr[r][c] > arr[ny][nx]) {
				cnt += solution(ny, nx);
			}
		}
	}

	dp[r][c] = cnt;

	return cnt;
}

console.log(solution(0, 0));
