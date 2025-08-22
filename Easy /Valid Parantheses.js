/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // Stack to keep track of opening brackets
    let stack = [];
    // Object to hold the matching pairs
    let matchingBracket = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    
    // Iterate through each character in the string
    for (let char of s) {
        if (char in matchingBracket) {
            // Pop from stack if stack is not empty, else assign a dummy value '#'
            let topElement = stack.length > 0 ? stack.pop() : '#';
            // Check if the popped element matches the corresponding opening bracket
            if (matchingBracket[char] !== topElement) {
                return false;
            }
        } else {
            // It's an opening bracket, push to the stack
            stack.push(char);
        }
    }
    
    // Check if the stack is empty
    return stack.length === 0;
};
