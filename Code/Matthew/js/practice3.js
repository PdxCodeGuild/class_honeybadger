

function add(a, b) {
  return a + b
}
// console.log(add(5, 2)) // 7

function random_element(array) {
  let i = Math.floor(Math.random()*array.length)
  return array[i]
}

// console.log(random_element(['apples', 'bananas', 'pears'])) // could return 'apples', 'bananas' or 'pears'

function eveneven(nums) {
  let count = 0
  for (let i=0; i<nums.length; ++i) {
    if (nums[i] % 2 == 0) {
      ++count
    }
  }
  return count % 2 == 0
}

// console.log(eveneven([5, 6, 2])) // True
// console.log(eveneven([5, 5, 2])) // False

function print_every_other(nums) {
  // let i = 0
  // while (i < nums.length) {
  //   if (i%2 == 0) {
  //     console.log(nums[i])
  //   }
  //   ++i
  // }
  
  // let i = 0
  // while (i < nums.length) {
  //   console.log(nums[i])
  //   i += 2
  // }
  
  // for (let i=0; i<nums.length; ++i) {
  //     if (i%2 == 0) {
  //       console.log(nums[i])
  //     }
  // }
  
  for (let i=0; i<nums.length; i+=2) {
    console.log(nums[i])
  }
  
  
}
// print_every_other([0, 1, 2, 3, 4, 5, 6])


function reverse(nums) {
  
  nums = nums.slice(0)
  nums.reverse()
  return nums
  
  // let r = []
  // for (let i=nums.length-1; i>=0; --i) {
  //   r.push(nums[i])
  // }
  // return r
  
  // let r = []
  // for (let i=0; i<nums.length; ++i) {
  //   r.unshift(nums[i])
  // }
  // return r
  
}
// nums = [1, 2, 3, 4]
// console.log(reverse(nums))


function extract_less_than_ten(nums) {
  let lazy_array = []
  for (let i=0; i<nums.length; i++) {
    if (nums[i] < 10) {
      lazy_array.push(nums[i])
    }
  }
  return lazy_array
}

// console.log(extract_less_than_ten([2, 3, 11, 12]))


function common_elements(nums1, nums2) {
  let common = []
  for (let i=0; i<nums1.length; ++i) {
    for (let j=0; j<nums2.length; ++j) {
      // console.log(nums1[i] + ', ' + nums2[j])
      if (nums1[i] == nums2[j]) {
        common.push(nums1[i])
      }
    }
  }
  return common
}
console.log(common_elements([1, 2, 3, 4], [3, 4, 5, 6, 7])) // [3, 4]








