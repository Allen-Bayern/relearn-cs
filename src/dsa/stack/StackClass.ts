import type { BiNode as Node, Maybe } from "../types";
import { createBiNode } from "../types/FactoryFunctions";

const Stack = class<T = unknown> {
  private _stackTop: Maybe<Node<T>> = null;
  private _length = 0;

  get size(): number {
    return this._length;
  }

  push(v: T): this {
    const newNode = createBiNode(v);
    if (!this._stackTop) {
      this._stackTop = newNode;
      this._length = 1;
    } else {
      this._stackTop.next = newNode;
      newNode.prev = this._stackTop;
      this._stackTop = newNode;
      this._length++;
    }

    return this;
  }

  pop(): Maybe<T> {
    if (!this._stackTop) {
      this._length = 0;
      return null;
    }

    const { prev: prevNode, value } = this._stackTop;
    if (prevNode) {
      prevNode.next = null;
    }
    this._stackTop = prevNode;
    this._length--;
    return value;
  }

  extend(...values: T[]): this {
    return values.reduce((_self, val) => _self.push(val), this);
  }
};

export default Stack;
