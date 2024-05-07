from django.shortcuts import render

def todo_list(request):
    nome = 'Leonardo'
    alunos = ["Paulo", "Naty", "Ana", "Leo"] 
    return render(request, 'todos/todo_list.html', {'nome': nome, 'alunos': alunos})
