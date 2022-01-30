

# Python

## 1. 파이썬 기초

- 쉽다
- 크로스 플랫폼 언어

[toc]

### 개발환경

- 대화형
  - 기본 Interpreter(IDLE)
  - Jupyter Notebook - 실습
- 스크립트 실행 - 프로젝트, 평가
  - .py 파일 작성해 실행
  - IDE, 통합개발환경(Pycharm) - 알고리즘
    - 파이썬에 특화
  - Text editor(Visual Studio Code) - 웹, 실습
    - 모든 언어에 사용 가능한 텍스트 편집 툴



### 변수

- 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

  - 객체: 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것
  - 파이썬은 객체지향 언어로 모든것이 객체로 구현

- 언제든 변수에 다른 객체를 할당 해 참조하는 객체가 바뀔 수 있기 때문에 변수라고 불림

- 할당 연산자`=`를 통해 할당

- `type()` : 변수에 할당된 값의 타입

- `id()` : 변수에 할당된 객체의 고유한 아이덴티티 값이며, 메모리주소

- ```python
  x, y = 10, 20
  temp = x # 임시 변수 활용
  x = y
  y = temp
  print(x, y)
  ```

- ```python
  x, y = 10, 20
  y, x = x, y # Pythonic!
  print(x, y)
  ```



### 식별자

- 파이썬 객체의 이름
  - RedApple : CamelCase
  - red_apple : snake_case(파이썬에서 사용)
- 영문, _, 숫자로 구성
  - 첫 글자에 숫자는 불가
- 길이제한 없으며 대소문제 구별
- 키워드, 예약어는 사용 불가
- 내장함수나 모듈 이름 사용시 더이상 동작하지 않음



### 주석

- `#` , `"""` , `'''` , `ctrl + /`
- docstring



### 자료형

- None

- Boolean

  - True, False
    - 비어있는 값은 모두 False
    - ex) 0, 0.0, (), [], {}, '', None

- Numeric

  - int: 모든 정수, 오버플로우 발생하지 않음

    - 2진수: 0b
    - 8진수: 0o
    - 16진수: 0x

  - float: 정수가 아닌 모든 실수

    - 부동소수점

    - Floatint point rounding error 발생 가능

    - ```python
      a == b # 작은 오차 발생해 True가 나와야 하지만 False 나올 수 있음
      ```

      ```python
      abs(a - b) <= 1e-10 # 매우 작은 수 활용
      ```

      ```python
      import sys # 입실론 활용
      print(abs(a - b) <= sys.float_info.epsilon)
      print(sys.float_info.epsilon)
      ```

      ```python
      import math
      math.isclose(a, b)
      ```

  - complex

- String: 모든 문자

  - Immutable: 한글자만 할당 불가능

  - Iterable: 한글자씩 반복수행 가능

  - `''`, `""` 중 하나로 통일, `'''` 사용 가능

  - Escape sequence 사용

  - String Interpolation

    - %-formatting: 거의 대부분 프로그래밍 언어에서 사용되는 방식, `%s`, `%d`, `%f`

    - str.format()

    - f-strings: python 3.6 이상

      ``` python
      import datetime
      today = datetime.datetime.now()
      today(today)
      print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일')
      ```

      

### 컨테이너

- 시퀀스

  - 리스트 - Mutable
    - `[]`, `list()` 로 생성
    - 인덱스를 통해 접근 및 할당 가능(Positive Index: 0부터 시작, Negative Index: -1부터 시작)
  - 튜플 - Immutable
    - 인덱스로 접근은 가능하나 할당은 불가능
    - 일반적으로 파이썬 내부에서 활용
  - 레인지 - Immutable
    - `range(n)` : 0부터 n-1
    - `range(n, m)` : n부터 m-1
    - `range(n, m, s) ` : n부터 m-1까지 s씩 증가, n>m이면 s는 음수

- 비시퀀스

  - 세트 - Mutable

    - `{}` 또는 `set()` 로 생성, 빈 `{}` 는 딕셔너리로 인식되므로 값을 넣거나 `set()` 활용 

    - 중복 및 순서 없이, Immutable 객체만 참조 가능

    - 인덱스로 접근 불가

    - ```python
      my_list = ['서울', '서울', '대전', '광주']
      len(set(my_list)) # 중복 제거한 개수
      set(my_list) # 순서는 유지 안됨
      ```

  - 딕셔너리 - Mutable

    - `{}` 또는 `dict()` 로 생성
    - 순서 없이 `key:value` 쌍으로 이루어진 객체를 참조
    - key에는 Immutable만 가능,  value에는 모든 값 가능
    - key를 통해 value에 접근, 반대는 불가



### 형변환

- 암시적 형 변환(Implicit): 파이썬이 내부적으로 자료형을 변환
- 명시적 형 변환(Explicit): 사용자가 의도적으로 자료형 변환
- 컨테이너 간의 형 변환도 가능하나 range와 dict로는 불가능
  - dictionary를 다른 컨테이너로 변환할 때는 key만 가능



### 연산자

- 산술

- 비교

- 논리

  - and, or, not

  - 단축평가: 결과가 확실한 경우 두 번째 값은 확인하지 않음

    ```python
    a = 5 and 4 # 5(True)확인 -> 4(True)까지 확인해야 결과 확정
    print(a)	# 4
    
    b = 5 or 3  # 5(True)만 확인하면 전체 True 확정
    print(b)	# 5
    
    c = 0 and 5 # 0(False)만 확인하면 전체 False 확정
    print(c)	# 0
    
    d = 5 or 0  # 5(True)만 확인하면 전체 True 확정
    print(d)	# 5
    ```

    

- 복합

  - `+=`, `-=` ,연산과 대입이 동시에

- 멤버십

  - in, not in

- 식별

- 기타

  - 시퀀스형 연산자
    - 산술연산자
    -  `+` (연결), `*` (반복)
  - 인덱싱
  - 슬라이싱
    - Positive Index, Negative Index 혼용도 가능
    - `s[n:m:s]` : n번째 부터 m-1번째까지 s만큼 증가시키며
    - `s[:-1]` : 처음부터
    - `s[0:]` : 끝까지
    - `s[:]` : 처음부터 끝까지
    - `s[::-1]` : 처음부터 끝까지 역순

## 2. 제어문

### 제어문

- 파이썬은 기본적으로 위에서 아래로 코드를 실행
- 특정 상황에서 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어 필요
- 순서도로 표현 가능



### 조건문 

- 순서도에서 `◇` 모양

- 참/거짓을 판단할 수 있는 조건식과 함께 활용

  ```python
  if <condition> == True:
      # 조건식이 참일 때 실행
  else:
      # 조건식이 거짓일 때 실행
  ```

  ```python
  if <condition1>:
      # 조건식 1이 참일 때 실행
  elif <condition2>:
      # 조건식 2가 참일 때 실행
  elif <condition3>:
      # 조건식 3이 참일 때 실행
  else:	# else에는 절대로 조건식 들어가면 안됨
      # 조건식이 모두 거짓일 때 실행
  ```

- 조건 표현식

  - `<참일 때 실행> if <조건식> else <거짓일 때 실행>`

  

### 반복문

- while

  - 조건이 참인 경우 반복적으로 코드를 실행

  - 반드시 종료 조건 필요

  ```python
  while <condition>:
      <expression> # 조건식이 참인 경우 반복 실행
  ```

- for
  - 시퀀스를 포함한 Iterable인 객체의 요소를 모두 순회

  ```python
  for <variable> in <iterable>:
      # Iterable인 객체를 언패킹해 요소를 하나씩 변수에 대입
  ```
  - dictionary는 key를 순회
    - `dictionary.keys()` : key로 구성된 결과
    - `dictionary.values()` : value로 구성된 결과, 값을 활용해 key에 접근 불가
    - `dictionary.items()` : (key,value) 튜플로 구성된 결과

  - `enumerate(iterable, start = 0)` 

    - (index, value) 형태의 튜플 객체 반환

  - List Comprehension

    ```python
    my_list = [<expression> for <variable> in <iterable> if <condition>]
    
    # 풀어쓰면
    my_list = list()
    for <variable> in <iterable>:
        if <condition>:
            mylist.append(<expression>)
    ```

  - Dictionary Comprehension

    ```python
    {<key>:<value> for <variable> in <iterable> if <condition>}
    
    my_dict = dict()
    for <variable> in <iterable>:
        if <condition>:
            my_dict[<key>] = <value>
    ```

- 반복문 제어

  - break

    - 반복문 종료

    - `for + break + else` 사용 가능

      ```python
      for <variable> in <iterable>:
          if <condition>:
              break
      else:
          <expression> # break를 만나지 않으면 실행
      
      # for else 사용하지 않으면
      
      is_true = False # flag 변수
      
      for <variable> in <iterable>:
          if <condition>:
              is_true = True # break를 만나는 경우 flag를 True로 변경
              break
      
      if is_true:
          <expression> # break를 만나지 않으면 실행
      ```

  - continue

    - 이후 코드블록 수행하지 않고 condition으로 돌아감

  - pass

    - 아무것도 하지 않음
    - 특별히 할 일이 없을 때 자리를 채우는 용도
    - 반복문 아니어도 사용 가능



## 3. 함수

### 함수 기초

- 함수란 특정한 기능을 하는 코드의 묶음
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

- 종류
  - Built-in 함수
  - 표준 라이브러리
  - 사용자 함수(직접 정의)
- 반복을 피하기 위해 사용



### 기본 구조

- 선언과 호출

  - `def function(parameter):` 형태로 선언
  - `function(argument)` 형태로 호출
- 입력

  - **Parameter** vs **Argument**

    - parameter: 함수 내부에서 사용되는 식별자

    - argument: 함수를 호출 할 때 넣어주는 값

  - Positional Argument: 위치에 따라 전달
  - Keyword Argument: Keyword를 언급해 특정 Argument 전달
    - Keyword Argument 다음에 Positional Argument 활용 불가
  - Default Argument value: 기본값을 지정해 argument를 전달하지 않아도 값 설정 가능
  - `*args`: 정해지지 않은 개수의 Positional 인자를 packing해 전달
  - `**kwargs`: 정해지지 않은 개수의 Keyword Argument를 딕셔너리 형태로 전달
- 결과

  - `return`문을 통해 값 반환하고 바로 함수 종료
  - `return`문이 없을 경우 `None`반환
  - 두개 이상의 값을 반환할 경우 하나의 튜플로 반환

### 함수의 범위

1. **L**ocal scope: 함수 내부
   - 함수가 호출된 이후 부터 종료될 때까지 유지
2. **E**nvelope scope: 특정 함수의 상위 함수
   - 해당 함수가 호출된 이후 부터 종료될 때까지 유지
3. **G**lobal scope: 코드 어디서든 참조할 수 있는 공간
   - 모듈이 호출된 시점 이후부터 인터프리터가 끝날 때까지 유지
4. **B**uilt-in scope: 파이썬 내장 함수 또는 속성
   - 실행 된 이후부터 영원히 유지

- 상위 변수에 접근은 가능하나 수정은 불가
- 상위 변수를 수정하기 위해서는 global 또는 nonlocal로 선언
  - global문
    - 현재 코드블록 전체에 적용되며, 나열된 식별자는 global 변수로 사용
    - global에 나열된 식별자는 같은 코드 블록에서 global 앞에 등장 불가
    - global에 나열된 식별자는 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
  - nonlocal문
    - global을 제외하고 가장 가까운 scope의 변수를 연결
    - global에 나열된 식별자와 같은 조건 가짐
    - global과 달리 이미 존재하는 식별자와의 연결만 가능
- `globals()`, `locals()`
  - `locals()`: 실행되는 함수 내의 namespace들을 딕셔너리로 정리
  - `globals()`: **LGB** 정보 모두 딕셔너리로 정리

### 문서화

- Docstring: `'''`안에 작성`'''`
- Naming Convention
  - 일반적으로 snake_case
  - 클래스 및 예외의 이름은 PascalCase
  - 상수 이름은 전체를 대문자




### 함수 응용

- zip(*iterables)

  - 여러 iterable을 모아 튜플을 원소로 하는 zip object 반환

- lambda 함수

  - **`lambda`**` [parameter] : <expression>`
  - 표현식을 계산한 결과값을 반환
  - return문을 가질 수 없음
  - 간편 조건문 외의 조건문이나 반목문을 가질 수 없음
  - `def`없이도 간결하게 사용 가능

- 재귀 함수

  - 자기 자신을 호출

  - 알고리즘 중 재귀로 표현하는것이 자연스러운 경우 존재

  - 변수의 사용이 줄어들며 가독성 향상

  - 1개 이상의 base case가 존재하여 수렴하도록 작성해야 무한한 호출이 이루어지지 않음

    ```python
    def recursive_function(parameter):
        if base_case:
            return result
        else:
    	    return recursive_function()
    ```

    - 이런 형태로 사용

  - base case에 도달할 때까지 함수를 호출

  - 메모리 스택이 넘치는것을 방지하기 위해 최대 깊이가 1000번으로 설정되어 이를 넘어가면 RecursionError 발생

  - 최대 깊이 변경 가능

    ```python
    import sys
    sys.setrecursionlimit(max_depth)
    ```

  - 함수를 호출 스택에 쌓아두고 마지막으로 호출된 함수부터 실행하기 때문에 반복문에 비해 속도가 느림
  - 재귀로 표현 가능한 경우는 반복문으로도 처리 가능



## 4. 모듈

### 모듈과 패키지

- 모듈: 특정 기능을 하는 코드를 **.py**단위로 작성한 것

- 패키지: 여러 모듈 및 서브패키지 들의 집합

- `from` `import` 문을 활용해 불러옴

  - `from package import *`: 모든 하위 기능 불러옴

- 패키지 관리자(pip)

  - PyPI(Python Package Index)에 저장된 외부 패키지 설치해주는 패키지 관리 시스템

    - bash, cmd 환경에서 사용

      ```bash
      $ pip install Packge==Version
      $ pip uninstall Package
      $ Pip list
      $ pip show Package
      $ pip freeze > requirements.txt
      $ pip install -r requirements.txt
      ```

- 패키지의 모든 폴더에는 `__init__.py` 파일 필요



### 가상환경

- 복수의 프로젝트를 할 때 필요한 패키지 버전이 상이한 경우 프로젝트 마다 독립적으로 패키지 관리 가능

  ```bash
  $ python -m venv <경로> # 가상 환경 생성
  $ source <경로> /Scripts/activate # 활성화
  $ deactivate # 비활성화
  ```

  

## 5. 데이터 구조

### 데이터 구조

- `dir()` 사용하면 컨테이너가 가지고 있는 메서드 확인 가능

- mutable 객체의 경우 메서드를 통해 값을 직접 변경하거나 함수를 통해 변경된 값 반환

- immutable 객체의 경우 변경된 값을 반환하는 경우만 가능

  

### 복사 방법

- 할당

  - `original_list = copy_list`
  - 대입 연산자 사용해 할당
  - 객체 참조를 복사하기 때문에 동일한 객체를 참조하게 됨

- 얕은 복사

  ```python
  original_list = copy_list[:]
  original_list = list(copy_list)
  
  from copy import copy
  original_list = copy(copy_list)
  ```

  - 객체 내부의 원소들을 복사
  - 원소가 또 다른 객체를 참조할 경우 객체 참조를 복사

- 깊은 복사

  ```python
  from copy import copy
  original_list = deepcopy(copy_list)
  ```

  - 새로운 객체를 만들고 원본 객체 내에 있는 객체에 대한 복사를 재귀적으로 삽입



## 6. 에러와 예외 처리

### 디버깅

- 방법
  - `print()`활용
  - 개발 환경 등에서 제공하는 기능 활용
  - Python tutor 활용
  - 뇌컴파일, 눈디버깅
- 에러 메시지
  - 해당 하는 위치를 찾아 메시지를 해결
- 로직 에러
  - 명시적인 에러 메시지 없이 예상과 다른 결과가 나오는 경우



### 에러와 예외

- Syntax Error

  - 잘못된 문법을 작성한 경우
  - `^`(캐럿, caret) 기호를 통해 발생한 위치 표현
  - EOL: End of Line
  - EOF: End of FIle

- Exception

  - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
  - 모든 내장 예외는 Exception Class를 상속받음
  - 사용자 정의 가능(PascalCase로 정의)

- 내장 예외 계층 구조

  - **BaseException**

    - **KeyboardInterrupt**: 임으로 프로그램을 종료

    - **Exception**

      - **AttributeError**
      - **ArithmeticError**
        - **ZeroDicisionError**: 0으로 나눌 때 발생
      - **EOFError**
      - **NameError**: namespace에서 이름을 찾을 수 없는 경우
      - **LookupError**
        - **IndexError**: 인덱스가 존재하지 않거나 범위를 벗어나는 경우
        - **KeyError**: 키가 존재하지 않는경우
      - **StopIteration**
      - **OSError**
      - **TypeError**: 자료형이 올바르지 않거나 인자가 잘못 전달된 경우
      - **ValueError**: 자료형은 올바르나 값이 적절하지 않거나 없는 경우

      - **ImportError**: 모듈은 있으나 존재하지 않는 클래스 또는 함수를 가져오는 경우
        - **ModuleNotFoundError**: 존재하지 않는 모듈을 `import`하는 경우
      - **SyntaxError**
        - **IndentationError**: 들여쓰기가 잘못된 경우



### 예외 처리

```python
try:
    <expression> # 일단 실행
except (<Error1>, <Error2>): # 여러 개의 예외 지정 가능
	<expression>
except <Error3> as <variable1>: # as는 선택, 원본 에러 메시지를 변수에 담아 사용 가능
    <expression> # try 문에서 해당 예외가 발생 시 실행
except <Error4> as <variable2>: # 위에서 부터 순차적으로 수행되기 때문에 가장 작은 범주부터 처리
    <expression>
else: # 모든 except 절 뒤에 와야 함
    <expression> # try 문에서 예외가 발생하지 않으면 실행
finally: # 선택적, 반드시 실행돼야 하는 코드가 있을 경우
    <expression> # 예외 발생 여부와 관계없이 항상 실행
    
raise <Error>('message') # 예외 강제 발생
assert <boolean expression>, 'message' # 표현식이 False 인 경우 AssertionError 발생
# 일반적으로 상태를 검증해 디버깅하는 용도로 사용
```

```bash
$ python -O filename.py # -O(대문자 O) 옵션으로 실행하면 assert문과 __debug__에 따른 조건부 코드 제거 후 실행
```



## 객체 지향 프로그래밍(OOP)

### 객체 지향 프로그래밍

- 객체는 특정 타입의 인스턴스
  - 타입(type): 사용 가능한 연산자와 method를 결정
  - 속성(attribute): 특정 클래스의 객체들이 가지는 상태 또는 데이터
  - 기능(method): 특정 클래스의 객체에 공통적으로 적용 가능한 함수
- 객체 지향 프로그래밍이란 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 것
  - 현실 세계를 추상화해 프로그램 설계에 반영
- 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 사용
- 프로그래밍을 더 배우기 쉽게 하고, 유지보수를 간편하게 하며, 직관적인 분석을 가능하게 함



### OOP 기초

- 기본 문법

  ```python
  class MyClass: # 클래스 정의, 클래스 명은 PascalCase
      
      def __init__(self, name): # 생성자
          self.name = name # 인스턴스 변수
      
      def my_method(self): # self대신 다른 변수명 쓸 수는 있지만 하면 안됨
          pass
  
  my_instance = MyClass() # 인스턴스 생성, 인스턴스 명은 snake_case
  my_instance.my_method() # 메서드 호출
  my_instance.my_attribute # 인스턴스 변수 접근
  ```

- 클래스틑 객체들의 분류이며 인스턴스는 각각의 실체
- 객체 비교
  - `==`: 변수가 참조하는 객체의 내용이 같으면 True
  - `is`: 변수가 동일한 객체를 가리키면 True



### 인스턴스

- 인스턴스 변수: 인스턴스가 가지고 있는 attribute 또는 고유한 변수
- 인스턴스 메서드
  - 인스턴스 변수를 사용하거나 인스턴스 변수에 값을 설정하는 메서드
  - 클래스 내부에 정의되는 메서드의 기본
  - 호출 시, 첫번째 인자로 인스턴스 자기 자신(self)이 자동으로 전달됨
  - 동일한 객체에 정의된 속성 및 다른 메서드에 자유롭게 접근 가능하며 클래스 자체에도 접근 가능
  - 그 외에는 함수와 동일
- 매직 메서드
  - `__`(Double underscore, Dunder bar)가 있는 특수한 동작을 위해 만들어진 메서드
  - 특정 상황에 자동으로 호출
  - 생성자 메서드(`__init(self)__`)
    - 인스턴스 객체가 생성될 때 자동으로 호출
    - 인스턴스 변수들의 초깃값을 설정
  - 소멸자 메서드(`__del(self)__`)
    - 인스턴스 객체가 소멸(주로 `del` 문을 통해)되기 직전에 호출되는 메서드
  - 그 외
    - `__str__(self)`: `print()`를 통해 출력될 때
    - `__repr__(self)`: 내부적으로 호출되어 객체를 형식적으로 표현, 쥬피터에서 반환값을 보여줄 때도 사용
    - `__len__(self)`: `len()`을 구현하기 위해 호출
    - `__lt__(self)`: <
    - `__le__(self)`: <=
    - `__eq__(self)`: ==
    - `__gt__(self)`: >
    - `__ge__(self)`: >=
    - `__ne__(self)`: !=



### 클래스

```python
class MyClass:
    class_variable = <값, 변수> # 클래스 변수
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def my_method(cls): # cls대신 다른 변수명 쓸 수는 있지만 하면 안됨
        pass
    
    @staticmethod
    def my_static_method(): # 꼭 인자를 넘겨줘야 하는건 아님
        pass
    
MyClass.class_variable # 클래스 변수 접근
```

- 클래스 변수: 클래스의 attribute
  - 한 클래스 내의 모든 인스턴스가 같은 값 공유
  - 클래스 선언 내부에서 정의
- 클래스 메서드:
  - `@classmethod` 데코레이터로 정의
    - 데코레이터
    - 일급 객체로 함수를 인자로 넣을 수 있고, 매개변수로 사용하거나 반환값으로 설정할 수 있음
    - 함수를 다른 함수로 꾸며 추가적인 기능을 부여
  - 호출 시, 첫번째 인자로 클래스(cls) 자동으로 전달
  - cls 인자에만 접근할 수 있기 때문에 객체 인스턴스의 attribute를 수정할 수 없음
- 스태틱 메서드
  - 매개변수를 받을 수 있음
  - 인스턴스 변수나 클래스 변수를 다루지 않고 단지 기능만을 하는 메서드
  - 클래스의 이름공간에 귀속되어 해당 클래스만 사용하는 함수
  - 호출 시 어떤 인자도 자동으로 전달되지 않아 클래스 정보에 접근하거나 수정 불가능
- 이름 공간
  - 인스턴스에서 특정 속성에 접근하면 인스턴스 -> 클래스 순으로 탐색



### 객체지향의 핵심

- 추상화

  - 현실 세계를 프로그램 설계에 반영

- 상속

  ```python
  class ParentClass1:
      def __init__(self, arg1):
          self.arg1 = arg1
  
  class ChildClass(ParentClass1, ParentClass2):# 다중 상속 시 상속 순서 중요
      def __init__(self, arg1, arg2, arg3):
          super().__init__(arg1) # 부모 클래스의 요소 호출
  		self._arg2 = arg2 # Protected
          self.__arg3 = arg3 # Private
      
      @property
      def arg2(self):
          return self._arg2
      
      @arg2.setter
      def arg2(self, new):
          self._arg2 = new
          
  parent_instance = ParentClass1()
  child_instance = ChildClass()
  print(isinstance(child_instance, ParentClass1)) # True: 클래스의 instance이거나 subclass 인 경우
  print(isinstance(parent_instance, ChildClass)) # False
  
  print(issubclass(ChildClass, ParentClass1)) # True: 클래스의 subclass인 경우
  print(issubclass(ChildClass, (ParentClass1, ParentClass2))) # 튜플로 전달하면 모든 항목 검사
  ```

  - 두 클래스 사이 부모 자식 관계를 정립
  - 모든 파이썬 클래스는 object를 상속 받음
  - 하위 클래스는 상위 클래스에 정의된 요소들을 모두 상속 받기 때문에 코드의 재사용성 향상
  - 상속 관계에서의 이름 공간은 인스턴스, ChildClass, ParentClass1, ParentClass2 순서로 탐색
    - mro 메서드로 확인 가능(Method Resolution Order)

- 다형성(Polymorphism)

  - 동일한 메서드도 서로 다른 클래스에 속해 있다면 다른 방식으로 작동 가능
  - 메소드 오버라이딩: 부모 클래스에 정의된 메서드를 자식 클래스에서 재정의
    - 이름과 기본 기능은 그대로 사용하고 특정 기능만 변경할 때 사용
    - `super()`를 활용해 부모 클래스의 메소드 실행 가능

- 캡슐화

  - 객체의 일부 구현 내용에 대한 외부로부터 직접적인 접근 차단
  - 파이썬에서 암묵적으로만 존재하고 실제로 접근을 차단하지는 않음
  - Public Acces Modifier
    - 대부분의 메서드나 속성
    - 어디서나 호출 가능하고 하위 클래스 오버라이딩 허용
  - Protected Acces Modifier
    - `_`로 시작하는 메서드나 속성
    - 부모 클래스 내부와 자식 클래스에서만 호출 가능
      - 외부에서도 호출 가능하지만 하면 안됨
    - 하위 클래스 오버라이딩 허용
  - Private  Acces Modifier
    - `__`로 시작하는 메서드나 속성
    - 본 클래스 내부에서만 사용 가능
    - 하위 클래스 상속 및 호출 불가능
      - AttributeError 발생
    - 외부 호출 불가능
      - 오류 발생
      - `my_instance._MyClass__attribute` 와 같이 접근 가능하지만 하면 안됨
  - getter
    - 변수의 값을 읽는 메서드
    - `@property` 데코레이터 사용
  - setter
    - 변수의 값을 설정하는 메서드
    - `@<variable>.setter` 데코레이터 사용
