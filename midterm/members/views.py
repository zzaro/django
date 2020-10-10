from django.shortcuts import render
from django.views.generic import ListView, DetailView
from members.models import Members
from django.views.generic import FormView
from members.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
class MembersLV(ListView):
    model = Members


class MembersDV(DetailView):
    model = Members


class SearchFormView(FormView):
    form_class = PostSearchForm # 폼으로 사용할 클래스는 PostSearchForm 클래스.
    template_name = 'blog/post_search.html' # SearchFormView에서 호출할 html 문서 지정.

    # POST 요청으로 들어온 데이터의 유효성 검사. 에러가 없으면 form_valid() 실행
    def form_valid(self, form):
        # 유효성 검사 통과시 사용자가 입력한 데이터들은 cleaned_data 사전에 존재.
        # 이 사전에서 serch_word 값을 추출해 serachWord 변수에 지정. search_word 키는 PostSearchForm 클래스에서 정의한 필드명.
        searchWord = form.cleaned_data['search_word']
        # Q객체 : filter()메소드의 매칭 조건을 다양하게 지정.
        # icontains : 대소문자를 구분하지 않고 단어가 포함되어 있는지 검사.
        # distinct : 중복된 객체 제외
        members_list = Members.objects.filter(Q(name__icontains=searchWord)|Q(tel__icontains=searchWord)|Q(address__icontains=searchWord)|Q(email__icontains=searchWord)).distinct()

        # 컨텍스트 변수
        context={}
        context['form']=form # form(PostSearchForm) 객체를 컨텍스트 변수 form에 지정
        context['search_term']=searchWord # 검색용 단어 searchWord를 컨텍스트 변수 search_term에 저장
        context['object_list']=members_list # 검색 결과 리스트인 post_list를 컨텍스트 변수 object_list에 지정.

        return render(self.request, self.template_name, context)
