let input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");
const [N, L, R] = input.shift().trim().split(" ").map(Number);
let arr = input.map((v) => v.trim().split(" ").map(Number));

let ans = 0;

const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];

function bfs(r, c, visit) {
	let nums = [];
	let total = arr[r][c];
	let cnt = 1;
	nums.push([r, c]);
	visit[r][c] = 1;
	let q = [];
	q.push([r, c]);

	while (q.length > 0) {
		let [y, x] = q.shift();

		for (let i = 0; i < 4; i++) {
			let ny = y + dy[i];
			let nx = x + dx[i];
			if (
				ny >= 0 &&
				ny < N &&
				nx >= 0 &&
				nx < arr.length &&
				visit[ny][nx] == 0
			) {
				let minus = Math.abs(arr[y][x] - arr[ny][nx]);
				if (minus >= L && minus <= R) {
					cnt += 1;
					visit[ny][nx] = 1;
					total += arr[ny][nx];
					nums.push([ny, nx]);
					q.push([ny, nx]);
				}
			}
		}
	}

	if (nums.length > 1) {
		for (let [y, x] of nums) {
			arr[y][x] = Math.floor(total / cnt);
		}
	}

	return nums.length;
}

while (true) {
	let flag = false;
	let visit = Array.from(Array(N), () => Array(arr.length).fill(0));

	for (let i = 0; i < N; i++) {
		for (let j = 0; j < arr.length; j++) {
			if (visit[i][j] == 0) {
				if (bfs(i, j, visit) > 1) flag = true;
			}
		}
	}

	if (!flag) break;

	ans += 1;
}

console.log(ans);
