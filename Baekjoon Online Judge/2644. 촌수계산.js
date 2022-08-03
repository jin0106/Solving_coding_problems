const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");
const N = Number(input.shift().split());
const [start, end] = input.shift().split(" ").map(Number);
const M = Number(input.shift().split());
const graph = Array.from(Array(N + 1), () => new Array());
const visited = Array(N + 1).fill(-1);
for (let i = 0; i < M; i++) {
	let [y, x] = input.shift().split(" ").map(Number);
	graph[y].push(x);
	graph[x].push(y);
}

function solution(start, cnt) {
	const q = [];
	q.push([start, cnt]);
	visited[start] = 1;

	while (q.length) {
		const [num, cnt] = q.shift();
		if (num === end) return cnt;
		for (let i = 0; i < graph[num].length; i++) {
			const child = graph[num][i];
			if (visited[child] === -1) {
				q.push([child, cnt + 1]);
				visited[child] = 1;
			}
		}
	}
	return -1;
}
console.log(solution(start, 0));
