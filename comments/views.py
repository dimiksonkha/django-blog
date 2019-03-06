from django.shortcuts import render
from .models import Comment,Reply

# Create your views here.
#Comment submission by logged in user
@login_required
def submit_comment(request):

    if request.method == 'POST' :

        comment_title = request.POST.get('comment_title')
        comment_content = request.POST.get('comment_content')
        post_id = request.POST.get('post_id')
        current_user = request.user
        profile = UserProfileInfo.objects.get(user=current_user)

        c = Comment()
        c.post = Post.objects.get(id=post_id)
        c.content = comment_content
        c.author = UserProfileInfo.objects.get(id=profile.id)
        c.published_date = datetime.now()
        c.save()

    return HttpResponseRedirect(reverse('blog:post_details', args=(post_id, )))

#Reply submission by logged in user
@login_required
def submit_reply(request):

    if request.method == 'POST' :
        post_id = request.POST.get('post_id')
        reply_title = request.POST.get('reply_title')
        reply_content = request.POST.get('reply_content')
        comment_id = request.POST.get('comment_id')
        current_user = request.user
        profile = UserProfileInfo.objects.get(user=current_user)

        r = Reply()
        r.comment = Comment.objects.get(id=comment_id)
        r.content = reply_content
        r.author = UserProfileInfo.objects.get(id=profile.id)
        r.published_date = datetime.now()
        r.save()

    return HttpResponseRedirect(reverse('blog:post_details', args=(post_id, ))) # have to work here
