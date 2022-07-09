const N = parseInt(require("fs").readFileSync("/dev/stdin").toString().trim());
const arr = new Array(N + 1).fill(0);
arr[3] = 1;
arr[2] = 1;

function solution(n) {
	for (let i = 4; i <= n; i++) {
		arr[i] = arr[i - 1] + 1;
		if (i % 2 === 0) arr[i] = Math.min(arr[i], arr[i / 2] + 1);
		if (i % 3 === 0) arr[i] = Math.min(arr[i], arr[i / 3] + 1);
	}
	return arr[n];
}

console.log(solution(N));
