from django.shortcuts import render, redirect
from projeto.models.Fabricante import Fabricante
from projeto.forms.FabricanteForm import FabricanteForm

def list_fabricante_view(request):
    fabricantes = Fabricante.objects.all()

    context = {
        "fabricantes": fabricantes
    }

    return render(
        request,
        "fabricante/fabricante.html",
        context
    )

def create_fabricante_view(request):
    if request.method == "POST":
        form = FabricanteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/fabricante")

    else:
        form = FabricanteForm()

    context = {
        "form": form
    }

    return render(
        request,
        "fabricante/fabricante-create.html",
        context
    )

def edit_fabricante_view(request,id=None):
    fabricante = Fabricante.objects.filter(id=id).first()

    if request.method == "POST":
        form = FabricanteForm(
            request.POST,
            instance=fabricante
        )

        if form.is_valid():
            form.save()
            return redirect("/fabricante")

    else:
        form = FabricanteForm(
            instance=fabricante
        )

    context = {

        "form": form,
        "fabricante": fabricante

    }

    return render(
        request,
        "fabricante/fabricante-edit.html",
        context
    )

def details_fabricante_view(request,id=None):
    fabricante = Fabricante.objects.filter(id=id).first()

    context = {
        "fabricante": fabricante
    }

    return render(
        request,
        "fabricante/fabricante-details.html",
        context
    )

def delete_fabricante_view(request,id=None):
    fabricante = Fabricante.objects.filter(id=id).first()

    if request.method == "POST":
        fabricante.delete()
        return redirect("/fabricante")

    context = {
        "fabricante": fabricante
    }

    return render(
        request,
        "fabricante/fabricante-delete.html",
        context
    )