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

- 

## 3. CSS 기본 스타일

## 4. Selector 심화

## 5. Box model

## 6. Display

## 7. Position