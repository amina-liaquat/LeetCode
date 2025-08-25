function interpret(command) {
  let ans = "";

  let i = 0;
  while (i < command.length) {
    if (command[i] === "G") {
      ans += "G";
      i++;
    } else if (command[i] === "(" && command[i + 1] === ")") {
      ans += "o";
      i += 2;
    } else if (
      command[i] === "(" &&
      command[i + 1] === "a" &&
      command[i + 2] === "l" &&
      command[i + 3] === ")"
    ) {
      ans += "al";
      i += 4;
    } else {
      i++;
    }
  }

  return ans;
}


let command = "G()(al)";
console.log(interpret(command));
