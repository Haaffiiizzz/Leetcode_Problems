/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let count = 0
    let proceed = true
    while (proceed) {
        let current = typeof args[count]
        if (current != "undefined") {
            count += 1
        } else {
            proceed = false
        }
        
    } return count
    
};

/**
 * argumentsLength(1, 2, 3); // 3
 */