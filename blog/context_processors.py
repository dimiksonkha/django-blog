from blog.models import Post, UserProfileInfo,Tag,Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#Populating dictionary for all_posts, tags, categories, post years
def post_widget(request):
    all_posts = Post.objects.filter(status='published').order_by('published_date')
    years = []
    tags = Tag.objects.all()
    categories = Category.objects.all()

    for post in all_posts :
        year = post.published_date.year

        if year not in years:
            years.append(year)


    return {
    'all_posts':all_posts,
    'years':years,
    'tags':tags,
    'categories':categories
    }


# @login_required
# def user_profile_info(request):

    # if request.method == 'GET':
    #     current_user = request.user
    #
    # logged_in_user = UserProfileInfo.objects.get(user=current_user)
    # profile_pic = logged_in_user.profile_pic
    # return{
    # 'profile_pic':profile_pic
    # }
