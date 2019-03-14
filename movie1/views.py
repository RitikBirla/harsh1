from django.shortcuts import render, HttpResponse
from . import forms
import hashlib


def matrix_detail(request):
    if request.method == 'POST':
        form = forms.MatrixForm(request.POST)
        if form.is_valid():
            r = form.cleaned_data['Row']
            c = form.cleaned_data['Column']
            sr = form.cleaned_data['Select_Dimension']
            data = form.cleaned_data['Data']
            size = r * c
            dlen = round(len(data)/2)
            if sr == 'Row':
                if size == dlen:
                    li = list(data.split(' '))
                    print(li)
                    mat = []
                    for i in range(r):
                        mat.append([])
                    for i in range(r):
                        for j in range(c):
                            mat[i].append(j)
                            mat[i][j] = 0
                    a = 0
                    for i in range(r):
                        for j in range(c):
                            mat[i][j] = li[a]
                            a = a + 1
                            print(mat)
                    md = str(mat)
                    bsdata = bytes(md, 'utf-8')
                    m = hashlib.sha256()
                    m.update(bsdata)
                    ensdata = m.digest()
                    print("after encryption by SHA-256 ", ensdata)
                    en = str(ensdata)
                    return HttpResponse(en)
                else:
                    raise HttpResponse("<h1>Data Not Entered Properly.</h1>")
            elif sr == 'Column':
                if size == dlen:
                    li = list(data.split(' '))
                    print(li)
                    mat = []
                    for i in range(c):
                        mat.append([])
                    for i in range(c):
                        for j in range(r):
                            mat[i].append(j)
                            mat[i][j] = 0
                    a = 0
                    for i in range(c):
                        for j in range(r):
                            mat[i][j] = li[a]
                            a = a + 1
                            print(mat)
                    md = str(mat)
                    bsdata = bytes(md, 'utf-8')
                    m = hashlib.sha256()
                    m.update(bsdata)
                    ensdata = m.digest()
                    print("after encryption by SHA-256 ", ensdata)
                    en = str(ensdata)
                    return HttpResponse(en)
            instance = form.save(commit=False)
            instance.auth = request.user
            instance.save()
            return render(request, 'data.html', context=None)
    else:
        form = forms.MatrixForm()
    return render(request, 'form.html', {'form': form})
