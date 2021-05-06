
const oldArray = ["abode", "ABc", "xyzD"];
const test2 = ["abide", "ABc", "xyz"];
const test3 = ["IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"];

function alphaCount(word) {
    count = 0;
    const alpha = 'abcdefghijklmnopqrstuvwxyz'.split("");
    for (let i = 0; i < word.split("").length; i++) {
        word[i].toLowerCase() === alpha[i] ? count += 1 : count += 0;
        console.log(`finished iteration ${i}`)
    }
    return count
}
let newArray = test3.map(alphaCount);
console.log(newArray);
    // for i in len(word)
    // word[i] === alpha[i]
    // count += 1
    // counts.push(count)}
// console.log(alphaCount('abode'))