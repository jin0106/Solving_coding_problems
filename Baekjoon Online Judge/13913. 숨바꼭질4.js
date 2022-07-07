const fs = require("fs");
const [n, k] = fs
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split(" ")
	.map(Number);

function solution(N, K) {
	const dist = new Array(100001).fill(0);
	const move = new Array(100001).fill(0);
	q = [];
	q.push(N);

	while (q.length > 0) {
		let curr = q.shift();
		if (curr === K) {
			console.log(dist[curr]);
			const arr = [];
			let temp = curr;
			for (i = 0; i < dist[curr] + 1; i++) {
				arr.push(temp);
				temp = move[temp];
			}
			console.log(arr.reverse().join(" "));
			break;
		} else {
			for (i of [curr + 1, curr - 1, curr * 2]) {
				if (0 <= i <= 100000 && dist[i] === 0) {
					q.push(i);
					dist[i] = dist[curr] + 1;
					move[i] = curr;
				}
			}
		}
	}
}
solution(n, k);
