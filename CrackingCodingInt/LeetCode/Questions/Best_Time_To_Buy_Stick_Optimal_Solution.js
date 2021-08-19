/**
 * @param {number[]} prices
 * @return {number}
 */
 var maxProfit = function(prices) {
    
    //set the min as the maximum value
    let min = Number.MAX_VALUE;
    //initialize max profit as 0
    let max = 0;
    
    //go through each price in the array
    for (let i = 0; i < prices.length; i++) {
        //if the next price in the array is below the minimum, set the price as the new minimum
        if (prices[i] < min) {
            min = prices[i];
        // else, if the new price - the minimum is higher than the maximum stored profit, set the new profit as the max profit
        } else if (prices[i] - min > max) {
            max = prices[i] - min;
        }
        //if neither of these conditions are true that means there is no maximum profit so the function returns 0
    }
    
    return max;

    
};