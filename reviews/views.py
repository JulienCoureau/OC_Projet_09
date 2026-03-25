from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from reviews.models import Ticket, Review, UserFollows
from reviews.forms import TicketForm, ReviewForm, FollowUserForm
from itertools import chain

User = get_user_model()


@login_required
def feed(request):
    follows = UserFollows.objects.filter(user=request.user)
    followed_users = [follow.followed_user for follow in follows]
    followed_users.append(request.user)

    tickets = Ticket.objects.filter(user__in=followed_users)
    reviews = Review.objects.filter(user__in=followed_users)

    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'reviews/feed.html', {'posts': posts})


@login_required
def create_ticket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('feed')

    return render(request, 'reviews/create_ticket.html', {'form': form})


@login_required
def create_review(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('feed')
    else:
        form = ReviewForm()

    return render(request, 'reviews/create_review.html', {'form': form, 'ticket': ticket})


@login_required
def create_review_standalone(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()

            return redirect('feed')
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'reviews/create_review_standalone.html', context)


@login_required
def my_posts(request):
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)

    from itertools import chain
    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'reviews/my_posts.html', {'posts': posts})


@login_required
def follow_users(request):
    form = FollowUserForm()

    if request.method == 'POST':
        form = FollowUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user_to_follow = User.objects.get(username=username)

                if user_to_follow == request.user:
                    messages.error(request, "Vous ne pouvez pas vous suivre vous-même.")

                elif UserFollows.objects.filter(user=request.user, followed_user=user_to_follow).exists():
                    messages.warning(request, "Vous suivez déjà cet utilisateur.")

                else:
                    UserFollows.objects.create(user=request.user, followed_user=user_to_follow)
                    messages.success(request, f"Vous suivez maintenant {username} !")
                    return redirect('follow_users')

            except User.DoesNotExist:
                messages.error(request, "Cet utilisateur n'existe pas.")

    following = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)

    return render(request, 'reviews/follow_users.html', {
        'form': form,
        'following': following,
        'followers': followers
    })


@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)

    follow_relation = UserFollows.objects.filter(user=request.user, followed_user=user_to_unfollow)

    if follow_relation.exists():
        follow_relation.delete()
        messages.success(request, f"Vous ne suivez plus {user_to_unfollow.username}.")
    else:
        messages.warning(request, "Vous ne suiviez pas cet utilisateur.")

    return redirect('follow_users')


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    form = TicketForm(instance=ticket)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('my_posts')
    return render(request, 'reviews/edit_ticket.html', {'form': form, 'ticket': ticket})


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == 'POST':
        ticket.delete()
        return redirect('my_posts')
    return render(request, 'reviews/delete_confirm.html')


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('my_posts')
    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('my_posts')
    return render(request, 'reviews/delete_confirm.html')
 