import type { SingleNode, BiNode, BiTreeNode } from "./index";

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

/**
 * Create an empty bi-tree node.
 * @param value The value of the node
 * @returns An empty bi-tree node.
 */
const createTreeNode = <T = unknown>(value: T): BiTreeNode<T> => ({
  value,
  left: null,
  right: null,
});

export { createSingleNode, createBiNode, createTreeNode };
