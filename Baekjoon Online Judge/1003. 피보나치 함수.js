const [n, ...arr] = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n")
	.map(Number);
let fiboArr = [0];
let ans = [
	[1, 0],
	[0, 1],
	[1, 1],
];
function fiboWithMemo(n) {
	if (n < 0) return;
	if (n < 3 && n > 0) fiboArr[n] = 1;
	if (n !== 0 && !fiboArr[n]) {
		fiboArr[n] = fiboWithMemo(n - 1) + fiboWithMemo(n - 2);
		ans[n] = [ans[n - 1][0] + ans[n - 2][0], ans[n - 1][1] + ans[n - 2][1]];
	}

	return ans[n].join(" ");
}

for (let i of arr) {
	console.log(fiboWithMemo(i));
}
