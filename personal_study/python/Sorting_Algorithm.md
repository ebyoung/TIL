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





### 참고

https://jackpot53.tistory.com/98

https://d2.naver.com/helloworld/0315536
