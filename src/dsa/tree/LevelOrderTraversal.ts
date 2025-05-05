/**
 * @author Yuebing
 * @description 二叉树层序遍历
 */
import type { BiTreeNode, Maybe } from "../types";
import Queue from "yocto-queue";

/** 层序遍历 */
export const LevelOrder = <T = unknown>(root: Maybe<BiTreeNode<T>>): T[][] => {
  if (!root) {
    return [];
  }

  const queue = new Queue<BiTreeNode<T>>();
  queue.enqueue(root);

  const res: T[][] = [];

  while (queue.size) {
    const { size: times } = queue;
    const curLevel: T[] = [];

    for (let i = 0; i < times; i++) {
      const node = queue.dequeue();
      if (node) {
        curLevel.push(node.value);
      }
      if (node?.left) {
        queue.enqueue(node.left);
      }
      if (node?.right) {
        queue.enqueue(node.right);
      }
    }

    res.push(curLevel);
  }

  return res;
};
