function myFunction(arr) {
  let result = {};
  for (let i = 0; i < arr.length; i++) {
    let currentWord = arr[i];
    let innerArr = [];
    let firstChar = currentWord[0].toLowerCase();
    if (result[firstChar] === undefined) {
      innerArr.push(currentWord);
      result[firstChar] = innerArr;
    } else {
      result[firstChar].push(currentWord);
    }
  }
  console.log(result);
  return result;
}

function sortByFirstChar(arr) {
  return arr.reduce((acc, cur) => {
    const firstLetter = cur.toLowerCase().charAt(0);
    return { ...acc, [firstLetter]: [...(acc[firstLetter] || []), cur] };
  }, {});
}

myFunction(["Alf", "Alice", "Ben"]);
myFunction(["Berlin", "Paris", "Prague"]);

sortByFirstChar(["Alf", "Alice", "Ben"]);
sortByFirstChar(["Berlin", "Paris", "Prague"]);
