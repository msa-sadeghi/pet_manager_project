from django.shortcuts import render


from .models import Owner


def owner_detail(request, pk):
    owner = Owner.objects.get(id=pk)
    context = {"owner": owner}
    return render(request, "owners/detail.html", context)
