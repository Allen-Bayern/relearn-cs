type Maybe<T> = T | null;

interface SingleNode<T = unknown> {
  value: T;
  next: Maybe<SingleNode<T>>;
}

interface BiNode<T = unknown> {
  value: T;
  prev: Maybe<BiNode<T>>;
  next: Maybe<BiNode<T>>;
}

export { Maybe, SingleNode, BiNode };
