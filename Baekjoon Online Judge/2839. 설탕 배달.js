const N = parseInt(require("fs").readFileSync("/dev/stdin").toString().trim());

const arr = new Array(N + 5).fill(5001);
arr[3] = 1;
arr[5] = 1;

function solution(n) {
	for (let i = 6; i <= n; i++) {
		arr[i] = Math.min(arr[i - 3], arr[i - 5]) + 1;
	}

	if (arr[n] >= 5001) return -1;
	else return arr[n];
}

console.log(solution(N));
