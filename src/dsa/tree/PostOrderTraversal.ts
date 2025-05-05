/**
 * @author Yuebing
 * @description 二叉树后序遍历
 */
import type { BiTreeNode, Maybe } from "../types";

/** 递归遍历 */
export function recursivePostOrderTraversal<T = unknown>(
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

    dfs(node.left);
    dfs(node.right);
    res.push(node.value);
  };

  dfs(root);
  return res;
}

export function stackPostOrderTraversal<T = unknown>(
  root: Maybe<BiTreeNode<T>>
): T[] {
  if (!root) {
    return [];
  }

  // 栈
  const stack: Maybe<BiTreeNode<T>>[] = [root];
  const res: T[] = [];

  let node: Maybe<BiTreeNode<T>> = null;

  // 实际上while循环中的顺序是“根右左”
  while (stack.length) {
    node = stack.pop()!;

    if (node) {
      res.push(node.value);
      stack.push(node.left);
      stack.push(node.right);
    }
  }

  // 所以需要反转一下
  return res.reverse();
}
