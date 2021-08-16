/**
 * @param {number[]} prices
 * @return {number}
 */
 var maxProfit = function(prices) {
    
  if (prices.length < 2) {
      return 0;
  };
  
  let profits = [];
  
  for (let i = 0; i < prices.length - 1; i++) {
      
      //copy of original array to mutate
      let prices2 = [...prices];
      
      //buy price (shifts every time)
      let buy = prices[i];
      //console.log("Buy: " + buy);
      
      //splices array so only the days ahead will be included
      let futureDays = prices2.splice(prices.indexOf(buy), (prices2.length - prices.indexOf(buy)));
      
      let sell = Math.max(...futureDays);
      //console.log("Sell: " + sell);
      
      let profit = sell - buy;
      
      profits.push(profit);
      
      //console.log(profits);
      
  }
  
  return Math.max(...profits);

  
};