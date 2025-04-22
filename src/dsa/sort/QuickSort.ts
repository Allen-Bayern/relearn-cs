function quickSort(list: number[]): number[] {
  if (list.length <= 1) {
    return [...list];
  }

  const pivot = list[0];
  const left = list.filter((x) => x < pivot);
  const middle = list.filter((x) => x === pivot);
  const right = list.filter((x) => x > pivot);

  return [...quickSort(left), ...middle, ...quickSort(right)];
}
