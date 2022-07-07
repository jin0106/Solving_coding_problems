const fs = require("fs");
const [n, k] = fs
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split(" ")
	.map(Number);
const dist = new Array(100001).fill(0);
function solution(N, K) {
	q = [];
	q.push([N, 0]);

	while (q) {
		let [curr, cnt] = q.shift();
		if (curr === K) {
			console.log(cnt);
			break;
		} else {
			for (i of [curr + 1, curr - 1, curr * 2]) {
				if (0 <= i && i <= 100000 && dist[i] === 0) {
					+i / 2 === curr ? q.unshift([i, cnt]) : q.push([i, cnt + 1]);
					dist[i] = 1;
				}
			}
		}
	}
}
solution(n, k);
