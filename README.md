# HanNune
Han Nune Live Chat Analytics Platform

### 1. python Django 설치
- python --version          : 3.10.2
- pip --version             : pip 22.0.3
- django-admin --version    : 4.0.3
- download : https://www.python.org/downloads/
- git bash 설치
1. 가상환경
    - 설치 : python -m venv vm
    - 실행 : 폴더 vm > Scripts >>> source activate
2. django
    - 설치 : pip install django
    - 프로젝트 생성 : django-admin startproject HanNune
    - 실행 : python manage.py runserver
3. vue.js & vuetify framework 설치
    - npm 설치
    - front end 가상환경 : vmFront
    - vue-cli 설치 : npm install -g @vue/cli
    - 프로젝트 생성 : vue create frontend -> vue2 선택
    - 실행 : cd frontend > npm run serve
    - vuetify framework 추가 : vue add vuetify > default 선택
    - vue ui : Vuetify 플러그인 설치 (선택사항)
    - Nuxt 설치 - Vuetify는 Nuxt Vuetify 모듈을 설치하여 추가가능
    - Nuxt 설치 : npm install @nuxtjs/vuetify -D
    - npm install vuetify
    - .eslintrc.json : babel error 해결
    - vue add electron-builder : Vuetify를 Electron과 사용 위해 plugin 추가
    - eslint 설치 : npm install eslint --save -dev
    - eslint 환경 설정 : npx eslint --init