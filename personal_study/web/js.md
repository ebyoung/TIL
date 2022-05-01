# JavaScript

[toc]

## 1. 브라우저

### 브라우저에서 할 수 있는 일

- DOM(Document Object Model) 조작
  - DOM이란 HTML, XML과 같은 문서를 다루기 위한 프로그래밍 인터페이스
  - 문서를 구조화하고, 구조화된 구성 요소를 하나의 객체로 취급하며 다루는 논리적 트리 모델
  - 문서가 객체로 구조화되어 있어 key로 접근 가능
  - 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
  - 주요 객체
    - window: DOM을 표현하는 창(브라우저 탭), 최상위 객체
    - document: 페이지 컨텐트의 Entry Point 역할을 하며 `<head>`, `<body>` 등과 같은 수많은 다른 요소들을 포함
    - navigator, location, history, screen
  - 파싱: 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
- BOM(Browser Object Model) 조작
  - 자바스크립트가 브라우저와 소통하기 위한 모델
  - 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
    - 버튼, url 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
  - window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)을 지칭
- JavaScript Core(ECMAScript)
  - 브라우저(DOM, BOM)을 조작하기 위한 명령어 약속(언어)



### DOM 조작

- Document는 문서 한 장(HTML)에 해당하고 이를 조작하는 것



#### DOM 관련 객체의 상속 구조

> EventTarget -> Node -> Element -> HTMLElement
>
> ​									  -> Document

- EventTarget: Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
- Node: 여러 가지 DOM 타입들이 상속하는 인터페이스
- Element: Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
  - 부모인 Node와 그 부모인 EventTarget의 속성을 상속
- Document: 브라우저가 불러온 웹 페이지를 나타냄
  - DOM 트리의 진입점(Entry Point) 역할을 수행
- HTMLElement: 모든 종류의 HTML 요소
  - 부모 element의 속성 상속



#### 조작 순서

1. 선택(Select)

   - `document.querySelector(selector)`
     - 제공한 선택자와 일치하는 element 하나 선택
     - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null)
   - `document.querySelectorAll(selector)`
     - 제공한 선택자와 일치하는 여러 element를 선택
     - 매칭 할 하나 이상의 셀렉터를 포함하는 유요한 CSS selector를 인자로 받음
     - 지정된 셀렉터에 일치하는 NodeList 반환
   - `getElementById`, `getElementByTagName`, `getElementByClassName` 등도 사용 가능
     - `getElementById`: id값은 고유하기 때문에 단일 element 반환
     - `getElementByTagName`, `getElementByClassName`: HTMLCollection 반환
     - id, class, tag 선택자 등을 모두 사용 가능해 더 구체적이고 능동적으로 선택 가능한 `querySelector`를 주로 사용

   | HTMLCollection                                     | NodeList                                                     |
   | -------------------------------------------------- | ------------------------------------------------------------ |
   | name, id, index 속성으로 각 항목에 접근 가능       | index로만 각 항목에 접근 가능<br />대신 `forEach`메서드 및 다양한 메서드 사용 가능 |
   | Live Collection으로 DOM의 변경사항 실시간으로 반영 | `querySelectorAll()`에 의해 반환되는 NodeList의 경우<br />Static Collection으로 실시간으로 반영되지 않음 |

2. 변경(Manipulation)

   - `document.createElement(tag)`
     - 작성한 태그 명의 HTML 요소를 생성하여 반환
   - `Element.append()`
     - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 **Node 객체나 DOMString**을 삽입
     - 여러 개의 Node 객체, DOMString을 추가 할 수 있음
     - 반환 값이 없음
   - `Node.appendChild()`
     - **하나의 Node를** 특정 부모 Node의 자식 NodeList중 마지막 자식으로 삽입(**Node만 가능**)
     - 한번에 오직 하나의 Node만 추가 가능
     - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동
     - 추가된 Node 객체를 반환
   - `Node.innerText`
     - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)을 표현
     - 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
   - Element.innerHTML
     - element 내에 포함된 HTML 마크업을 반환
     - XSS(Cross-site Scripting) 공격에 취약
       - 공격자가 입력요소(`<input>`)를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법
       - 피해자의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함
   - `ChildNode.remove()`
     - Node가 속한 트리에서 해당 Node를 제거
   - `ParentNode.removeChile(ChildNode)`
     - DOM에서 자식 Node를 제거하고 제거된 Node를 반환
     - Node는 인자로 들어가는 자식 Node의 부모 Node
   - `Element.setAttribute(name, value)`
     - 지정된 요소의 값을 설정
     - 속성이 이미 존재하면 값을 갱신하고 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
   - `Element.getAttribute(attributeName)`
     - 해당 요소의 지정된 값을 반환
     - 인자는 값을 얻고자 하는 속성의 이름





## 2. JavaScript의 역사

### 핵심 인물

- 팀 버너스리
  - www, URL, HTTP, HTML 최초 설계자
- 브랜던 아이크
  - JavaScript 최초 설계자
  - 모질라 재단 공종 설립자
  - 코드네임 피닉스 프로젝트 진행
    - 파이어폭스의 전신



### 역사

- 1차 브라우저 전쟁
  - 넷스케이프 vs MS
  - IE를 발표해 MS 승리
  - 이후 넷스케이프 후계자들은 모질라 재단 기반으로 파이어폭스 개발
- 파편화
  - 브라우저 마다 자체 JavaScript 언어를 사용
  - 크로스 브라우징 이슈 발생
    - 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들되 어느 한 쪽에 치우치지 않도록 웹 페이지를 제작하는 방법론(동일성이 아닌 동등성)
    - 브라우저마다 렌더링에 사용하는 엔진이 다르기 때문
- 2차 브라우저 전쟁
  - MS vs 구글
  - 구글이 크롬을 발표해 압도적인 속도와 강력한 개발자 도구, 웹 표준 등의 요인으로 승리
- 표준화
  - ECMA에 표준 제정 요청
  - ES6가 탄생해 고질적인 문제들 해결
- Vanilla JavaScript
  - 크로스 브라우징, 간편한 활용 등을 위해 `jQuery`와 같은 라이브러리를 순수 JavaScript보다 많이 썼으나 ES6 이후 다시 순수 JavaScript 활용 증대



## 3. 기본 문법

### 변수와 식별자

#### 식별자의 정의와 특징

- 식별자는 변수를 구분할 수 있는 변수명
- 반드시 문자, `$`, `_`로 시작
- 대소문자를 구분하며 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능
- 작성 스타일
  - 카멜 케이스(camelCase, lower-camel-case): 변수, 객체, 함수에 사용
  - 파스칼 케이스(PascalCase, upper-camel-case): 클래스, 생성자에 사용
  - 대문자 스테이크 케이스(SNAKE_CASE): 상수(변경될 가능성이 없는 값)에 사용



#### 변수 선언 키워드

|        | `let`       | `const`     | `var`       |
| ------ | ----------- | ----------- | ----------- |
| 재할당 | 가능        | 불가능      | 가능        |
| 재선언 | 불가능      | 불가능      | 가능        |
| 범위   | 블록 스코프 | 블록 스코프 | 함수 스코프 |

- 호이스팅: 변수 선언 이전에 참조할 수 있는 현상
  - 변수 선언 이전의 위치에서 접근 시 `undefined`를 반환
  - `var` 키워드는 호이스팅 문제로 ES6 이후부터는 사용하지 않고 대신 `let`과 `const`를 사용하는 것을 권장
- 스코프
  - 블록 스코프: `if`, `for`, 함수 등의 중괄호 내부
    - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
  - 함수 스코프: 함수의 중괄호 내부
    - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능



### 데이터 타입

#### 데이터 타입 종류

- 원시 타입(Primitive Type): 객체(Object)가 아닌 기본 타입으로 변수에 실제 값이 담기고 실제 값이 복사됨

  - `Number`: 정수 실수 구분 없는 하나의 숫자 타입
    - 부동소수점 형식
    - 계산 불가능한 경우에 반환되는 값인 NaN(Not A Number)도 숫자 타입
  - `String`: 텍스트 데이터를 나타내는 타입
    - 16비트 유니코드 문자의 집합
    - 작은 따옴표 또는 큰 따옴표 모두 가능
    - 템플릿 리터럴 사용 가능
      - ES6부터 지원
      - backtick으로 표현하며 `${ expression }` 형태
  - `Boolean`: 논리적 참 거짓을 나타내며 `true` 또는 `false`로 표현

  | 데이터 타입 | 거짓         | 참               |
  | ----------- | ------------ | ---------------- |
  | `undefined` | 항상 거짓    | X                |
  | `Null`      | 항상 거짓    | X                |
  | `Number`    | 0, -0, `NaN` | 나머지 모든 경우 |
  | `String`    | 빈 문자열    | 나머지 모든 경우 |
  | `Object`    | X            | 항상 참          |

  

  - `undefined`: 값이 없음을 나타내는 데이터 타입
    - 변수 선언 이후 값을 할당하지 않으면 **자동으로** `undefined`가 할당
    - `typeof` 연산자의 결과는 `undefined`
  - `null`: 값이 없음을 **의도적으로** 표현할 때 사용하는 데이터 타입
    - 원시 타입의 정의에 따라 원시 타입에 속하지만 `typeof`연산자의 결과는 object로 표현됨
  - `Symbol`

- 참조 타입(Reference Type): 

  - `Object`
    - `Array`, `Function` 등



### 연산자

#### 할당 연산자

- `=`, `+=`, `-=`, `*=`, `/=` : 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당
- `++`, `--` : 피연산자의 값을 1 증가시키거나 감소시키는 연산자
  - Airbnb Style Guide에서는 `+=` 또는 `-=`과 같이 더 분명한 표현으로 적을 것을 권장



#### 비교 연산자

- 피연산자들을 비교하고 결과값을 `boolean`으로 반환
- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
  - 알파벳끼리 비교하면 순서상 후순위가 더 큼
  - 소문자가 대문자보다 더 큼
- 동등/일치 비교 연산자: 두 피연산자가 같은 값으로 평가되는지 비교 후 `boolean` 값을 반환
  - 두 피연산자가 모두 객체일 경우 메모리의 같은 값을 바라보는지 판별
  - 차이점

|           | 동등 비교 연산자                                             | 일치 비교 연산자                                          |
| --------- | ------------------------------------------------------------ | --------------------------------------------------------- |
| 비교 방식 | 암묵적 타입 변환을 통해 타입을 일치시킨 후 비교              | 두 비교 대상의 타입과 값 모두 같은지 비교하는 엄격한 비교 |
| 비고      | 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음 | 일반적으로 사용                                           |



#### 삼항 연산자

- 형태: `<조건식> ? <참인 경우 반환 값> : <거짓인 경우 반환 값>`
- 결과 값을 변수에 할당 가능
- 한줄로 표기하는 것을 권장
- 삼항 연산자의 반환 값으로 삼항 연산자를 넣을 수 있음



### 조건문

#### if 문

- 조건 표현식의 결과값을 `Boolean` 타입으로 변환 후 참 거짓을 판단
- 조건은 소괄호 안에 작성하고 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

```javascript
if (condition) {
    // 실행 코드
} else if (condition) {
    // 실행 코드
} else {
    // 실행 코드
}
```



#### switch 문

- 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별
- 주로 특정 변수의 값에 따라 조건을 분기할 때 사용
- 조건이 많아질 경우 if문보다 가독성이 나을 수 있음
- `break` 문과 `default`문은 선택적으로 사용 가능
- `break`문이 없는 경우 `break`문을 만나거나 `default`문을 실행할 때 까지 계속해서 조건문 실행
- 블록 스코프 생성

```javascript
switch(expression) {
    case 'first value': {
        // 표현식의 결과가 'first value'와 일치하면 실행
        break
    }
    case 'second value': {
        // 표현식의 결과가 'second value'와 일치하면 실행
        break
    }
    default: {
        // 표현식의 결과와 일치하는 값이 없으면 실행 
    }
}

const nation = 'Korea'

switch(nation) {
    case 'Korea': {
        console.log('안녕하세요')	// 표현식의 결과와 값이 일치하기 때문에 실행
    }
    case 'France': {
        console.log('Bonjour')		// Fall-through: break문이 없으면 아래의 코드는 모두 실행
    }
    default: {
        console.log('Hello')		// default문을 만났기 때문에 여기까지 실행
    }
}
```



### 반복문

- `while (condition) { 실행 코드 }`
- `for (initialization; condition; expression) { 실행 코드 }`
- `for (variable in obejct) { 실행 코드 }`
  - 객체(`object`)의 **속성(key)**들을 순회할 때 사용
  - 배열을 순회하려고 하면 속성에 해당하는 인덱스 값을 순회하게 됨
  - 블록 스코프 생성
- `for (variable of iterables) { 실행 코드 }`
  - 반복 가능한(iterable) 객체(주로 배열)를 순환하며 **값**을 꺼낼 때 사용
  - 블록 스코프 생성



### 함수

- 참조 타입중 하나로 `function`타입으로 분류
- 함수를 정의하는 방법
  - 함수 선언식
  - 함수 표현식
  - 추가로 Arrow Function
    - 함수를 비교적 간결하게 정의
    - `function`키워드 생락 가능
    - 매개변수가 단 하나 뿐이라면 `()`도 생략 가능
    - 함수의 몸통이 표현식 하나라면 `{}`과 `return` 도 생략 가능
    - `this`를 사용할 경우 상위 메서드를 인식
- JavaScript의 함수는 **일급 객체**에 해당
  - 일급 객체의 조건
    - 변수에 할당 가능
    - 함수의 매개변수로 전달 가능
    - 함수의 반환 값으로 사용 가능
- 기본 인자 선언 가능
  - `const myFunc = function (name = 'Anonymous') { return }`
- 매개 변수와 인자의 개수 불일치 허용
  - 매개 변수보다 더 많은 인자가 들어오면 알아서 무시
  - 매개 변수보다 더 적은 인자가 들어오면 인자를 받지 못한 매개 변수는 `undefined` 할당
- rest parameter(`...`)을 사용해 정해지지 않은 수의 매개변수를 배열로 받을 수 있음
  - python의 `*args`와 유사
  - 만약 rest parameter로 처리한 매개변수에 인자가 넘어오지 않을 경우 빈 배열로 처리
- spread operator(`...`)를 사용해 배열 인자를 전개하여 전달 가능

```javascript
// 함수 선언식
// - 호이스팅이 발생해 호출 이후에 선언해도 동작
function name(args) {
    // 실행 코드
}

// 함수 표현식
// - 이름을 생략하고 익명 함수로 정의 가능
// - var 키워드로 선언하면 선언 전에 undefined로 초기화 되어 다른 에러 발생
const name = function (args) {
    // 실행 코드
}

// Arrow Function

// 1. function 키워드 삭제
const arrow1 = (name) => { return `hello, ${name}` }
// 2. 매개변수가 1개이므로 ()도 생략
const arrow2 = name => { return `hello, ${name}` }
// 3. 함수 바디가 return을 포함한 표현식 1개이므로 {}과 return 삭제
const arrow1 = name => `hello, ${name}`
```





### 문자열

#### 문자열 메서드

| 메서드                  | 설명                                                        | 비고                                          |
| ----------------------- | ----------------------------------------------------------- | --------------------------------------------- |
| `includes('value')`     | 특정 문자열(`'value'`)의 존재여부를 참/거짓으로 반환        |                                               |
| `split('value')`        | 문자열을 토큰(`'value'`) 기준으로 나눈 배열 반환            | 인자가 없으면 기존 문자열을 배열에 담아 반환  |
| `replace('from', 'to')` | 해당 문자열(`'from'`)을 대상 문자열(`'to'`)로 교체하여 반환 | 하나만 교체, 모두 교체하려면 `replaceAll`사용 |
| `trim`                  | 문자열의 좌우 공백(스페이스, 탭, 엔터 등) 제거하여 반환     | `trimstart`, `trimend`                        |



### 배열

#### 정의와 특징

- 키와 속성들을 답고 있는 참조 타입의 객체(object)
- 순서를 보장
- 주로 대괄호를 이용하여 생성
- 인덱스로 접근 가능
- 배열의 길이는 `array.length`로 접근
  - 배열의 마지막 원소는 `array[array.length - 1]`
- spread operator(`...`)를 사용해 얕은 복사 가능
  - 깊은 복사는 `lodash`라이브러리의 `_.cloneDeep` 사용



#### 배열 메서드

| 메서드             | 설명                                                         | 비고                              |
| ------------------ | ------------------------------------------------------------ | --------------------------------- |
| `reverse`          | 원본 배열의 요소들의 순서를 반대로 정렬                      |                                   |
| `push`, `pop`      | 배열의 맨 뒤에 요소를 추가 또는 제거                         |                                   |
| `unshift`, `shift` | 배열의 맨 앞에 요소를 추가 또는 제거                         |                                   |
| `includes`         | 배열에 특정 값이 있는지 판별 후 참/거짓 반환                 |                                   |
| `indexOf`          | 배열에 특정 값이 있는지 판별 후 인덱스 반환                  | 요소가 없으면 -1 반환             |
| `join`             | 배열의 모든 요소를 구분자를 기준으로 연결                    | 구분자 생략 시 쉼표 기준          |
| `forEach`          | 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행<br />콜백 함수는 3개의 매개변수(`element`, `index`, `array`)로 구성 | 반환 값 없음                      |
| `map`              | 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환           |                                   |
| `filter`           | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 |                                   |
| `reduce`           | 콜백 함수의 반환 값들을 하나의 값(`acc`)에 누적 후 반환<br />콜백 함수는 4개의 매개변수(`acc`, `element`, `index`, `array`)로 구성<br />- `acc`: 이전 콜백 함수의 반환 값이 누적되는 변수<br />- `initialValue`: 최초 콜백 함수 호출 시 `acc`에 할당되는 값<br />    -기본값은 배열의 첫 번째 값<br />    -빈 배열의 경우 `initialValue`를 지정하지 않으면 오류 발생 |                                   |
| `find`             | 콜백 함수의 반환 값이 참이면 해당 요소를 반환                | 찾는 값이 없으면 `undefined` 반환 |
| `some`             | 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환       | 빈 배열은 항상 거짓 반환          |
| `every`            | 배열의 모든 요소가 판별 함수를 통과하면 참을 반환            | 빈 배열은 항상 참 반환            |



### 객체

#### 정의와 특징

- 객체는 속성(property)의 집합이며 중괄호 내부에 `key`와 `value`의 쌍으로 표현
- `key`는 문자열 타입만 가능
  - `key` 이름에 띄어쓰기 등 구분자가 있으면 따옴표로 묶어서 표현
- `value`는 모든 타입 가능
- 객체 요소 접근은 점 또는 대괄호로 가능
  - `key`이름에 띄어쓰기 등 구분자가 있으면 대괄호 접근만 가능



#### 객체 관련 ES6 문법

```javascript
// 1. key와 할당하는 변수의 이름이 같은 경우
const books = ['book1', 'book2', 'book3']
const magazines = ['magazine1', 'magazine2']

const bookshop = {
    books: books,
    magazines: magazins,
}
// 다음과 같이 축약 가능
const bookshop2 = {
    books,
    magazines,
}


// 2. 메서드 선언시
const obj = {
    greeting: function() {
        // 실행 코드
    }
}
// function 키워드 생략 가능
const obj2 = {
    greeting() {
        // 실행 코드
    }
}


// 3. 계산된 속성
const key = 'regions'
const value = ['서울', '광주', '대전', '구미', '부울경']

// key의 이름을 표현식을 이용하여 동적으로 생성 가능
const ssafy = {
    [key]: value,
}
// { regions: ['서울', '광주', '대전', '구미', '부울경'] } 와 동일


// 4. 구조 분해 할당
const userInformation = {
    name: 'kim',
    userId: 'ssafyStudent1234',
    phoneNumber: '010-1234-5678',
}

const name = userInformation.name
const userId = userInformation.userId
const phoneNumber = userInformation.phoneNumber

// 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당 가능(변수명이 속성명과 동일해야 가능)
const { name } = userInformation
const { userId } = userInformation
const { phoneNumber } = userInformation
// 복수개도 가능
const { name, userId } = userInformation


// 5. spread operator
const obj = {b: 2, c: 3, d: 4}
const newObj = {a: 1, ...obj, e: 5}
// const newObj = {a:1, b:2, c:3, d:4, e: 5} 와 동일
// 얕은 복사에 활용 가능
```



### JSON(JavaScript Object Notation)

- `key`-`value` 쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
- 자바 스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입
  - 따라서 JS의 객체로 조작하기 위해서는 구문 분석(parsing) 필요
- JSON을 조작하기 위해서 두 가지 내장 메서드 제공
  - `JSON.parse()`: JSON(문자열) -> 자바스크립트 객체
  - `JSON.stringify()`: 자바스크립트 객체 -> JSON(문자열)



### this

- `this` 는 실행 문맥에 따라 다른 대상을 가리킴
- class 내부의 생성자 함수에서는 생성되는 객체(python의 `self`)
- 메서드 내부에서는 해당 메서드가 소속된 객체를 가리킴
- 그 외의 모든 경우에서 최상위 객체인 window를 가리킴
  - 따라서 메서드 내부의 콜백함수에서 사용 될 경우 메서드에서 사용되는 것이 아니기 때문에 window를 가리킴
    - 이를 방지하기 위해서 `.bind(this)`메서드를 사용하거나 Arrow Function을 사용



### lodash

- 모듈성, 성능 및 추가 기능을 제공하는 JavaScript의 유틸리티 라이브러리
- 자료구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수들 제공
- `_.reverse`, `_.sortBy`, `_.range`, `_.random`, `_.cloneDeep` 등



## 4. Event

### Event의 개념

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- 이벤트 발생
  - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음
  - 특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있음
- 이벤트 기반 인터페이스
  - AnimationEvent, ClipboardEvent, DragEvent 등
  - UIEvent
    - 간단한 사용자 인터페이스 이벤트
    - Event의 상속을 받음
    - MouseEvent, KeyboardEvent, InputEvent, FocusEvent 등의 부모 객체 역할을 함



### 함수

- `EventTarget.addEventListner(type, listener)`
  - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
  - 이벤트를 지원하는 모든 객체를 대상으로 지정 가능
  - type: 반응 할 이벤트 유형(대소문자를 구분하는 문자열)
  - listener: 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
    - EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함
- `event.preventDefault()`
  - 현재 이벤트의 기본 동작을 중단
  - HTML요소의 기본 동작을 작동하지 않게 막음
  - 이벤트를 취소할 수 있는 경우 이벤트의 전파를 막지 않고 그 이벤트를 취소
  - 취소 할 수 없는 이벤트도 존재하며 `event.cancelable`을 통해 확인 가능
