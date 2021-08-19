/**
 * @param {number[]} nums
 * @return {number}
 */
 var missingNumber = function(nums) {
    
  let sorted = nums.sort(function(a, b){return a-b});
  
  console.log(sorted);
  
  for (let i = 0; i <= sorted.length; i++) {
      
      if (sorted[i] !== i) {
          return i;
      }
      
  }
  
};