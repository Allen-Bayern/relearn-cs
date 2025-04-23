import type { BiNode as Node, Maybe } from "../types";
import { createBiNode } from "../types/FactoryFunctions";

class Queue<T = unknown> {
  private _queueHead: Maybe<Node<T>> = null;
  private _queueTail: Maybe<Node<T>> = null;
  private _length = 0;

  get size(): number {
    return this._length;
  }

  enqueue(v: T): this {
    const newNode = createBiNode(v);
    if (!this._queueHead || !this._queueTail) {
      this._queueHead = newNode;
      this._queueTail = newNode;
      this._length = 1;
    } else {
      this._queueTail.next = newNode;
      newNode.prev = this._queueTail;
      this._queueTail = newNode;
      this._length++;
    }

    return this;
  }

  dequeue(): Maybe<T> {
    if (!this._queueHead || !this._queueTail) {
      this._queueHead = null;
      this._queueTail = null;
      this._length = 0;
      return null;
    }

    const { next: nextNode, value } = this._queueHead;
    if (nextNode) {
      nextNode.prev = null;
    }
    this._queueHead = nextNode;
    this._length--;
    return value;
  }

  extend(...values: T[]): this {
    return values.reduce((_self, v) => _self.enqueue(v), this);
  }
}

export default Queue;
