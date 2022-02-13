# HTML(Hyper Text Markup Language)

[toc]

## 1. 기본 개념

### - 정의

- 웹 페이지를 작성하기 위한 언어

- 웹을 이루는 가장 기초적인 구성 요소 중 하나
  - HTML: 웹 콘텐츠의 의미와 구조를 정의할 때 사용

  - [CSS](./css.md): HTML이나 XML로 작성된 문서의 표시 방법을 기술하기 위한 스타일 시트 언어

  - [JavaScript](./js.md): 클라이언트 측 웹(브라우저)에서 실행 되고, 웹 페이지가 이벤트 발생 시 어떻게 작동하는 지 디자인 / 프로그래밍하는 가벼운 객체 지향 인터프리터 언어
- Hyper Text: 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- Markup Language: 문서나 데이터의 를 구조화 하는 언어
  - 연산 능력을 가진 프로그래밍 언어와는 전혀 다른 종류
  - 태그를 사용해 문서나 데이터의 구조를 명시



### - 관계

- WHATWG(Web Hypertext Application Technology Working Group)에서 표준 제정
- Mozilla: MDN Web Docs 제공



## 2. 기본 구조

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

- ! + `tab`으로 자동완성 가능

### - html

- 문서의 최상위 요소

### - head

- 문서의 메타데이터 요소

- `<title>`: 브라우저 상단 타이틀
- `<meta>`: 문서 레벨 메타데이터 요소
  - `charset="UTF-8"`:  문서 인코딩에 사용한 문자 인코딩을 나타내는 문자 집합 선언
  - `http-equiv="X-UA-Compatible"`: 특정 http헤더를 지정해 프레그마 지시문을 정의
  - `x-ua-compatible`로 지정할 경우 `content="IE=edge"`여야함
  - `content="IE=edge"`: 가장 최신 표준 모드를 선택하는 문서 모드
  - `name="viewport"`: 전체 페이지에 적용되는 문서 레벨 메타데이터 제공
- `<link>`: 외부 리소스 연결 요소(CSS파일 등)
  - `href="file_name.css"`: 외부 리소스 연결을 위한 경로/파일명 지정
  - `rel="stylesheet"`: 현재 문서와 연결된 리소스간의 관계를 정의
- `<script>`: 스크립트 요소(JavaScript 파일/코드)
- `<style>`: CSS 내부 참조 방식으로 작성



### - DOM(The Document Object Model) Tree

- DOM
  - HTML, XML 문서의 프로그래밍 인터페이스
  - 문서의 구조화된 표현을 제공해 문서에 대한 모델을 구성
  - 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - 문서 구조, 스타일, 내용 등을 변경 변경할 수 있게 돕는 역할
  - 구조화된 nodes와 각 요소에 접근 및 수정을 위한 property, method를 갖고 있는 object로 문서를 표현

- Tree

  document

  └ html

  ​	├ head

  ​	│	└ title 

  ​	│			└ "Title"

  ​	└ body

  ​			├ h1

  ​			│	└ "A heading"

  ​			└ a ─ href

  ​				└ "Link text"

  - 이런 트리 모양의 구조로 구성
  - Indentation: 2 space



### - Element

- 태그와 내용(Contents)으로 구성
  - `<tag attribute="value"> contents </tag>` 형태
  - 시작 태그 안에 속성 이름과 값 작성
  - 태그로 컨텐츠를 감싸 그 정보의 성격과 의미를 정의
- 태그
  - 컨텐츠를 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 태그별로 사용할 수 있는 속성이 다름
  - 컨텐츠가 없는 태그 존재
    - `<br>, <hr>, <img>, <input>, <link>, <meta>` 등
- 중첩이 가능해 이를 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍 중요
    - 잘못되어도 오류를 반환하는 것이 아니라 레이아웃이 깨져서 출력되기 때문에 디버깅 어려움



### - 속성

- 경로나 크기와 같은 태그의 부가적인 정보 설정
- 시작 태그 안에 이름과 값을 하나의 쌍으로 작성
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute) 존재

- HTML Global Attribute
  - id: 문서 전체에서 유일한 고유 식별자 지정
    - 주로 JS에서 요소에 접근할 때 사용
  - class: 공백으로 구분된 해당 요소의 클래스의 목록
    - CSS, JS에서 요소를 선택하거나 접근할 때 사용
  - data-*: 페이지에 개인 사용자 정의 데이터를 저장
  - style: inline 스타일 지정
  - title: 요소에 대한 추가 정보 지정
  - tabindex: 요소의 탭 순서



### - 시맨틱 태그

- Sementic: 의미론적인
- 시맨틱 태그란 기존의 단순히 영역만 의미하는 div 태그를 대체하여 사용하는 의미론적 요소를 담은 태그
- 대표적인 태그
  - header: 문서 전체나 섹션의 머리말 부분
  - nav: 내비게이션
  - aside: 사이드에 위치한 공간으로 메인 콘텐츠와 관련성이 적은 콘텐츠
  - section: 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - article: 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - footer: 문서 전체나 섹션의 마지막 부분
  - 그 외 h1, table 태그들도 포함
- Non semantic 요소
  - div: 블록 요소
  - span: 인라인 요소
- 단순히 구역을 나누는 것 뿐만 아니라 의미있는 정보의 그룹을 태그로 표현하는 것
- 가독성을 높이고 유지보수를 용이하게 하며 SEO를 위해 중요

## 3. 문서 구조화

### - 텍스트 요소

- `<a> </a>`: href 속성을 활용해 다른 URL로 연결하는 하이퍼링크 생성
- `<b> </b>`: 굵은 글씨
- `<strong> </strong>`: 보통 굵은 글씨로 표현되는중요한 강조하고자 하는 요소
- `<i> </i>`: 기울임 글씨
- `<em> </em>`: 보통 기울임 글씨로 표현되는 중요한 강조하고자 하는 요소
- `<br>`: 텍스트 내에 줄 바꿈 생성
- `<img>`: src속성을 활용하여 이미지 표현
- `<span> </span>`: 의미 없는 인라인 컨테이너



### - 그룹 컨텐츠

- `<p> </p>`: 하나의 문단(Paragraph)
- `<hr>`: 문단 레벨 요소에서의 주제의 분리를 의미하는 수평선(A Horizontal Rule)
- `<ol> </ol>`: 순서가 있는 리스트(Ordered List)
- `<ul> </ul>`: 순서가 없는 리스트(Unordered List)
- `<pre> </pre>`: HTML에 작성한 내용을 그대로 표현하며 보통 고정폭 글꼴이 사용되고 공백 문자를 유지
- `<blockquote> </blockquote>`: 텍스트가 긴 인용문을 주로 들여쓰기를 한 것으로 표현
- `<div> </div>`: 의미없는 블록 레벨 컨테이너



### - 표(table)

- `<table> </table>`
  - thead(header) : 영역 구분
    - tr > th
    - `<tr>`로 가로 줄 구성
    - `<th>`로 제목 셀 구성
  - tbody(body)
    - tr > td 
    - `<td>`로 셀 구성
  - tfoot(footer)
    - tr > td 
    - `<td colspan="n">`으로 셀 가로 병합
    - `<td rowspan="n">`으로 셀 세로 병합
  - caption: 표 설명 또는 제목



### - form

- `<form> </form>`
- 정보를 서버에 제출하기 위한 영역
- 기본 속성
  - action: form을 처리할 서버의 URL
  - method: form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
  - enctype: method가 post인 경우 데이터의 유형
    - application/x-www-form-urlencoded: 기본값
    - multipart/form-data: 파일 전송시(input type이 file인 경우)



### - input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯 존재
- `<input>`
- 기본 속성
  - id: `<label>`의 for 속성과 함께 활용해 상호 연관 가능
  - name / value: form control에 적용되어 이름과 값이 페어로 전송
  - autocomplete: 양식 자동생성 기능 암시
  - autofocus: 페이지가 로딩될 때 해당 양식에 자동으로 커서 위치
  - disabled: 양식 컨트롤이 비활성화 되었는지의 여부
  - readonly: 불리언값으로 이 값은 수정이 불가능함
  - required: 불리언값으로 양식이 전송되기 위해서 반드시 입력하거나 확인이 필요한 값
- `type="유형"` 형태로 유형을 지정하면 유형에 따라 동작이 달라짐
- 일반 유형
  - text: 일반 텍스트
  - password: 입력 시 값이 보이지 않고 문자를 특수기호(`*`)로 표현
  - email: 이메일 형식이 아닌 경우 제출 불가
    - 동적 키보드 지원 시 적합한 키보드 표시
  - number: 숫자만 입력 가능
    - min, max, step 속성을 활용해 범위 설정 가능
    - 스피너를 표시
    - 동적 키보드 지원 시 숫자 키패드 표시
  - file: 파일 지정
    - accept 속성을 활용하여 허용하는 파일 유형 지정 가능
- 선택 유형
  - checkbox: 각각의 항목을 선택하거나 해제
  - radio: 여러개의 항목 중 하나만 선택
- 기타 유형
  - color: 색 지정
  - date: 날짜를 지정
  - datetime-local: 날짜와 시간 지정
    - 브라우저가 지원하는 경우 달력과 시계 등 표시 가능
  - hidden: 사용자에게 보이지 않는 입력
    - 미리 만들어 둔 값을 자동으로 넘어가게 할 때 사용
