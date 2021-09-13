from .base import *

env_list = dict()
local_env = open(os.path.join(BASE_DIR, '.env'))
while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=')
    key = line[:start]
    value = line[start + 1:]
    env_list[key] = value

SECRET_KEY = env_list['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = [
    '*'  # 일단은 모든 ip가 가능하게
]


# 디플로이 환경 디비
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}