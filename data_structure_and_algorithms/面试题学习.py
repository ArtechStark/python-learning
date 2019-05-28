
"""
1. (leetcode 20)判断大中小括号是否合法
只有一种经典的方法，即使堆栈的方法：
a. 左括号进来后压入栈底 push
b. 右括号进来查看堆栈栈顶是不是匹配的左括号(peek)，
如果匹配则把栈顶元素推出去(pop)，如果不匹配则返回不合法。
c. 最后，堆栈本身必须是空的。如果不为空，则返回不合法。

时间复杂度：每个元素进栈出栈的操作是O(1)，每个元素都会进入一次，所以是O(n)
空间复杂度：O(n)

还有一种思路比较简单的解法，从字符串里面找'()', '[]', '{}'一旦发现就删除掉，
然后继续这么做，直到最后字符串为空，就返回正确。但是时间复杂度平均是O(n^2 / 2)。
所以还是栈的方法好。
"""

def isValid(s):
    stack = []
    paren_map = {')':'(', ']':'[', '}':'{'}
    for c in s:
        if c not in paren_map:
            stack.append(c)
        elif not stack or paren_map[c] != stack.pop():
            return False
    return not stack

"""
2. (leetcode 232, 225)
2.1 stack -> queue
2.2 queue -> stack

2.1 只用先入后出的方法实现先入先出的效果。一个stack肯定不行，需要两个stack。
stack_in, stack_out
实现三个函数：进入队列push, 出队列pop, 查看peek
push时只从stack_in进, 只要遇到pop和peek操作，先查看stack_out里有没有。
如果有，就在stack_out里pop或peek就行；如果没有，就把所有stack_in的内容放到
stack_out里，然后stack_in清空，然后在stack_out里做pop或peek操作.

"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackin = []
        self.stackout = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stackin.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stackin and not self.stackout:
            return True
        else:
            return False


"""
3. (leetcode 703)
K largest. 流动的输入数据，最后返回第K大的值
solution 1: save k max，然后每次进来新的数，就在这K个数里面
进行排序，把最小的淘汰掉
假设总共N个数，则时间复杂度是O(N*K*logk)。因为每次排序最快是KlogK,总共N次

solution 2：优先队列
维护一个Min Heap（小顶堆），保证堆的元素个数为K。每次有元素进来，就和堆顶
的元素进行比较，如果比堆顶元素小，pass；如果比堆顶元素大，那么把堆顶踢掉，
新元素进来并调整堆(调整的时间复杂度是log2(k))。
时间复杂度O(N*1)~O(N*log2(k))
"""

class KthLargest(object):
    import heapq
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: list[int]
        """
        nums.sort()
        self.heap = nums[-k:]
        self.k = k
        heapq.heapify(self.heap)
    def add(self, val):
        """
        :type val: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]

"""
4. (leetcode 239) 
array sliding window max
sliding window是高频题
[1 3 -1 -3 5 3 6]
solution 1: priority queue
Max Heap
维护一个大顶堆元素个数等于窗口长度(O(logk))，结果就是堆顶元素(O(1))。
O(N*logk)
solution 2: queue
维护k个元素的双端队列(deque)
前K个元素依次加到队列里，后面维护队列。保证队列的最大值在左边,进来新的数如果最大，则删除6
时间复杂度O(N)
"""

def maxSlidingWindow(self, nums, k):
    if not nums: return [] #对参数进行判断，给面试官一个严谨的印象
    window, res = [], []  # window存下标，result存最后的结果
    for i, x in enumerate(nums):
        if i >= k and window[0] <= i-k:
            window.pop(0)
        while window and nums[window[-1]] <= x:
            window.pop()
        window.append(i)
        if i >= k-1:
            res.append(nums[window[0]])
    return res

"""
5. (leetcode 242) Valid Anagram
判断两个字符串是不是所有元素相同（比如"rat"和"tar"， 返回True）
solution 1: sort, 然后看是否相同
n*log(n)
solution 2: map 计数{'letter':count},然后比较两个map是否相同
map的插入、删除、查询都是O(1)，总共O(n)


"""
def isAnagram1(self, s, t):
    """
    用哈希表的方法(python字典是哈希表)
    """
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1 # 这里.get方法比直接用键索引的更好，
                                           # 因为后者没有的话会报错
    for item in t:
        dic2[item] = dic2.get[item, 0] + 1
    return dic1 == dic2

def isAnagram2(self, s, t):
    """
    相当于用列表自建了一个哈希表，这里的哈希函数就是
    每个字符的ASCII码减去'a'对应的ASCII码的结果。
    和用字典本质上一样的，都是哈希表
    """
    dic1, dic2 = [0]*26, [0]*26
    for item in s:
        dic1[ord(item)- ord('a')] += 1
    for item in t:
        dic2[ord(item) - ord('a')] += 1
    return dic1 == dic2



def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)


"""
6. (leetcode 1) two sum
只有一种可能，并且没有重复元素
solution 1: 枚举，两层循环 O(n^2)
solution 2: set. 一层循环枚举x，然后去set里查询有没有9-x。 O(n) * O(1) = O(n)

"""

def twoSum(nums, value):
    """
    nums: list of number
    value: number
    """
    dic = {}
    for i, x in enumerate(nums):
        if x not in dic:
            dic[value - x] = i
        else:
            return i, dic[x]

"""
7. (leetcode 15 3 sum，返回和为0的三个数的index.非常非常常见！) (leetcode 18 5 sum)

solution 1: 枚举。三重循环， O(n^3)
solution 2: 枚举+查询。两重循环，然后查询value-(a+b). O(n^2)
在这里也可以看出，map和set通常用来做查询和计数
solution 3: sort + find
整个数组排序，O(n*log(n))
第一层循环，枚举a，在剩下的数组里面找b和c
"""

def threeSum(nums):
    if len(nums) < 3:
        return None
    dic = {}
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if -nums[i]-nums[j] not in dic:
                dic[-nums[i]-nums[j]] = [i, j]
    for k in range(len(nums)):
        if nums[k] in dic:
            result = dic[nums[k]]
            result.append(k)
            result = [nums[x] for x in result]
            return result
def treeSum2(nums):
    if len(nums) < 3:
        return None
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        if i >= 1 and v == nums[i-1]:
            continue
        d = {}
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x] = 1
            else:
                res.add((v, -v-x, x))
    return res








if __name__ == "__main__":
    #s = input()
    
    # 1
    #print(isValid(s))

    # 2.1
    #x = 1
    #obj = MyQueue()
    #obj.push(x)
    #param_2 = obj.pop()
    #param_3 = obj.peek()
    #param_4 = obj.empty()

    print(threeSum([1, 2, 0, -1, 3, 4]))
    print(treeSum2([1, 2, 0, -1, 3, 4]))