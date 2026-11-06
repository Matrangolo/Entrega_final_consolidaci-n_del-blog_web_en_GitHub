
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Post
from .forms import PostForm


def inicio(request):
    posts = Post.objects.filter(
        estado='publicado'
    ).order_by('-fecha_creacion')

    return render(
        request,
        'posts/inicio.html',
        {'posts': posts}
    )


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.estado == 'borrador':
        if not request.user.is_authenticated or post.autor != request.user:
            return HttpResponseForbidden(
                'No tenés permiso para ver este borrador.'
            )

    return render(
        request,
        'posts/detalle.html',
        {'post': post}
    )


@login_required
def crear_post(request):
    if request.method == 'POST':
        formulario = PostForm(request.POST, request.FILES)

        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.autor = request.user
            post.save()

            return redirect('detalle_post', pk=post.pk)
    else:
        formulario = PostForm()

    return render(
        request,
        'posts/formulario.html',
        {'formulario': formulario, 'titulo': 'Crear publicación'}
    )


@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.autor != request.user:
        return HttpResponseForbidden(
            'No tenés permiso para editar esta publicación.'
        )

    if request.method == 'POST':
        formulario = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        formulario = PostForm(instance=post)

    return render(
        request,
        'posts/formulario.html',
        {'formulario': formulario, 'titulo': 'Editar publicación'}
    )


@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.autor != request.user:
        return HttpResponseForbidden(
            'No tenés permiso para eliminar esta publicación.'
        )

    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')

    return render(
        request,
        'posts/confirmar_eliminar.html',
        {'post': post}
    )
