class Node {
	constructor(item) {
		this.item = item;
		this.next = null;
	}
}

class Queue {
	constructor() {
		this.head = null;
		this.tail = null;
		this.size = 0;
	}
	length() {
		return this.size;
	}

	isEmpty() {
		return this.size === 0;
	}

	enqueue(item) {
		const node = new Node(item);

		if (this.head === null) {
			this.head = node;
		} else {
			this.tail.next = node;
		}

		this.tail = node;
		this.size += 1;
	}

	dequeue() {
		let poppedItem;
		if (this.head !== null) {
			poppedItem = this.head.item;
			this.head = this.head.next;
			this.size -= 1;
		}

		return poppedItem;
	}
}

const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

const [N, M] = input.shift().split(" ").map(Number);
let arr = input.map((v) => v.split(" ").map(Number));

const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];

function melting() {
	for (let y = 0; y < N; y++) {
		for (let x = 0; x < M; x++) {
			if (arr[y][x] > 0) {
				let cnt = 0;
				for (let i = 0; i < 4; i++) {
					const ny = y + dy[i];
					const nx = x + dx[i];
					if (ny >= 0 && ny < N && nx >= 0 && nx < M && arr[ny][nx] === 0) {
						cnt += 1;
					}
				}
				if (arr[y][x] - cnt <= 0) {
					arr[y][x] = -1;
				} else {
					arr[y][x] -= cnt;
				}
			}
		}
	}
}

function minusToZero() {
	for (let y = 0; y < N; y++) {
		for (let x = 0; x < M; x++) {
			if (arr[y][x] === -1) arr[y][x] = 0;
		}
	}
}
function solution(r, c, visit) {
	const q = new Queue();
	q.enqueue([r, c]);
	while (q.length() > 0) {
		const [y, x] = q.dequeue();

		for (let i = 0; i < 4; i++) {
			const ny = y + dy[i];
			const nx = x + dx[i];

			if (
				ny >= 0 &&
				ny < N &&
				nx >= 0 &&
				nx < M &&
				arr[ny][nx] !== 0 &&
				visit[ny][nx] === 0
			) {
				q.enqueue([ny, nx]);
				visit[ny][nx] = 1;
			}
		}
	}
}

let ans = 0;
while (true) {
	const visit = Array.from(new Array(N), () => new Array(M).fill(0));
	let cnt = 0;

	for (let i = 0; i < N; i++) {
		for (let j = 0; j < M; j++) {
			if (arr[i][j] !== 0 && visit[i][j] === 0) {
				visit[i][j] = 1;
				solution(i, j, visit);
				cnt += 1;
			}
		}
	}

	if (cnt >= 2) {
		console.log(ans);
		break;
	} else if (cnt === 0) {
		console.log(0);
		break;
	}
	melting();
	minusToZero();
	ans += 1;
}
