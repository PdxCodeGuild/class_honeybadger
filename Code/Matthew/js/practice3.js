

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
// console.log(common_elements([1, 2, 3, 4], [3, 4, 5, 6, 7])) // [3, 4]




function combine(nums1, nums2) {
  let length = Math.min(nums1.length, nums2.length)
  let combined = []
  for (let i=0; i<length; i++) {
    combined.push(nums1[i])
    combined.push(nums2[i])
  }
  return combined
}
// console.log(combine(['a','b','c'],[1,2,3])) // ['a', 1, 'b', 2, 'c', 3]


function combine2(nums1, nums2) {
  if (nums1.length > nums2.length) {
    let t = nums1
    nums1 = nums2
    nums2 = t
  }
  let combined = []
  for (let i=0; i<nums1.length; i++) {
    combined.push(nums1[i])
    combined.push(nums2[i])
  }
  for (let i=nums1.length; i<nums2.length; ++i) {
    combined.push(nums2[i])
  }
  return combined
}
// console.log(combine2(['a','b','c'],[1,2,3,4,5,6])) // ['a', 1, 'b', 2, 'c', 3, 4, 5, 6]

function find_pair(nums, target) {
  for (let i=0; i<nums.length; ++i) {
    for (let j=i+1; j<nums.length; ++j) {
      if (nums[i] + nums[j] == target) {
        return [nums[i], nums[j]]
      }
    }
  }
  return null
}
// console.log(find_pair([5, 6, 2, 3], 7)) // [5, 2]

function merge(nums1, nums2) {
  let merged_array = []
  let length = Math.min(nums1.length, nums2.length)
  for (let i=0; i<length; ++i) {
    merged_array.push([nums1[i], nums2[i]])
  }
  return merged_array
}
// console.log(merge([5,2,1], [6,8,2])) // [[5,6],[2,8],[1,2]]


function combine_all(arrays) {
  let merged2 = []
  for (let i=0; i<arrays.length; ++i) {
    for (let j=0; j<arrays[i].length; ++j) {
      merged2.push(arrays[i][j])
    }
  }
  return merged2
}
// console.log(combine_all([[5,2,3],[4,5,1],[7,6,3]])) // [5,2,3,4,5,1,7,6,3]


function fibonacci(n) {
  let fibi = [1, 1]
  for (let i=2; i<n; ++i) {
    // console.log(i + ' ' + fibi[i-2] + '+' + fibi[i-1] + ' = ' + (fibi[i-2] + fibi[i-1]))
    fibi.push(fibi[i-2] + fibi[i-1])
    // console.log(fibi)
  }
  return fibi
}
// console.log(fibonacci(8)) // [1, 1, 2, 3, 5, 8, 13, 21]

function fibonacci2(n) {
  num1 = 1
  num2 = 1
  for (let i=0; i<n-2; ++i) {
    num3 = num1 + num2
    num1 = num2
    num2 = num3
  }
  return num2
}
// console.log(fibonacci2(10))


function minimum(nums) {
  let running_min = nums[0]
  for (let i=0; i<nums.length; ++i) {
    if (nums[i] < running_min) {
      running_min = nums[i]
    }
  }
  return running_min
}

function maxmimum(nums) {
  let running_max = nums[0]
  for (let i=0; i<nums.length; ++i) {
    if (nums[i] > running_max) {
      running_max = nums[i]
    }
  }
  return running_max
}

function mean(nums) {
  let running_total = 0
  for (let i=0; i<nums.length; ++i) {
    running_total += nums[i]
  }
  return running_total / nums.length
}
function median(nums) {
  nums.sort((a, b) => a - b)
  if (nums.length % 2 == 1) {
    let middle = Math.floor(nums.length / 2)
    return nums[middle]
  } else {
    let middle = nums.length / 2
    // console.log('='.repeat(10))
    // console.log(nums)
    // console.log(middle)
    // console.log(nums[middle])
    // console.log('='.repeat(10))
    return (nums[middle] + nums[middle-1]) / 2
  }
}
function mode(nums) {
  let map = {}
  let count = 0
  for (let i=0; i<nums.length; ++i) {
    if (!map[nums[i]]) {
      map[nums[i]] = 1
    } else {
      map[nums[i]] += 1
    }
  }
  let max_value = 0
  let max_count = 0
  for (num in map) { // iterate over the properties/keys of the object/dictionary
    let count = map[num]
    // console.log(num, count)
    if (count > max_count) {
      max_count = count
      max_value = num
      // console.log('\t' + max_value + ' ' + max_count)
    }
  }
  return parseInt(max_value)
}

// let f = (a, b) => a + b
// let f = function(a, b) {
//   return a + b
// }


let nums = [12, 24, 24, 35, 88, 88, 120, 120, 120, 155, 155] //[12, 24, 35, 24, 88, 120, 155, 88, 120, 155, 120]
// console.log(nums)
// console.log(minimum(nums))
// console.log(maxmimum(nums))
// console.log(mean(nums))
// console.log(median(nums))
// console.log(mode(nums))



function find_unique(nums) {
  let nicoles_array = []
  for (let i=0; i<nums.length; ++i) {
    if (!nicoles_array.includes(nums[i])) {
      nicoles_array.push(nums[i])
    }
  }
  return nicoles_array
}


console.log(find_unique(nums)) // [12, 24, 35, 88, 120, 155]


