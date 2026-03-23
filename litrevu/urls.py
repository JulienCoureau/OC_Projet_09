"""
URL configuration for litrevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authentication.views
import reviews.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.LoginPageView.as_view(), name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('feed/', reviews.views.feed, name='feed'),
    path('my-posts/', reviews.views.my_posts, name='my_posts'),
    path('ticket/create/', reviews.views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/create-review/', reviews.views.create_review, name='create_review'),
    path('review/create/', reviews.views.create_review_standalone, name='create_review_standalone'),
    path('follow-users/', reviews.views.follow_users, name='follow_users'),
    path('unfollow/<int:user_id>/', reviews.views.unfollow_user, name='unfollow_user'),
    path('feed/', reviews.views.feed, name='feed'),
    path('ticket/<int:ticket_id>/edit/', reviews.views.edit_ticket, name='edit_ticket'),
    path('ticket/<int:ticket_id>/delete/', reviews.views.delete_ticket, name='delete_ticket'),
    path('review/<int:review_id>/edit/', reviews.views.edit_review, name='edit_review'),
    path('review/<int:review_id>/delete/', reviews.views.delete_review, name='delete_review'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
