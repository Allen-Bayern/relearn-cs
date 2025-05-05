/**
 * @author Yuebing
 * @description 二叉树前序遍历
 */
import type { BiTreeNode, Maybe } from "../types";

/** 递归遍历 */
export function recursivePreOrderTraversal<T = unknown>(
  root: Maybe<BiTreeNode<T>>
): T[] {
  if (!root) {
    return [];
  }

  const res: T[] = [];

  const dfs = (node: Maybe<BiTreeNode<T>>): void => {
    if (!node) {
      return;
    }

    res.push(root.value);
    dfs(root.left);
    dfs(root.right);
  };

  dfs(root);
  return res;
}

export function stackPreOrderTraversal<T = unknown>(
  root: Maybe<BiTreeNode<T>>
): T[] {
  if (!root) {
    return [];
  }

  const stack: BiTreeNode<T>[] = [];
  const res: T[] = [];

  let node: Maybe<BiTreeNode<T>> = root;

  while (stack.length && node) {
    while (node) {
      res.push(node.value);
      if (node?.left) {
        stack.push(node.left);
        node = node.left;
      }
    }

    node = stack.pop()!;
    node = node.right;
  }

  return res;
}
