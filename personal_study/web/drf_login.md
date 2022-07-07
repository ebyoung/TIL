```bash
$ pip install dj-rest-auth
$ pip install django-allauth
```

- `settings.py`

```python
INSTALLED_APPS = [
    ...,
    # token base authentication
    'rest_framework.authtoken',
    # DRF auth
    'dj_rest_auth',  # signup 제외 auth 관련 담당
    'dj_rest_auth.registration',  # signup 담당

    # signup 담당을 위해 필요 
    'allauth', 
    'allauth.account',
    'allauth.socialaccount',
    ...
    'django.contrib.sites',  # dj-rest-auth signup 필요
]

SITE_ID = 1

# 맨 아래
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 모두에게 허용
        # 'rest_framework.permissions.AllowAny', 

        # 인증된 사용자만 모든일이 가능 / 비인증 사용자는 모두 401 Unauthorized
        'rest_framework.permissions.IsAuthenticated'
    ]
}
```

- `project/urls.py`

```python
urlpatterns = [
    ...,
    path('api/v1/accounts/', include('dj_rest_auth.urls')),
    path('api/v1/accounts/signup/', include('dj_rest_auth.registration.urls')),
]
```

