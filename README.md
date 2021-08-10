#장고 프로젝트 WITH 박형석 강사님

###20210701 
프로젝트 만들고 시크릿 키 옮기고 정리함

SETTING.PY의 INSTALLED_APPS에 accountapp 추가

gitignore 만들어내고 이를 env파일을 반영함

urls.py에서 accountapp의 경로를 읽을 수 있게 하였음

port 번호는 좌측 위 드롭다운을 눌러서 컨피규어가 나오게 되는데 그것을 바꿔주면 된다.

###20210705

- base.html 작업 분할 extends와 include를 이용해서 head, header, footer로 작업공간을 분리했음
- extends를 이용해서 메인 작업공간을 블럭화했고 accountapp에서도 templates - accountapp을 만들어서 블럭을 다시 불러옴
- header와 footer를 꾸미기 (section과 div를 이용해서 구역을 다시 나누고 css text-align center 적용)
- 기존 CONTROLLER의 역할을 view.py에서 하고 있기에 이걸 잘 기억해야 하고 게시글을 잘 렌더링해서 단순한 html에 쿼리문을 이용해서 데이터를 수정할 수 있게 됨
- http://127.0.0.1:8000/accountapp.hello_world 를 설명해주심 http는 통신 프로토콜, ip주소, 페이지 경로 /// 그 후에 쿼리데이터를 파라메터값으로 받아온다는 거
- css를 꾸미기 위해 bootstrap과 googlefont를 사용한다고 한다.


###20210706

1. 부트스트랩의 navbar 적용 (혼자)
- googlefonts 가져와 사용
- 새로운 디렉토리인 static을 만들어서 css파일 만들어서 이를 가져오는 것으로 한다고 함
- 장고에서는 load static을 통해서 static에 있는 걸 불러서 사용하겠다고 해야 함
- static 폴더가 어디 있는지를 확인하고 해줘야해 
  https://docs.djangoproject.com/ko/3.2/howto/static-files/
- STATICFILES_DIRS = [ BASE_DIR / "static", '/var/www/static/', ] setting.py에 추가함
- display inline 태그 None도 있어
1. display - block
2. display - inline => text의 형태로 진행된다.
3. display - inline-block
4. display - none
- Hidden 을 하게 되면 아예 안보이는거야
- rem을 쓰는 이유 -> fontsize에 영향을 받음 
1. px은 부모 사이즈와 상관없이 무조건 고정
2. em은 부모의 사이즈가 커지거나 작아지는 비율을 모두 적용해서 한다는 거야
3. rem은 em과 조금 다른데 사이트마다 픽셀이 16정도인데 이걸 따라가냐 마냐라는거야
4. %는 부모의 크기 또는 너비에 맞춰서 움직이게 되는 것

###20210708
- em, rem 정리를 한번 다시 하셨음
- overflow => hidden, scroll로 설정할 수 있다 => overflow => scroll을 정히해보자
- migration : 장고가 변화를 반영하는 방법(데이터 베이스 스키마에 대해서)
1. model.py에 테이블을 만들어 준다.
2. python manage.py makemigrations 명령어를 침으로 0001_initial.py 에 스키마를 만들어준다
3. Migrations for 'accountapp': ==> 이렇게 모델이 완료되었다고 한다.
   accountapp\migrations\0001_initial.py
    - Create model HelloWorld
4. python manage.py migrate
-  Apply all migrations: accountapp, admin, auth, contenttypes, sessions가 적용이 된다는 것을 알 수 있다.
- GET . POST 
1. GET 방식에서는 파라메터에 값을 달아서 보내는 방식
2. POST 방식은 post + body에 내용을 실어서 서버로 보내는 방식

###20210712
1. POST 방식에서 input을 post 방식에서 보내고 싶다면 name으로 보내야 한다.
2. sqllite 연결 db 프로퍼티에 들어가게 되면 관련 드라이버가 깔리지 않은 것을 볼 수 있다.
3. view.py에서 model.py의 클래스인 HelloWorld를 불러왔고 이 안에 있는 text 를 다시 불러왔다.
그리고 이걸 temp 임시 변수가 받은 input을 넣어서 저장을 해줬다.
4. 그리고 이를 불러줄때는 항상 key가 중요하다. html과 view의 key를 맞추도록 하자
5. db에 저장된 열을 전부 꺼내고 싶다면 for endfor를 사용하고 
5. 모델의 클래스를 불러오고 objects를 부른다음 all로 전부를 꺼내오는 방법이 있다.
6. 매번 포스트를 하고 넘어가는 것이 그러니까 redirect을 해서 get으로 간 홈페이지를 불러와야한다.
7. 이를 view.py에서 HttpResponseRediect을 불러오고 reverse를 불러와서 해야 한다.
8. 주소를 다시 치기 귀찮아서 생기는 것이다.

###20210713
1. 장고가 CRUD를 만드는 걸 아주 적합한데 view로 로직을 잘 만들기로 좋다
- Class Based View 로 만들어야 한다. 왜냐하면 이미 만들었던 것이 Function Based View 형식인데 데이터의 attribute가 30개면 다 부르기 빡세다는 것
- view에서는 로직을 패턴이 있다. CRUD 패턴에 맞춰서 갈거임
2. 회원가입을 위한 create view 시작
- 모델을 만들어서 user로 받아주고
- form_class를 만들어서 일일히 다 부르고
- 이를 reverse사용했던 것 처럼 하되, 클래스에서 부르는 것이니까 reverse_lazy로 해야 한다.
- 그리고 template_name을 불러서 create,html로 회원가입 페이지를 만들어야 한다.
- path를 설정해야 하는데 urls.py에서 경로를 설정해준다.
3. create.html을 만들고 이를 회원가입 form으로 만들자
- extends로 base.html을 불러와주고
- 리다이렉을 해주려면  action="{% url 'accountapp:create' %} 로 url을 적고 리다이렉을 해준다.
- success_url = reverse_lazy('accountapp:hello world') 성공했다면 hello html을 불러줄 것이다.
- {{ form }} 이렇게 하면 UserCreationForm를 여기서는 회원가입 form을 만든걸 불러와준다는 거야 
- 참고로 비번을 암호화해주더라
- 참고로 회원가입 form은 그냥 있다는 것만 알면 된다.


###20210715
1. nav 버튼의 실용화
- 로그인 회원가입 버튼 생성
- 회원 로그인 여부 확인 user.is_authenticated 로 확인 유저 객체를 불러서 확인 가능
- bootstap에 적용하기
  
2. 회원가입 폼을 수정해보자
- django-bootstrap4 설치 및 해당 form 사용 설치함
- https://django-bootstrap4.readthedocs.io/en/latest/quickstart.html
퀵 스타터 따라감
  
- css 파일로 페이지 디자인을 바로적용하고 싶을때 f12 개발자 도구 - network - Disable cache를 체크해주자

3. 나눔글꼴 불러오기
- static 디렉토리에 글꼴 fonts 디렉토리를 만들기 
- 파일 넣고
- head.html에 style 태그로 적용

4. 회원정보 detail view 생성
- key를 가지고 정보를 받고 찾아오기
- 근데 어떻게 가져올거냐? context objects name으로 가자
- path.py에서 클래스를 만들고 DetailView를 불러와서 context_object_name을 쓰게끔 하고 target_user를 가져오게끔 한다.
- urls.py에서  'detail/<int:pk>' 를 하면서 요청한 user 객체의 해당 pk값을 가져와서 보겠다고 선언했어
- 그리고 target_user의 username을 부르고 date_joined 을 내부적으로 들어있는 것을 불러올 수 있다.

###0719
1. 사용자 정보 업데이트
- urls, view, detail,html 수정
2. 사용자 정보 탈퇴
- urls, view, detail,html 수정
3. 파라메터 값을 수정
- 본인 페이지가 아닌 타인 페이지를 파라메터값으로 옮겨다닐 수 있음 => if 구문으로 확인해주는 작업을 거치고
- update form을 UserCreationForm으로 하게 되면 안됨 => id가 바뀜
- 새로운 form을 만들어서 받아오자

###0720
1. Authentication 진행
- account를 update, delete 같은 경우 파라메터로 접근 타인 것을 지우는 것이 가능해서 로그인했을때만 할 수 있게끔 진행
- 로그인한 유저와 현재 보고 있는 페이지 유저와 같은지를 확인
2. Decorator
- 함수를 넘겨주는 것으로 할 것이다.
- decorated로 중복되는 것을 정리해준다는 거야

##0722
1. Decorator 추가
- @login_required로 로그인 여부 확인. 다만, 이것도 클래스 안의 메소드이기에 클래스 위에 써야 함.
- @method_decorator 이걸 적음
- @method_decorator(login_required, 'get') 이렇게 적음으로 get 메소드에 적용한다는 것을 명시함
- 다만, 로그인 여부만 확인하는 거만 했음 해당 유저가 그 유저인지는 알 수 없음
- 로그인했을때 안되는 부분을 맘대로 다른 유저의 정보를 지울 수 없게끔 하는 걸 만들어야 함
- decorator.py를 만듬으로 해당 유저가 맞는지 확인하는 걸 넣어주도록 하자
- has_ownership이라는 리스트를 만들어서 이를 넣어서 관리하는거로 했음

2. 슈퍼 유저 관리자 생성
- python manage.py createsuperuser
- 슈퍼계정을 하나만들 수 있음
- 관리자 페이지를 들어가서 확인할 수 있음 http://127.0.0.1:8000/admin/

3. profileapp 생성 ( detail page를 보완 개념 )
- 회원의 media를 적용하기 위해서 저장할 수 있고 불러올 수 있게끔 setting.py에 추가
- profileapp 생성 python manage.py startapp profileapp 
- urls, setting profileapp 추가 후 profileapp의 urls 추가


##0726
1. profileapp 설정
- model 설정 -> migration만들자 -> pillow가 없어서 설치 안됨(pip install pillow) -> python manage.py makemigrations, python manage.py migrate
-> makemigrations 는 모델에서 변화가 일어났는 것을 model에 차이가 있으면 변경사항을 감지해서 저장해주는 것 하지만 실제로 반영되지 않았어
-> migrate는 이제 모델에 실제로 반영을 해주는 거
  
2. forms 만들기

3. view 설정
- templates/profileapp 디렉토리 생성
- create.html 생성,  form 커스터마이징 진행 enctype="multipart/form-data" 추가
- multipart/form-data는 form 요소가 파일이나 이미지를 서버로 전송할 때 쓰임

##0727
1. Profile views.py에 form_valid를 추가
- user 속성이 model에 없는데 그걸 넣어주는 거야 유저를 할당해주는거야

2. profile info 추가
- detail.html에 profile info가 나오게끔 수정
- urls.py에  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)를 추가
- account detail.html, css 추가

3. profile update 추가
- profileapp의 views.py에 updateview 추가
- profileapp의 urls.py에 path (pk가 감안된) 추가
- accountapp의 detail에 추가할 수 있게 path 설정

##0729
1. profile 로그인해야 볼 수 있게끔 하자
- decorator 추가

2. profile update redirect 페이지 수정
- success_url = reverse_lazy('accountapp:hello world') 수정
- profile views.py에 get_success_url 추가
- accountapp views.py에 get_success_url 추가

3. accountapp update 단어를 구글 아이콘으로 수정하기

4. account detail.html 수정
- update, delete icons 추가

##0802
1. articleapp 추가
- python manage.py startapp articleapp
- main의 setting, urls 조정

2. Magic Grid 추가
- https://jsfiddle.net/eolaojo/4pov0rdf/
- https://github.com/e-oj/Magic-Grid/blob/master/dist/magic-grid.cjs.js
- list.html 수정

3. lorem picsum 추가
- https://picsum.photos/
- 개발자 탭에 사진을 언제 요청하고 가져오고 하는 걸 알 수 있는데 가져올때마다 레이아웃을 다시 정리해야해함
- 로딩될때마다 다시 해주는 것
- magicgrid에서 하는 걸 추가해줬음

4. article Model구축
- model.py 수정, python manage.py makemigrations, python manage.py migrate

##0803
1. Article create 만들기
- articleapp view에 createview 추가
- urls에 path 추가
- db에 보면 writer_id가 null로 되어있어
=> 이걸 해결해야해 
  view에 form_valid를 추가해줘야 해
  Cannot assign "<SimpleLazyObject: <django.contrib.auth.models.AnonymousUser object at 0x000001A824342730>>": "Article.writer" must be a "User" instance.
  로그인하고 나서 할 수 있게 해야해
  
2. Article detail 
- articleapp view에 detailview 추가
- urls에 path 추가
- detail.html 추가

3. Article update 
- articleapp view에 updateview 추가
- urls에 path 추가
- update.html 추가 create.html과 같아

4. Article detail.html 버튼 추가

5.  Article delete 
- articleapp view에 deleteview 추가
- urls에 path 추가
- delete.html create.html에서 아주 조금 고쳐서 가자

##0805
1. articlesapp decorator.py 추가
- 로그인 확인
- 해당 유저인지 아닌지 확인하는 거
- createview 에서는 successurl 추가 

2. Article detail.html 수정
- detail.html 수정
- base.css  추가

3. Article list 수정
- view.py에 ArticleListView 추가
- urls.py path 수정
- list.html 수정
- create button 추가
- pagination 추가
- include로 pagination.html 불러오기

##0809
1. CommentApp(댓글)
- Mixin : DetailView에서는 Form을 만들수가 없다.
- 다중 상속을 통해서 한다는 거야
- 그럼 form_class를 설정할 수 있게 된다.
- Create Delete만 만들거고 Success_url은 article과 관련되게 할 것이다.
- Model도 구축할거임
 
2.  시작
- python manage.py startapp commentapp
- setting.py, urls.py 설정하고 urls.py 추가

3. comment Model 구축
- python manage.py makemigrations
- python manage.py migrate
- forms.py 추가해서 form을 커스터마이징하자

4. comment create 구축
- views.py에 CommentCreateView 추가
- urls.py에 urlspattern 추가
- templates/commentapp create.html 추가

5. comment 댓글 article detail.html에 추가하기
- articleapp view.py에 ArticleDetailView에 FormMixin를 다중상속시킴 form_class = CommentCreationForm 추가
- detail.html에 {% include 'commentapp/create.html' %} 로 추가
- create.html에 url 이름 수정 및 target_article.pk 값 전송을 위해 input hidden 타입으로 전송
- commentapp view.py에 form_valid 추가 이때 article_pk를 input name으로 받아오기
  
- appname 수정 => urls.py의 app_name 수정, creta.html에 comments 수정

6. comment Delete 추가
- delete.html 추가, urls.py path 추가, view.py view 추가

##0810
1. 댓글 시각화
-  detail.html 수정
   - comment 삭제 버튼 추가
    - 로그인 확인
- CommentCreateView 로그인 확인
- CommentDeleteView 작성자 확인
- decorated.py 추가

2. 반응형으로 만들고 싶다.
- NGROK Tunneling Program => host가 allow가 안되서 에러가 날거임
    - setting.py에서 ALLOWED_HOSTS에 "*"로 모든 ip에서 접근할 수 있게끔
- meta 태그 추가 => 기기에 따라 달라지게
- <meta name="viewport" content="width=device-width, intial-scale=1.0, shrink-to-fit=no">
- shrink-to-fit=no는 파이어 폭스 전용