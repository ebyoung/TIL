# Sorting Algorithm

## 개요

- 정렬 알고리즘
  - 데이터들이 주어졌을 때 정해진 순서대로 나열하는 알고리즘
- 정렬된 데이터의 특징
  - 어떤 임의의 값을 골랐을 때 그 값의 왼쪽에는 더 작은 값이, 오른쪽에는 더 큰 값이 위치
- 정렬의 목적
  - 이진 탐색과 같은 순차 탐색에 비해 훨씬 강력한 탐색 알고리즘을 활용하기 위해
- 분류
  - Stable: 동일한 값을 가지는 원소가 있을 때 정렬 후에 원래의 순서가 유지되는지 여부
    - Stable Sort: Bubble Sort, Insertion Sort, Merge Sort, Count Sort, Radix Sort, Tim Sort
    - Unstable Sort:  Quick Sort, Heap Sort
  - Comparison: 값의 비교를 통해 정렬하는지 여부
    - Comparison Sort: Quicksort, Heapsort, Shellsort, Merge sort, Insertion sort, Selection sort Bubble sort
    - Uncomparison Sort:  Counting sort, Radix sort
  - In place / Out of place: 정렬 시 입력된 데이터 리스트 외에 추가 메모리 공간이 필요한지 여부
    - In place: Bubble Sort, Selection Sort, Insertion Sort
    - Out of place: Shell Sort, Quick Sort, Merge Sort, Heap Sort, Counting Sort, Radix Sort



## 시간 복잡도

| 이름           | 최선         | 평균         | 최악         | 메모리     |
| -------------- | ------------ | ------------ | ------------ | ---------- |
| Bubble Sort    | *O(n)*       | *O(n^2)*     | *O(n^2)*     | *O(1)*     |
| Insertion Sort | *O(n)*       | *O(n^2)*     | *O(n^2)*     | *O(1)*     |
| Counting Sort  | *O(n+k)*     | *O(n+k)*     | *O(n+k)*     | *O(k)*     |
| Heap Sort      | *O(n)*       | *O(n log n)* | *O(n log n)* | *O(1)*     |
| Merge Sort     | *O(n log n)* | *O(n log n)* | *O(n log n)* | *O(n)*     |
| Quick Sort     | *O(n log n)* | *O(n log n)* | *O(n^2)*     | *O(log n)* |
| Tim Sort       | *O(n)*       | *O(n log n)* | *O(n log n)* | *O(n)*     |

- 버블 정렬과 삽입 정렬
  - 추가 메모리를 사용하지 않고 안정적
  - 평균 시간 복잡도가 *O(n^2)*로 매우 느린것이 단점
- 힙 정렬
  - 추가 메모리를 사용하지 않고 최악의 경우에도 *O(n log n*)으로 시간복잡도가 좋아보이지만 참조 지역성이 좋지 않은 정렬 방식이어서 실제 동작 시간은 생각보다 느릴 수 있음
  - 참조 지역성 원리
    - CPU는 미래에 원하는 데이터를 예측하여 속도가 빠른 장치인 캐시 메모리에 저장하는데 이때의 예측률을 높이기 위하여 사용하는 원리
    - 일반적으로 최근에 참조한 메모리나 그 메모리와 인접한 메모리를 다시 참조할 확률이 높아 이를 캐시 메모리에 저장해 놓고 빠르게 읽어올 수 있도록 하는 것
    - 따라서 시간 복잡도가 *O(n log n)*이라고 하면 실제로는 *C* **n log n*의 시간이 걸린다고 볼 수 있음
  - 힙 정렬은 한 위치에 있는 요소를 해당 요소의 인덱스 두 배 또는 절반인 요소와 비교하기 때문에 캐시 메모리에서 예측하기 어렵고, 따라서 *C*가 병합 정렬과 퀵 정렬에 비해 상대적으로 크다는 문제
- 병합 정렬
  - 인접한 덩어리를 병합하기 때문에 참조 지역성을 어느정도 만족하고 최악의 경우에도 *O(n log n)*으로 빠른 속도
  - 입력 배열의 크기만큼 추가 메모리를 사용한다는 단점 존재
- 퀵 정렬
  - pivot 주변에서 데이터의 위치 이동이 빈번하게 발생해 참조지역성이 좋기 때문에 힙 정렬과 병합 정렬보다 C의 값이 작고 평균 시간 복잡도는 셋 중에 가장 빠르다는 장점
  - 최악의 경우 *O(n^2)*가 될 수 있다는 단점 존재

- 팀 정렬
  - 실제로 사용되는 데이터는 이미 어느정도 정렬되어 있다는 점을 이용
  - 삽입 정렬과 병합 정렬을 결합
    - 삽입 정렬의 경우 인접한 데이터를 반복해서 비교하기 때문에 참조 지역성의 원리를 매우 잘 만족하며 퀵 정렬보다도 *C*값이 작다고 알려짐
    - 따라서 *n*의 크기가 작을 때는 *C×n^2*의 시간이 걸리는데도 불구하고 오히려 *C×n log n*의 시간이 걸리는 알고리즘 보다 빠를 수 있음
    - 병합 정렬의 안정적이면서 최악의 경우에도 *O(n log n)*을 보장하는 장점을 유지하면서 추가 메모리를 사용한다는 단점을 삽입정렬을 결합해 최대한 극복



## 구현

### 버블 정렬

- 인접한 두 개의 값을 비교해 왼쪽의 값이 더 크다면 교환, 아니면 지나가는 방식

  ```python
  def bubble_sort(arr):
      # len(arr)이 아닌 len(arr)-1인 이유는 j+1에서 index error를 막기 위함
      for i in range(len(arr)-1, 0, -1): # 정렬 구간의 끝
          for j in range(i):             # 비교 할 왼쪽 원소
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
  ```



### 선택 정렬

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

  ```python
  def selection_sort(nums):
      for i in range(len(nums)-1):        # 마지막 요소는 원소가 1개 있으니 정렬 할 필요가 없음
          min_idx = i                     # 최솟값에 해당하는 index를 i부터 시작 (0번 위치가 기준위치) -> 반복을 돌면서 자리가 하나씩 결정
          for j in range(i+1, len(nums)): # i 다음부터 보자 (i부터하면 불필요하게 한번 더 봐야하는 상황이 생김)
              if nums[min_idx] > nums[j]: # 내가 가진 최솟값(min_idx)보다 더 작다? 큰걸 뒤로 보낸다는 느낌으로!
                  min_idx = j             # 인덱스 갱신
  
          nums[i], nums[min_idx] = nums[min_idx], nums[i]  # i번째와 min_idx 위치를 교환 (교환은 마지막에 한번)
  ```



### 힙 정렬

- 선택 정렬과 유사하게 가장 작은 값의 원소를 찾아 맨 앞의 원소와 위치를 교환하는 방식이지만 최솟값을 찾을 때 힙 트리를 이용해 빠르게 값을 찾는 방식

  - 힙 트리: 완전 이진 트리의 일종으로 반정렬 상태를 유지하며 중복된 값을 허용
    - 반정렬 상태(느슨한 정렬 상태): 부모 노드와 자식 노드의 관계는 정해져 있지만(부모>=자식 또는 부모<=자식) 그 외에는 정해진 규칙이 없음
  - 최대 힙: 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리
  - 최소 힙: 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리
    - 배열을 통해 구현하며 부모 노드를 기준으로 왼쪽 자식의 인덱스는 (부모의 인덱스 × 2) 이고 오른쪽 자식의 인덱스는 (부모의 인덱스 × 2 + 1)의 형태
    - 최댓값을 찾고자 할 때는 최대 힙을 구성해 루트 노드를 확인하며 최솟값을 찾고자 할 경우에는 최소 힙을 구성해 루트 노드 확인
    - 힙에 새로운 요소가 들어오면 일단 힙의 마지막 노드에 삽입하고 부모 노드와 비교해 교환하는 과정을 힙의 성질을 만족시킬 때 까지 반복
    - 요소를 삭제 할 때는 루트 노드의 요소를 삭제하고 그 자리에 힙의 마지막 노드를 가져온 다음 자식 노드 중 더 큰 값(최소 힙의 경우 작은 값)과 비교해 교환하는 과정을 힙의 성질을 만족시킬 때 까지 반복

  ```python
  # 자식 노드들을 확인해 부모 노드보다 더 큰값이 있다면 교환
  def heapify(unsorted, index, heap_size):
      largest = index
      left_index = 2 * index + 1
      right_index = 2 * index + 2
      if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
          largest = left_index
      if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
          largest = right_index
      if largest != index:
          unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
          heapify(unsorted, largest, heap_size)
  
  def heap_sort(unsorted):
      n = len(unsorted)
      unsorted = [0] + unsorted # 인덱스를 편하게 사용하기 위해 1번 부터 시작
      for i in range(n // 2 - 1, -1, -1): # 자식노드가 없는 원소들을 확인 할 필요 없음
          heapify(unsorted, i, n)
      # 한번 힙이 구성되면 개별 노드는
      # 최악의 경우에도 트리의 높이(logn)
      # 만큼의 자리 이동을 하게 됨
      # 이런 노드들이 n개 있으므로 : O(nlogn)
      for i in range(n - 1, 0, -1):
          unsorted[1], unsorted[i] = unsorted[i], unsorted[1] # 루트 노드와 교환
          heapify(unsorted, 0, i)
      return unsorted
  ```

  ```python
  # 파이썬 라이브러리 활용
  import heapq
  
  def heapsort():
      h = []
      result = []
      for value in iterable:
          heapq.heappush(h, value)		# 단순히 원소들을 힙큐에 push 해줬다가
      
      for i in range(len(h)):
          result.append(heapq.heappop(h))	# pop으로 꺼내주면 됨
      
      return result
  ```

  



### 삽입 정렬

- k번째 원소를 1부터 k-1까지와 비교해 적절한 위치에 끼워넣고 그 뒤의 자료를 한 칸씩 뒤로 밀어내는 방식

- 자료구조에 따라선 뒤로 밀어내는데 걸리는 시간이 크며, 작은 값들이 뒤쪽에 몰려있으면 그만큼 시간 증가

- 이미 정렬된 데이터에 값을 하나씩 삽입하거나 제거하는 경우에 높은 효율

- 새로운 원소가 위치할 곳을 찾기 위해 이진 탐색을 활용하는 이진 삽입 정렬도 존재

  ```python
  def insertion_sort(array):
      for i in range(1, len(array)):
          for j in range(i, 0, -1):
              if array[j] < array[j-1]:
                  array[j], array[j-1] = array[j-1], array[j]
              else:
                  break
      
      return array
  ```

  



### 카운팅 정렬

- 데이터에 각 항목이 몇 개씩 있는지 확인해 

- 정수나 정수로 표현 가능한 자료에 대해서만 적용 가능

- 카운터 배열에 충분한 공간을 할당하기 위해 집합 내에 가장 큰 정수 확인 필요

- 시간 복잡도는 *O(n+k)*로 데이터의 길이 뿐 아니라 최대값의 크기도 영향

  ```python
  def counting_sort(arr: list, N: int):
      #1.
      # 카운팅하기 위한 배열 초기화
      counter = [0] * (max(arr)+1) # 최댓값 +1 (인덱스)
      result = [0] * N             # 배열 크기
  
      #2.
      # arr 안에 들어있는 숫자의 개수 카운팅
      for i in arr:
          counter[i] += 1
  
      #3.
      # 누적값 카운팅
      for i in range(1, len(counter)):
          counter[i] += counter[i-1]
  
      #4.
      # 기존 배열의 가장 뒤에 있는 원소(len(arr)-1)부터 시작해서
      # 정렬될 결과를 저장할 배열(result)에 쌓아가자
      for i in range(len(arr)-1, -1, -1):
          result[counter[arr[i]]-1] = arr[i]  # 위치 찾기
          counter[arr[i]] -= 1                # 같은 숫자가 왔을 때 더 하나 더 작은 위치에 놓이게 하기 위함!
  
      return result
  ```

  

### 병합 정렬

- 분할 정복 기법으로 *n*개의 데이터를 *n/2*개의 두 리스트로 나누는 과정(Divide)을 재귀적으로 실시해 각각의 개별 원소들로 나눈 뒤에 병합하는 방식

  - 1. 분할

   > ​			   24851637
   >
   > ​	  2485				1637
   >
   >   24		85		16		37
   >
   > 2	4	8	5	1	6	3	7

  - 2. Merge

   >   24        58		16		37
   >
   >   ​	  2457				1367
   >
   >   ​			  12345678

  ```python
  # 리스트를 합병하기 위한 함수
  def merge(left, right):
      result = []
      while len(left) > 0 or len(right) > 0:
          if len(left) > 0 and len(right) > 0:
              if left[0] <= right[0]:
                  result.append(left[0])
                  left = left[1:]
              else:
                  result.append(right[0])
                  right = right[1:]
          elif len(left) > 0:
              result.append(left[0])
              left = left[1:]
          elif len(right) > 0:
              result.append(right[0])
              right = right[1:]
      return result
  ```

  ```python
  # 리스트를 재귀적으로 분할한 뒤에 merge함수 호출
  def merge_sort(list):
      if len(list) <= 1:
          return list
      mid = len(list) // 2
      leftList = list[:mid]
      rightList = list[mid:]
      leftList = merge_sort(leftList)
      rightList = merge_sort(rightList)
      return merge(leftList, rightList)
  ```

  



### 퀵 정렬

- 병합 정렬과 마찬가지로 분할 정복 기법을 재귀적으로 실시하지만 정 가운데를 기준으로 분할하는 것이 아니라 pivot이라는 임의의 기준값을 사용해 분할

- pivot값을 선택하는 방식에 따라 성능이 달라지며 최악의 경우 모든 값이 한쪽에 몰려 시간복잡도가 *O(n^2)*이 될 수도 있음

  ```python
  def quick_sort(array, start, end):
      if start >= end:		# 원소가 1개인 경우 정렬 종료
          return
      
      pivot = start			# 첫 번째 값을 피벗으로 선택하는 방식, 가운데 값을 선택해도 됨
      left = start + 1		# 정렬되지 않은 부분의 첫 번째 인덱스
      right = end				# 정렬되지 않은 부분의 마지막 인덱스
      
      while left <= right:	# 피벗을 기준으로 작은 데이터들과 큰 데이터들로 구분
          while (left <= end) and (array[left] <= array[pivot]):
              left += 1		# 피벗보다 큰 데이터 탐색
              
          while (right > start) and (array[right] >= array[pivot]):
              right -= 1		# 피벗보다 작은 데이터 탐색
              
          if left > right:	# 엇갈린 경우 피벗 데이터를 사이로 이동
              array[right], array[pivot] = array[pivot], array[right]
          else:				# 엇갈리지 않은 경우 작은 데이터를 왼쪽, 큰 데이터를 오른쪽으로
              array[left], array[right] = array[right], array[left]
  	# 이후 양쪽 부분에 대해 각각 퀵 정렬 수행(현재 피벗 데이터는 right에 위치)
      quick_sort(array, start, right - 1) # 피벗의 왼쪽에 퀵 정렬
      quick_sort(array, right + 1, end)	# 피벗의 오른쪽에 퀵 정렬
  ```
  
  ```python
  # partition 함수를 따로 구현
  def partition(start, end, array):
       
      # Initializing pivot's index to start
      pivot_index = start
      pivot = array[pivot_index]
       
  
      while start < end:
          while start < len(array) and array[start] <= pivot:
              start += 1
               
          while array[end] > pivot:
              end -= 1
           
  
          if(start < end):
              array[start], array[end] = array[end], array[start]
       
      array[end], array[pivot_index] = array[pivot_index], array[end]
      
      return end
       
  # The main function that implements QuickSort
  def quick_sort(start, end, array):
       
      if (start < end):
          p = partition(start, end, array)
          quick_sort(start, p - 1, array)
          quick_sort(p + 1, end, array)
  ```
  
  

### 팀 정렬

- 병합 정렬의 과정에서 전체를 충분히 작은 덩어리로 나눈 뒤 삽입 정렬을 시행한 뒤에 병합

- 전체를 나눠서 정렬하는 병합 정렬의 특징과 *n*이 작을수록 높은 성능을 보이는 삽입 정렬의 특징을 이용

- *2^x*개씩 잘라 각각 삽입 정렬로 정렬하면 일반적인 병합 정렬보다 *x*개의 병합 동작이 생략되면서 동작 시간은 *Cm ×n(log n - x) + α*

- 이 때의 *x*값을 최대한 크게 하고 *α*값을 최대한 작게 하기 위한 최적화 기법들 존재

  1. 실생활의 데이터는 주로 어느정도 정렬되어 있다는 점을 이용해 처음 2개의 데이터를 비교해 보고 증가하는 **run**(하나의 덩어리) 또는 감소하는 **run**으로 정의
  2. *2^x*(**minrun**)개를 삽입 정렬을 진행해 하나의 **run**을 만들고 이후 증가하거나 감소하는 상태가 지속되면 그만큼 **run**에 포함시켜 **run**을 최대한 크게
     - 새로운 원소를 **run**에 추가할 때 이미 앞의 원소는 정렬되어 있기 때문에 이진 삽입 정렬을 활용
  3. 감소하는 **run**은 뒤집어서 증가하는 **run**으로 변환
  4. 이러한 **run**이 만들어 질 때 마다 스택에 저장
     - 이 때 스택의 제일 위의 **run**의 길이는 그 아래의 원소보다 작고, 위 두개의 **run**의 길이의 합은 세번째 **run**보다 작아야함
     - 만약 새로운 **run**이 들어왔는데 조건이 충족되지 않는다면 두번째 원소를 새로 들어온 원소와 세번째 원소 중 더 작은 원소와 병합하는 과정을 조건이 충족될 때 까지 반복
     - 이를 통해 스택에 저장된 **run**의 수를 작게 유지하고, 가능한 길이가 비슷한 **run**끼리 병합할 수 있게 됨
  5. 두개의 **run**을 병합할 때는 길이가 더 작은 **run**을 복사해 놓고 앞쪽부터 작은 값을 채우거나 뒤쪽 부터 큰 값을 채우는 방식
     - 이를 통해 최악의 경우에도 *n/2*만큼만 메모리를 사용해 병합 정렬보다 더 적은 메모리 사용
     - 병합하기 전에 다른 **run**의 최솟값보다 더 작은 구간과 최댓값보다 더 큰 구간은 정렬할 필요 없는 구간으로 설정해 나머지 구간만 정렬 진행
       - 이 경우도 탐색에 추가적인 시간이 소요되기 때문에 정렬할 필요가 없는 구간이 없다면 손해를 보게 되지만 실생활 데이터가 어느정도 정렬되어 있다는 점을 이용하는 것
     - Galloping: 두 **run** 중 한쪽의 원소가 연속적으로 선택되면 두 **run**이 차이가 크다고 가정하고 인덱스를 선형이 아니라 *2^i*으로 증가시키며 대소 비교를 진행

  ``` python
  MIN_MERGE = 32
   
  def calcMinRun(n):
      """Returns the minimum length of a
      run from 23 - 64 so that
      the len(array)/minrun is less than or
      equal to a power of 2.
   
      e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
      ..., 127=>64, 128=>32, ...
      """
      r = 0
      while n >= MIN_MERGE:
          r |= n & 1
          n >>= 1
      return n + r
   
   
  # This function sorts array from left index to
  # to right index which is of size atmost RUN
  def insertionSort(arr, left, right):
      for i in range(left + 1, right + 1):
          j = i
          while j > left and arr[j] < arr[j - 1]:
              arr[j], arr[j - 1] = arr[j - 1], arr[j]
              j -= 1
   
   
  # Merge function merges the sorted runs
  def merge(arr, l, m, r):
       
      # original array is broken in two parts
      # left and right array
      len1, len2 = m - l + 1, r - m
      left, right = [], []
      for i in range(0, len1):
          left.append(arr[l + i])
      for i in range(0, len2):
          right.append(arr[m + 1 + i])
   
      i, j, k = 0, 0, l
       
      # after comparing, we merge those two array
      # in larger sub array
      while i < len1 and j < len2:
          if left[i] <= right[j]:
              arr[k] = left[i]
              i += 1
   
          else:
              arr[k] = right[j]
              j += 1
   
          k += 1
   
      # Copy remaining elements of left, if any
      while i < len1:
          arr[k] = left[i]
          k += 1
          i += 1
   
      # Copy remaining element of right, if any
      while j < len2:
          arr[k] = right[j]
          k += 1
          j += 1
   
   
  # Iterative Timsort function to sort the
  # array[0...n-1] (similar to merge sort)
  def timSort(arr):
      n = len(arr)
      minRun = calcMinRun(n)
       
      # Sort individual subarrays of size RUN
      for start in range(0, n, minRun):
          end = min(start + minRun - 1, n - 1)
          insertionSort(arr, start, end)
   
      # Start merging from size RUN (or 32). It will merge
      # to form size 64, then 128, 256 and so on ....
      size = minRun
      while size < n:
           
          # Pick starting point of left sub array. We
          # are going to merge arr[left..left+size-1]
          # and arr[left+size, left+2*size-1]
          # After every merge, we increase left by 2*size
          for left in range(0, n, 2 * size):
   
              # Find ending point of left sub array
              # mid+1 is starting point of right sub array
              mid = min(n - 1, left + size - 1)
              right = min((left + 2 * size - 1), (n - 1))
   
              # Merge sub array arr[left.....mid] &
              # arr[mid+1....right]
              if mid < right:
                  merge(arr, left, mid, right)
   
          size = 2 * size
  ```

  



### 참고

https://jackpot53.tistory.com/98

https://namu.wiki/w/%EC%A0%95%EB%A0%AC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

https://d2.naver.com/helloworld/0315536
