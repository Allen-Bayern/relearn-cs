/**
 * @author Yuebing
 * @description 二叉树中序遍历
 */
import type { BiTreeNode, Maybe } from "../types";

/** 递归中序遍历 */
export function recursiveInOrderTraversal<T = unknown>(
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

    dfs(root.left);
    res.push(root.value);
    dfs(root.right);
  };

  dfs(root);
  return res;
}

/** 迭代中序遍历 */
export function stackInOrderTraversal<T = unknown>(
  root: Maybe<BiTreeNode<T>>
): T[] {
  if (!root) {
    return [];
  }

  const stack: BiTreeNode<T>[] = [];
  const res: T[] = [];

  let node: Maybe<BiTreeNode<T>> = root;

  while (stack.length || node) {
    while (node) {
      if (node?.left) {
        stack.push(node.left);
        node = node.left;
      }
    }

    node = stack.pop()!;
    res.push(node.value);
    node = node.right;
  }

  return res;
}
