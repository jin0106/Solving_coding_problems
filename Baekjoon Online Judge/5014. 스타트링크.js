class Node {
	constructor(item) {
		this.item = item;
		this.next = null;
	}
}

class Queue {
	constructor() {
		this.head = null;
		this.size = 0;
		this.tail = null;
	}

	isEmpty() {
		return this.size === 0;
	}

	length() {
		return this.size;
	}

	enque(item) {
		const node = new Node(item);
		if (this.head === null) {
			this.head = node;
		} else {
			this.tail.next = node;
		}

		this.size += 1;
		this.tail = node;
	}

	deque() {
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
	.readFileSync("./input.txt")
	.toString()
	.trim()
	.split("\n");

const [F, S, G, U, D] = input.shift().split(" ").map(Number);

function solution() {
	const visit = new Array(1000001).fill(-1);
	visit[S] = 0;
	const q = new Queue();
	q.enque(S);
	while (q.length() > 0) {
		const curr = q.deque();
		if (curr === G) return visit[G];

		for (stair of [U, -D]) {
			const newFlr = curr + stair;
			if (1 <= newFlr && newFlr <= F && visit[newFlr] === -1) {
				visit[newFlr] = visit[curr] + 1;
				q.enque(newFlr);
			}
		}
	}
	return "use the stairs";
}

console.log(solution());
