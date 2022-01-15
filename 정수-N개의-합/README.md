# [Bronze II] 정수-N개의-합 - 15596 

[문제 링크](https://www.acmicpc.net/problem/15596) 

### 성능 요약

메모리: 383960 KB, 시간: 168 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

작성해야 하는 함수는 다음과 같다.


 C, C11, C (Clang), C11 (Clang): long long sum(int *a, int n);

 
  a: 합을 구해야 하는 정수 n개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
  n: 합을 구해야 하는 정수의 개수
  리턴값: a에 포함되어 있는 정수 n개의 합
 
 
 C++, C++11, C++14, C++17, C++ (Clang), C++11 (Clang), C++14 (Clang), C++17 (Clang): long long sum(std::vector<int> &a);
 
  a: 합을 구해야 하는 정수 n개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
  리턴값: a에 포함되어 있는 정수 n개의 합
 
 
 Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
 
  a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
  리턴값: a에 포함되어 있는 정수 n개의 합 (정수)
 
 
 Java: long sum(int[] a); (클래스 이름: Test)
 
  a: 합을 구해야 하는 정수 n개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
  리턴값: a에 포함되어 있는 정수 n개의 합
 
 
 Go: sum(a []int) int
 
  a: 합을 구해야 하는 정수 n개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
  리턴값: a에 포함되어 있는 정수 n개의 합


