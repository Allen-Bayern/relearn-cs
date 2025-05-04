import { Maybe } from "./helpers";

export interface SingleNode<T = unknown> {
  value: T;
  next: Maybe<SingleNode<T>>;
}

export interface BiNode<T = unknown> {
  value: T;
  prev: Maybe<BiNode<T>>;
  next: Maybe<BiNode<T>>;
}

export interface BiTreeNode<T = unknown> {
  value: T;
  left: Maybe<BiTreeNode<T>>;
  right: Maybe<BiTreeNode<T>>;
}
