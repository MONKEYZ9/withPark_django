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

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'  # 일단은 모든 ip가 가능하게
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# 로컬 환경 디비
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}