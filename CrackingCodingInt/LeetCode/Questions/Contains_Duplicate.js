/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
    
  let futureNums = [...nums];
  
  for (let i = 0; i < nums.length; i++) {
      
      let testNum = nums[i];
      
      futureNums.shift();
      
      if (testNum === nums[i + 1]) {
          return true;
      }
      
      if (futureNums.indexOf(testNum) >= 0) {
          return true;
      }
  }
  
  return false;
  
  
};