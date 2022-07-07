# Vue.js

[toc]

## 프론트 엔드

### 프론트 엔드 개발

- HTML, CSS 그리고 JavaScript를 활용해서 데이터를 볼 수 있게 만들어 주는 것
  - 이 작업을 통해 사용자는 데이터와 상호작용 할 수 있음
  - Django(서버)에서 JSON 데이터를 보내주면 이를 사용자가 보고 상호작용 할 수 있도록 만들어 주는 것
- 대표적인 프론트엔드 프레임 워크
  - Vue.js, React, Angulr



### SPA

- Single Page Appication
- 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 웹 애플리케이션
- 단일 페이지로 구성되며 서버로부터 최초에만 페이지를 다운로드하고 이후에는 DOM을 동적으로 구성해 매번 새로운 전체 페이지를 불러오는 것이 아닌 현재 페이지에서 필요한 부분만 다시 작성하도록 함
- 연속되는 펴이지 간의 사용자 경험(UX)을 향상
  - 모바일 사용량이 증가하고 있어 트래픽 감소와 속도, 사용성, 반응성의 향상이 매우 중요해졌기 때문
- 동작 원리의 일부가 CSR(Client Side Rendering)의 구조를 따름
- 등장 배경
  - 과거 웹 사이트들은 요청에 따라 매번 새로운 페이지를 응답하는 MAP(Multi Page Application) 방식이었으나 스마트폰이 등장하면서 모바일 최적화의 필요성이 대두됨
    - 모바일 네이티브 앱과 같은 형태의 웹 페이지가 필요
  - 이러한 문제를 해결하기 위해 Vue.js와 같은 프론트엔드 프레임워크와 CSR, SPA와 같은 개념이 등장함
  - 1개의 웹 페이지에서 여러 동작이 이루어지며 모바일 앱과 비슷한 형태의 사용자 경험을 제공



### CSR

- Client Side Rendering
- 서버에서 화면을 구성하는 SSR(Server Side Rendering)방식과 달리 클라이언트에서 화면을 구성
- 최초 요청 시 HTML, CSS, JS 등 데이터를 제외한 각종 리소스를 응답받고 이후 클라이언트에서는 필요한 데이터만 요청해 JS로 DOM을 렌더링하는 방식
- 즉 처음에 뼈대를 받고 브라우저에서 동적으로 DOM을 그림
- SPA가 사용하는 렌더링 방식



### SSR

- Server Side Rendering
- 서버에서 클라이언트에게 보여줄 페이지를 모두 구성하여 전달하는 방식
- JS 웹 프레임워크 이전에 사용되던 전통적인 렌더링 방식
- Django에서 DTL로 HTML문서를 만들어 `render()`함수를 통해 반환하던 것이 SSR 방식



#### CSR vs SSR

|      | CSR                                                          | SSR                                                          |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 장점 | 서버와 클라이언트 간 트래픽 감소<br> ● 웹 애플리케이션에 필요한 모든 정적 리소스를 최초에 한 번 다운로드 후<br/>   필요한 데이터만 갱신하기 때문<br>사용자 경험(UX) 향상<br> ● 전체 페이지를 다시 렌더링하지 않고 변경되는 부분만을 갱신하기 때문 | 초기 구동 속도가 빠름<br/> ● 클라이언트가 빠르게 컨텐츠를 볼 수 있음<br/>SEO(검색 엔진 최적화)에 적합<br/> ● DOM에 이미 모든 데이터가 작성되어 있기 때문 |
| 단점 | SSR에 비해 전체 페이지 최종 렌더링 시점이 느림<br/>SEO(검색 엔진 최적화)에 어려움이 있음<br/> ● 최초 문서에 데이터 마크업이 없기 때문 | 모든 요청마다 새로운 페이지를 구성하여 전달<br/> ● 반복되는 전체 새로고침으로 인해 사용자 경험이 떨어짐<br/> ● 상대적으로 트래픽이 많아 서버의 부담이 클 수 있음 |

- 두 방식의 차이는 최종 HTML 생성 주체가 서버가 만드는지 클라이언트가 만드는지에 따라 결정
- 단순히 어떤 것이 더 좋다가 아니라 서비스 또는 프로젝트 구성에 맞는 방법을 적절하게 선택하는 것이 중요
- 예를 들어 Django에서 Axios를 활용한 좋아요/팔로우 로직의 경우 대부분은 Server에서 완성된 HTML을 제공하는 SSR 방식
  - 단 특정 요소(좋아요, 팔로우)만 JS로 AJAX를 활용해 비동기 요청으로 필요한 데이터를 클라이언트에서 서버로 직접 요청을 보내 받아오고 DOM을 조작하는 CSR 방식
- CSR 방식은 SEO에 어려움이 있다는 단점이 있었으나 Vue.js 또는 React 등의 SPA 프레임워크는 SSR을 지원하는 SEO 대응 기술이 이미 존재
  - SEO 대응이 필요한 페이지에 대해서는 선별적으로 SEO 대응 가능
  - 혹은 추가로 별도의 프레임워크를 사용하기도 함
    - Nuxt.js: Vue.js 응용 프로그램을 만들기 위한 프레임워크
    - Next.js: React 응용 프로그램을 만들기 위한 프레임워크



## Vue.Js

### Vue.js란

- 사용자 인터페이스를 만들기 위한 **The Progressive JavaScript Framework**
- 현대적인 툴과 다양한 라이브러리를 통해 SPA(Single Page Application)를 완벽하게 지원



### MVVM Pattern

- 애플리케이션 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴
- **M**odel
  - Vue에서 Model은 key와 value로 이루어진 JavaScript Object
  - Model은 Vue Instance 내부에서 data라는 이름으로 존재
  - data가 변경되면 View(DOM)가 반응
- **V**iew
  - Vue에서 View는 DOM(HTML)
  - data의 변화에 따라서 바뀌는 대상
- **V**iew**M**odel
  - Vue에서 View Model은 모든 Vue Instance
  - View와 Model 사이에서 data와 DOM에 관련된 모든 일을 처리하는 중재자 역할
  - ViewModel을 활용해 data를 얼마나 잘 처리해서 보여줄 것인지 고민하는 것



### 코드 작성 순서

- Django에서는 데이터의 흐름에 따라 코드를 작성
  - url -> views -> tempalte
- Vue.js에서는 Data가 변화하면 DOM이 변화하기 때문에
  1. Data 로직 작성
  2. DOM 작성



## Vue.js 기본 문법

### Vue Instance

- 모든 Vue 앱은 Vue 함수로 새 인스턴스를 만드는 것부터 시작
- Vue 인스턴스를 생성할 때는 Options 객체를 전달해야 함
- 여러 Options들을 사용하여 원하는 동작을 구현



### Options

- `el`
  - Vue 인스턴스에 연결할 기존 DOM 요소가 필요
  - CSS 선택자 문자열 혹은 HTML Element로 작성
  - new를 이용한 인스턴스 생성 때만 사용
- `data`
  - Vue 인스턴스의 데이터 객체로 상태 데이터를 정의하는 곳
  - Vue template에서 인터폴레이션을 통해 접근
  - `v-bind`, `v-on`과 같은 directive에서도 사용 가능
  - Vue 객체 내 다른 함수에서 `this` 키워드를 통해 접근 가능
- `methods`
  - Vue 인스턴스에 추가할 메서드
  - Vue template에서 인터폴레이션을 통해 접근
  - `v-on`과 같은 directive에서도 사용 가능
  - Vue 객체 내 다른 함수에서 `this` 키워드를 통해 접근 가능
  - 화살표 함수를 메서드를 정의하는데 사용하면 부모 컨텍스트를 바인딩 하기 때문에 this는 Vue 인스턴스가 아니게 됨



## Template 문법

### Template 문법

- 렌더링 된 DOM을 기본 Vue 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문을 사용
  1. Interpolation
  2. Directive



### Interpolation

```vue
// Text
<span>메시지: {{ message }}</span>
// Raw HTML
<span v-html="rawHtml"></span>
// Attribute
<div v-bind="dynamicId"></div>
// JS 표현식
{{ number + 1 }}
{{ message.split('').reverse().join('') }}
```



### Directive

- `v-` 접두사가 붙는 특수 속성
- 속성 값은 단일 JS 표현식의 됨(`v-for`는 예외)
- 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 역할을 함
- 전달인자(Arguments)는 `:`을 통해 받을 수 있음
  - `<a v-bind:href="url">url</a>`
- 수식어라고 하는 `.`으로 표시되는 특수 접미사를 통해 directive를 특별한 방법으로 바인딩 해야 함을 내타낼 수 있음
  - `<form v-on:submit.prevent="onSubmit"> </form>`
- `v-text`
  - 엘리먼트의 textContent를 업데이트
  - 내부적으로 Interpolation 문법이 `v-text`로 컴파일됨
- `v-html`
  - 엘리먼트의 innerHTML을 업데이트
  - XSS 공격에 취약할 수 있음
  - 임의로 사용자에게 입력받은 내용에는 사용하면 안됨
- `v-show`
  - Expensive initial load, cheap toggle
  - 조건부 렌더링 중 하나로 항상 렌더링이 되어 DOM에는 남아있지만 display CSS 속성을 `hidden`으로 만들어 토글하는 것
  - 실제로 렌더링은 되지만 눈에서만 안보이는 것이기 때문에 한 번만 렌더링이 되는 경우라면 `v-if`에 비해 비용이 높음
  - 하지만 자주 변경되는 요소라면 한 번 렌더링 된 이후에는 보여주는지에 대한 여부만 판단하면 되기 때문에 토글 비용이 적음
- `v-if`, `v-else-if`, `v-else`
  - Cheap initial load, Expensive toggle
  - 조건부 렌더링 중 하나로 조건에 따라 directive의 표현식이 `true`일 때만 렌더링
  - 엘리먼트 및 포함된 directive는 토글하는 동안 삭제되고 다시 작성됨
  - 전달인자가 `false`인 경우 화면에서 보이지 않을 뿐만 아니라 렌더링 자체가 되지 않기 때문에 렌더링 비용이 낮음
  - 하지만 자주 변경되는 요소라면 매번 다시 렝더링 해야 하므로 비용이 증가할 수 있음
- `v-for`
  - 원본 데이터를 기반으로 엘리먼트 또는 템플릿 블록을 여러 번 렌더링
  - `item in items` 구문 사용
  - `item` 위치의 변수(객체의 경우에는 key)를 각 요소에서 사용할 수 있음
  - 사용 시 반드시 key 속성을 각 요소에 작성해야 함
  - `v-if`와 함께 사용하는 경우 `v-for`가 우선수위가 더 높지만 가능하면 동시에 사용하지 말 것
- `v-on`
  - 엘리먼트에 이벤트 리스너를 연결
  - 이벤트 유형은 전달인자로 표시함
  - 특정 이벤프가 발생했을 때 주어진 코드가 실행
  - 약어는 `@`
    - `v-on:click` -> `@click`
- `v-bind`
  - HTML 요소의 속성에 Vue의 상태 데이터를 값으로 할당
  - Object 형태로 사용하면 value가 `true`인 key가 class 바인딩 값으로 할당
  - 약어는 `:`
    - `v-bind:href` -> `:href`
- `v-model`
  - HTML요소의 값과 data를 양방향 바인딩
  - 수식어
    - `.lazy`: input 대신 change 이벤트 이후에 동기화
    - `.number`: 문자열을 숫자로 변경
    - `.trim`: 입력에 대한 trim(좌우 공백 제거)을 진행/