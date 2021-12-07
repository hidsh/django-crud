from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Member
from .forms import MemberForm

# 一覧
def index(request):
  # return HttpResponse('一覧')
    members = Member.objects.all().order_by('id')
    return render(request, 'members/index.html', {'members':members})

# 編集/新規登録
def edit(request, id=None):
    if id:  # idがあるときは編集。検索して結果を返すか404エラー
        member = get_object_or_404(Member, pk=id)
    else:   # idがないときは新規登録。メンバーを作成して追加
        member = Member()

    if request.method == 'POST':                    # POSTのとき
        # forms.py からフォームを生成
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():     # バリデーションOKなら保存
            member = form.save(commit=False)
            member.save()
            return redirect('crud_app:index')
    else:                                           # GETのとき
            form = MemberForm(instance=member)

    return render(request, 'members/edit.html', dict(form=form, id=id))

# 削除
def delete(request, id):
  # return HttpResponse('削除')
    member = get_object_or_404(Member, pk=id)
    member.delete()
    return redirect('crud_app:index')

# 詳細
def detail(request, id=None):
  # return HttpResponse('詳細')
    member = get_object_or_404(Member, pk=id)
    return render(request, 'members/detail.html', {'member':member})
