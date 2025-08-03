from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Post
from .forms import PostForm, ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'bookshelf/post_list.html', {'posts': posts})

@permission_required('bookshelf.can_view', raise_exception=True)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'bookshelf/post_detail.html', {'post': post})

@permission_required('bookshelf.can_create', raise_exception=True)
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'bookshelf/post_form.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'bookshelf/post_form.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def example_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
