import type { SingleNode, BiNode } from "./index";

/**
 * Create an empty single node.
 * @param value The value of the node
 * @returns An empty single node.
 */
function createSingleNode<T = unknown>(value: T): SingleNode<T> {
  return {
    value,
    next: null,
  };
}

/**
 * Create an empty bi-direction node.
 * @param value The value of the node
 * @returns An empty bi-direction node.
 */
function createBiNode<T = unknown>(value: T): BiNode<T> {
  return {
    value,
    prev: null,
    next: null,
  };
}

export { createSingleNode, createBiNode };
