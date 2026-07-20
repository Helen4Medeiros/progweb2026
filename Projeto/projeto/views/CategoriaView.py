from django.shortcuts import render, redirect
from projeto.models.Categoria import Categoria

def list_categoria_view(request, id=None):
    categorias = Categoria.objects.all()

    if id is not None:
        categorias = categorias.filter(id=id)

    context = {
        "categorias": categorias
    }

    return render(
        request,
        "categoria/categoria.html",
        context=context,
        status=200
    )

def create_categoria_view(request):
    if request.method == "POST":
        nome = request.POST.get("Categoria")

        try:
            categoria = Categoria()
            categoria.Categoria = nome
            categoria.save()
            print("Categoria salva com sucesso")

        except Exception as e:
            print(e)

        return redirect("/categoria")

    return render(
        request,
        "categoria/categoria-create.html",
        status=200
    )

def edit_categoria_view(request, id=None):
    categoria = Categoria.objects.filter(id=id).first()

    context = {
        "categoria": categoria
    }

    return render(
        request,
        "categoria/categoria-edit.html",
        context=context,
        status=200
    )

def edit_categoria_postback(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nome = request.POST.get("Categoria")

        try:
            categoria = Categoria.objects.filter(id=id).first()
            categoria.Categoria = nome
            categoria.save()
            print("Categoria editada")

        except Exception as e:
            print(e)

    return redirect("/categoria")

def details_categoria_view(request, id=None):
    categoria = Categoria.objects.filter(id=id).first()

    context = {
        "categoria": categoria
    }

    return render(
        request,
        "categoria/categoria-details.html",
        context=context,
        status=200
    )

def delete_categoria_view(request, id=None):
    categoria = Categoria.objects.filter(id=id).first()

    context = {
        "categoria": categoria
    }

    return render(
        request,
        "categoria/categoria-delete.html",
        context=context,
        status=200
    )

def delete_categoria_postback(request):
    if request.method == "POST":
        id = request.POST.get("id")

        try:
            categoria = Categoria.objects.filter(id=id).first()
            categoria.delete()
            print("Categoria removida")

        except Exception as e:
            print(e)

    return redirect("/categoria")