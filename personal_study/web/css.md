# CSS(Cascading Style Sheets)

[toc]

## 1. 기본 개념

### - 정의

- 웹 페이지의 스타일을 지정하기 위한 언어
- 웹을 이루는 가장 기초적인 구성 요소 중 하나
  - [HTML](./html.md): 웹 콘텐츠의 의미와 구조를 정의할 때 사용
  - CSS: HTML이나 XML로 작성된 문서의 표시 방법을 기술하기 위한 스타일 시트 언어
  - [JavaScript](./js.md): 클라이언트 측 웹(브라우저)에서 실행 되고, 웹 페이지가 이벤트 발생 시 어떻게 작동하는 지 디자인 / 프로그래밍하는 가벼운 객체 지향 인터프리터 언어
- Cascading: 위에서 아래로 흐르는, 상속 또는 종속하는
- Style Sheet: 문서에 있는 요소들에 선택적으로 스타일을 적용할 수 있는 언어



### - 구문

```css
Selector {
    Property: Value;
} /* └ declaration ┘ */
```

- 선택자를 통해 스타일을 지정할 요소를 선택
- 중괄호 안에서 요소에 부여할 속성(어떤 기능을)과 값(어떻게 변경할지)을 하나의 쌍으로 선언



### - 정의 방법

- 인라인

  - `<tag style="property1: value1; property2: value2;"`
  - 해당 태그 안에서 직접 style 속성 활용

- 내부 참조

  ```html
  <head>
    <style>
      selector {
          property: value;
      }
    </style>
  </head>
  ```

  - `<head>` 태그 내에 `<style>` 태그에 지정

- 외부 참조

  - `<link rel="stylesheet" href="file_name.css">`
  - 외부 css 파일을 `<head>` 태그 내의 `<link>` 태그를 통해 불러옴



## 2. CSS Selector

### - 선택자 유형

- 기본 선택자
  - 전체 선택자
  - 요소 선택자
    - HTML 태그를 직접 선택

  - 클래스 선택자
    - 마침표로 시작하며, 해당 클래스가 적용된 항목을 선택

  - 아이디 선택자
    - `#` 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
    - 일반적으로 하나의 문서에 1번만 사용, 여러번 사용도 가능은 하지만 하면 안됨

  - 속성 선택자

- 결합자
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자

- 의사 클래스/요소
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 속성 선택자




### - 적용 우선순위

- !important: 최우선, 사용시 주의
- 인라인 > id > class, 속성 > 요소
- 우선순위 동일하면 나중에 적용된 스타일이 우선



### - 상속

- 부모 요소의 속성이 자식에게 상속되는 경우 존재
  - 상속 되는 경우
    - text 관련 요소(font, color, text-align)
    - opacity
    - visibility
  - 상속 되지 않는 경우
    - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
    - position 관련 요소(position, top/right/bottom/left, z-index)

## 3. CSS 기본 스타일

### - 크기 단위

- px (픽셀)
  - 고정적인 단위
- %
  - 가변적인 레이아웃에서 자주 사용
- em
  - 부모 요소에 지정된 사이즈에 상대적인 사이즈를 가지는 배수 단위
- rem
  - 최상위 요소의 사이즈(16px)를 기준으로 사이즈를 가지는 배수 단위
- viewport
  - 디바이스 화면을 기준으로 상대적인 사이즈 결정
  - vw, vh, vmin, vmax



### - 색상 단위

- 색상 키워드

  - 대소문자를 구분하지 않고 특정 색을 직접 글자로 나타냄
  - red, blue, black 등

- RGB 색상

  - 16진수 표기법 혹은 함수형 표기법을 사용해 특정 색을 표현

  ```css
  selector {
    color: #000000;				/* 16진수 표기법 */
    color: rgb(0, 0, 0);			/* 함수형 표기법 */
    color: rgba(0, 0, 0, 0.5);	/* a는 alpha(투명도) */
  }
  ```

  

- HSL 색상

  - 색상, 채도, 명도를 통해 특정 색을 표현

  ```css
  selector {
    hsl(120, 100%, 0);
    hsla(120, 100%, 0, 0.5)
  }
  ```

  

## 4. Selector 심화

### - 결합자

- 자손 결합자 `selectorA selectorB {}`
  - selectorA 하위의 모든 selectorB 요소
- 자식 결합자 `selectorA > selectorB {}`
  - selectorA 바로 아래의 selectorB 요소
- 일반 형제 결합자 `selectorA ~ selectorB {}`
  - selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택
- 인접 형제 결합자 `selectorA + selectorB {}`
  - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택

## 5. Box model

### - 박스 모델

- 모든 요소는 박스모델
- 좌측 상단부터 Normal Flow에 따라 쌓임
  - Inline Direction →
  - Block Direction ↓

- 하나의 박스는 네 영역

  - margin: 테두리 바깥의 외부 여백, 배경색 지정 불가

  - boder: 테두리 영역

  - padding: 테두리 안쪽의 내부 여백, 배경색과 이미지는 padding까지 적용

  - content: 글이나 이미지 등 요소의 실제 내용

- margin, padding

  ```css
  .margin-padding {
    margin-top: 10px;		/* 상 */
    margin-right: 20px;	/* 우 */
    margin-botom: 30px;	/* 하 */
    margin-left: 40px;	/* 좌 */
      /* shorthand */
    padding: 30px;				/* 상하좌우 */
    padding: 10px 20px;			/* 상하 좌우 */
    padding: 10px 20px 30px;		/* 상 좌우 하 */
    padding: 10px 20px 30px 40px;	/* 상 우 하 좌 */
  }
  ```

- border

  ```css
  .border {
    border-width: 2px;
    border-style: dashed;
    border-color: black;
      /* shorthand */
    border: 2px dashed black;
  }
  ```



### - box sizing

- 기본적으로 모든 요소의 box sizing은 padding을 제외한 content-box 영역만을 지정

- 일반적으로 영역을 볼 때 border까지를 생각하기 때문에 border-box 설정

  ```css
  .box-sizing {
    box-sizing: content-box;
    box-sizing: border-box;
  }
  ```



## 6. Display

### - 대표적인 Display

- `display: block;`

  - 줄 바꿈이 일어나는 요소
  - 화면 가로폭 전체를 차지
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
  - div, ul, ol, li, p, hr, form 등

- `display: inline;`

  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비 만큼 가로 폭을 차지
  - width, ehight, margin-top, margin-bottom 지정 불가
  - 상하 여백은 line-height로 지정
  - span, a, img, input, label, b, em, i, strong 등

- `display: inline-block;`

  - block처럼 width, height, margin 속성을 모두 지정 가능
  - inline 처럼 한 줄에 표시 가능

- `display: none;`

  - 해당 요소를 화면에 표시하지 않고, 공간도 부여되지 않음
  - `visibility: hidden;` 의 경우 공간은 차지하나 화면에 표시하지 않음

- 수평 정렬

  |             |                                               |                       |
  | ----------- | --------------------------------------------- | --------------------- |
  | 왼쪽 정렬   | `margin-right: auto;`                         | `text-align: left;`   |
  | 오른쪽 정렬 | `margin-left: auto;`                          | `text-align: right;`  |
  | 중앙 정렬   | `margin-right: auto;`<br>`margin-left: auto;` | `text-align: center;` |

  

## 7. Position

### - CSS Position

- 문서 상에서 요소의 위치를 지정
- static: 기본 값
  - Normal Flow를 따름
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치
- relative: 상대 위치
  - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
  - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음(normal position 대비 offset)
- absolute: 절대 위치
  - 요소를 일반적인 문서 흐름에서 제거해 레이아웃에 공간을 차지하지 않음(normal flow를 벗어남)
  - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body)
- fixed: 고정 위치
  - 요소를 일반적인 문서 흐름에서 제거해 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
  - 부모 요소와 관곙벗이 viewport를 기준으로 이동
    - 스크롤 시에도 항상 같은 곳에 위치
- 좌표 프로퍼티
  - top, bottom, left, right 등
  - relative, absolute, fixed 의 경우에 사용 가능



## 8. Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함한 인라인 요소들이 주변을 둘러싸도록 함

- 요소가 Normal Flow를 벗어나도록 함

- 속성값

  - none: 기본값
  - left: 요소를 왼쪽으로 띄움
  - right: 요소를 오른쪽으로 띄움

- clearing

  - Normal Flow에서 벗어난 상태이기 때문에 이후 요소에 대해 속성이 적용되지 않도록 clearing 필요

  - `::after` : 선택한 요소의 맨 마지막 자식으로 가상 요소를 생성

    - 보통 content 속성과 함께 짝지어 요소에 장식용 콘텐츠를 추가할 때 사용

    ```css
    .clearfix::after {
      content: "";
      display: block;
      clear: both;
    }
    ```

    

## 9. Flex Box

### - Flexible Box Layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
  - main axis(메인 축)
  - cross acis(교차 축)
- 부모 요소인 Flex Container 안에 자식 요소인 Flex Item 위치



### - [Flex 속성](./source/flex.html)

- 배치
  - flex-direction: main axis 기준 방향 설정
  - flex-wrap: 요소들을 강제로 한 줄에 배치 되게 할 것인지 여부
  - flex-flow: flex-direction과 flex-wrap의 short hand
- 공간 나누기
  - justify-content(main axis)
  - align-content(cross axis)
- 정렬
  - align-items: 모든 아이템을 cross axis 기준으로 정렬
  - align-self: 개별 아이템을 정렬