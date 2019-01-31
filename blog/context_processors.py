from blog.models import Post

#Populating dictionary for all_posts, tags, categories, post years
def post_widget(request):
    all_posts = Post.objects.order_by('published_date')
    years = []
    tags = []
    categories = []

    for post in all_posts :
        year = post.published_date.year
        tag = post.tag
        category = post.category


        if year not in years:
            years.append(year)

        if tag not in tags:
            tags.append(tag)

        if category not in categories:
            categories.append(category)

    return {
    'all_posts':all_posts,
    'years':years,
    'tags':tags,
    'categories':categories
    }
