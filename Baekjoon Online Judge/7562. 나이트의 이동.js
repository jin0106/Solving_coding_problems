const dy = [-2, -2, -1, -1, 2, 2, 1, 1];
const dx = [-1, 1, -2, 2, -1, 1, -2, 2];

function solution(l, start, end) {
	const visit = Array.from(Array(l), () => new Array(l).fill(0));
	const q = [];
	q.push([start[0], start[1], 0]);
	while (q.length) {
		const [y, x, cnt] = q.shift();
		if (y == end[0] && x === end[1]) return cnt;

		for (let i = 0; i < 8; i++) {
			const ny = y + dy[i];
			const nx = x + dx[i];

			if (l > ny && 0 <= ny && 0 <= nx && l > nx && visit[ny][nx] === 0) {
				visit[ny][nx] = 1;
				q.push([ny, nx, cnt + 1]);
			}
		}
	}
}

const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

for (let i = 0; i < +input[0]; i++) {
	const l = +input[i * 3 + 1];
	const [sx, sy] = input[i * 3 + 2].split(" ").map((v) => +v);
	const [ex, ey] = input[i * 3 + 3].split(" ").map((v) => +v);
	console.log(solution(l, [sx, sy], [ex, ey]));
}
