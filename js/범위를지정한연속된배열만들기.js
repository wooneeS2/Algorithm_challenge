function myFunction(min, max) {
  return Array(max - min + 1)
    .fill(min)
    .map((x, y) => x + y);
}
