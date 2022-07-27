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

const [N, M, K] = input[0].split(" ").map(Number);
let arr = input.slice(1).map((v) => v.split("").map(Number));

const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];

function solution(r, c, cnt) {
	const visit = Array.from(Array(N), () =>
		Array.from(Array(M), () => Array(K + 1).fill(0))
	);

	const q = new Queue();
	q.enqueue([r, c, cnt]);
	visit[0][0][0] = 1;

	while (!q.isEmpty()) {
		const [y, x, cnt] = q.dequeue();
		if (y === N - 1 && x === M - 1) return visit[y][x][cnt];
		for (let i = 0; i < 4; i++) {
			const ny = y + dy[i];
			const nx = x + dx[i];

			if (0 <= ny && ny < N && 0 <= nx && nx < M) {
				if (arr[ny][nx] === 0 && !visit[ny][nx][cnt]) {
					visit[ny][nx][cnt] = visit[y][x][cnt] + 1;
					q.enqueue([ny, nx, cnt]);
				} else if (arr[ny][nx] === 1 && !visit[ny][nx][cnt + 1] && cnt < K) {
					visit[ny][nx][cnt + 1] = visit[y][x][cnt] + 1;
					q.enqueue([ny, nx, cnt + 1]);
				}
			}
		}
	}
	return -1;
}

console.log(solution(0, 0, 0));
