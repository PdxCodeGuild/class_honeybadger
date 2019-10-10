function combine(nums1, nums2) {
  let combine = []
  for (let i=0; i<nums1.length; ++i) {
    combine.push(nums1[i])
    combine.push(nums2[i])
    }
    return combine
}

console.log(combine(['a','b','c',],[1,2,3]))
