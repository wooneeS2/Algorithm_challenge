/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let newList  = nums1.slice(0,m).concat(nums2)
    
    newList = newList.sort((a,b)=>a-b)
   
    nums1.splice(0, m+n, ...newList);
};