# Django

## 1. Web Framework

### Web

- World Wide Web
- 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 전 세계적인 정보 공간



### Static Web Page(정적 웹 페이지)

- 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
- 서버가 정적 웹 페이지에 대한 요청을 받아 추가적인 처리 없이 클라이언트에게 응답을 보냄
- 모든 상황에서 모든 사용자에게 동일한 정보 표시
- 일반적으로 HTML, CSS, JavaScript로 작성됨
- flat page라고도 함



### Dynamic Web Page(동적 웹 페이지)

- 웹 페이지에 대한 요청을 받은 경우 서버가 추가정인 처리 과정을 거쳐 클라이언트에게 응답을 보냄
- 동적 웹 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
- 서버 사이드 프로그래밍 언어(Python, Java, C++ 등)가 사용되며 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐



### Framework

- 프로그래밍에서 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
- 재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움
- Application framework 라고도 함



### Web Framework

- **웹 서비스는 클라이언트가 서버로 요청을 보내고 서버가 클라이언트에게 응답을 보내는 과정**
- 이 때 서버의 구성을 편리하게 해주는 것이 Framework 이며 그 한 종류가 Django
- 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적으로 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함
- 동적인 웹 페이지나 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 application framework의 일종



### Framework Architecture

- MVC Design Pattern(model-view-controller)
- 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
- 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
- Django는 MTV Pattern이라고 함



### MTV Pattern

- Model
  - 응용프로그램의 **데이터 구조**를 정의하고 **데이터베이스**의 기록을 관리(추가, 수정, 삭제)
- Template
  - 파일의 구조나 레이아웃을 정의
  - **실제 내용을 보여주는데 사용**
- View
  - **중간관리자 역할**
  - HTTP 요청을 수신하고 HTTP 응답을 반환
  - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  - Template에게 응답의 서식 설정을 맞김

![Django - files for views, model, urls, template](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction/basic-django.png)

- 전체적인 구조는 요청이 들어왔을 때 urls.py에서 어떤 함수를 호출할 지 확인하고, views.py에서 적절함 함수를 호출
- 이후 models.py에 정의된 데이터 구조에 따라 데이터를 읽거나 쓰고, 지정된 템플릿을 응답





## 3. 진행 순서

```bash
# 환경 세팅
$ python -m venv venv				# 가상환경 생성
$ source venv/Scripts/activate		# 가상환경 활성화
$ pip install django==3.2.12		# 버전 3.2.12로 설치
$ pip install -r requirments		# 혹은 requirements 그대로 설치

# 프로젝트 생성
$ django-admin startproject pjt01 .	# 프로젝트 이름에 하이픈(-)과 사용중인 키워드 사용 불가, 마지막에 . 잊지않기
$ python manage.py runserver		# 서버 실행
$ python manage.py startapp app01	# 어플리케이션 생성, 일반적으로는 어플리케이션 이름으로 복수형 사용 권장
```



## 4. 프로젝트 구조

- `BASE_DIR/`

> `	pjt01/`
>
> > `__init__.py`: 파이썬이 이 디렉토리를 하나의 파이썬 패키지로 다루도록 지시
> >
> > `asgi.py`: Asynchronous Server Gateway Interface, 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
> >
> > `settings.py`: 모든 설정을 포함
> >
> > - 수정이 필요한 부분
> >
> >   ```python
> >   INSTALLED_APPS = [
> >       # 순서도 중요!
> >   	# Local apps
> >       'app01',				# 앱 생성시 등록
> >   
> >       # Third party
> >       'django_extensions',	# 추가기능 사용 위해 등록
> >       
> >       # Django apps
> >       'django.contrib.admin',
> >       'django.contrib.auth',
> >       'django.contrib.contenttypes',
> >       'django.contrib.sessions',
> >       'django.contrib.messages',
> >       'django.contrib.staticfiles',
> >   ]
> >   
> >   TEMPLATES = [
> >       {
> >           'BACKEND': 'django.template.backends.django.DjangoTemplates',
> >           'DIRS': [BASE_DIR / 'templates',],	# base.html을 만들어 기본 템플릿으로 활용 시 경로 등록
> >           'APP_DIRS': True,
> >           'OPTIONS': {
> >               'context_processors': [
> >                   'django.template.context_processors.debug',
> >                   'django.template.context_processors.request',
> >                   'django.contrib.auth.context_processors.auth',
> >                   'django.contrib.messages.context_processors.messages',
> >               ],
> >           },
> >       },
> >   ]
> >   
> >   LANGUAGE_CODE = 'ko-kr'		# 언어 설정
> >   
> >   TIME_ZONE = 'Asia/Seoul'	# 시각 설정
> >   ```
> >
> > `urls.py`: 사이트의 url과 적절한 views의 연결을 지정
> >
> > - 기본 구조
> >
> >   ```python
> >   from django.contrib import admin
> >   from django.urls import path, include
> >   
> >   urlpatterns = [
> >       path('admin/', admin.site.urls),		# Django는 기본적으로 admin 페이지 지원
> >       path('app01/', include('app01.urls')),	# 프로젝트의 urls.py의 역할은 특정 앱으로 요청이 들어오면 해당 앱으로 연결하는 것
> >   ]
> >   ```
> >
> > `wsgi.py`: Web Server Gateway Interface, 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
> `manage.py`: Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
>
> - Django와 관련된 명령어를 실행할 때 호출
>
>   ```bash
>   $ python manage.py <conmmad> [options]
>   ```