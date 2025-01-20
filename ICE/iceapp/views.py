import random
from django.shortcuts import render, get_object_or_404,redirect
from django import template
from django.urls import reverse
from .models import Person, InstitutionBuilding, ChurchAndOtherBuilding, MajorCelebrationHistoricalEvent,ChurchCommunity,Comment
from django.http import JsonResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .forms import CustomUserCreationForm, CommentForm,CommentDeleteForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseForbidden
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from collections import defaultdict
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings




def person_detail(request, pk):
    person = Person.objects.get(pk=pk)
    content_type = ContentType.objects.get_for_model(person)
    comments = Comment.objects.filter(content_type=content_type, object_id=person.id).order_by('-created_at')

    context = {
        'person': person,
        'content_type': content_type,
        'object': person,
        'comments': comments,
        'comment_form': CommentForm(),
    }
    return render(request, 'person_detail.html', context)

def church_community_detail(request, pk):
    community = get_object_or_404(ChurchCommunity, pk=pk)
    content_type = ContentType.objects.get_for_model(community)
    comments = Comment.objects.filter(content_type=content_type, object_id=pk).order_by('-created_at')
    language_code = request.session.get('lang', 'en')
    
    context = {
        'community': community,
        'content_type': content_type,
        'object': community,
        'comments': comments,
        'comment_form': CommentForm(),
         'LANGUAGE_CODE': language_code,
    }
    return render(request, 'church_community_detail.html', context)


def institution_building_detail(request, pk):
    institution = get_object_or_404(InstitutionBuilding, pk=pk)
    content_type = ContentType.objects.get_for_model(institution)
    comments = Comment.objects.filter(content_type=content_type, object_id=pk).order_by('-created_at')
    
    context = {
        'institution': institution,
        'content_type': content_type,
        'object': institution,
        'comments': comments,
        'comment_form': CommentForm(),
    }
    return render(request, 'institution.html', context)


def church_and_other_building_detail(request, pk):
    church_and_other_building = get_object_or_404(ChurchAndOtherBuilding, pk=pk)
    content_type = ContentType.objects.get_for_model(church_and_other_building)
    comments = Comment.objects.filter(content_type=content_type, object_id=pk).order_by('-created_at')
    
    context = {
        'church_and_other_building': church_and_other_building,
        'content_type': content_type,
        'object': church_and_other_building,
        'comments': comments,
        'comment_form': CommentForm(),
    }
    return render(request, 'church_and_other_building_detail.html', context)


def major_celebration_historical_event_detail(request, pk):
    celebration = get_object_or_404(MajorCelebrationHistoricalEvent, pk=pk)
    content_type = ContentType.objects.get_for_model(celebration)
    comments = Comment.objects.filter(content_type=content_type, object_id=pk).order_by('-created_at')
    
    context = {
        'celebration': celebration,
        'content_type': content_type,
        'object': celebration,
        'comments': comments,
        'comment_form': CommentForm(),
    }
    return render(request, 'major_celebration_historical_event_detail.html', context)


def main_page(request):
    persons = Person.objects.all()
    institutions = InstitutionBuilding.objects.all()
    buildings = ChurchAndOtherBuilding.objects.all()
    events = MajorCelebrationHistoricalEvent.objects.all()
    return render(request, 'mainpage.html', {
        'persons': persons,
        'institutions': institutions,
        'buildings': buildings,
        'events': events
    })




def search_suggestions(request):
    query = request.GET.get('q', '')
    suggestions = []

    if query:
        # Search each model
        person_results = Person.objects.filter(name__icontains=query)
        institution_results = InstitutionBuilding.objects.filter(name__icontains=query)
        building_results = ChurchAndOtherBuilding.objects.filter(name__icontains=query)
        event_results = MajorCelebrationHistoricalEvent.objects.filter(name__icontains=query)
        community_results = ChurchCommunity.objects.filter(name__icontains=query)

        # Combine results with their respective type and URLs
        suggestions.extend([
            {'name': result.name, 'type': 'person', 'url': reverse('person_detail', args=[result.id])}
            for result in person_results
        ])
        suggestions.extend([
            {'name': result.name, 'type': 'institution', 'url': reverse('institution_building_detail', args=[result.id])}
            for result in institution_results
        ])
        suggestions.extend([
            {'name': result.name, 'type': 'building', 'url': reverse('church_and_other_building_detail', args=[result.id])}
            for result in building_results
        ])
        suggestions.extend([
            {'name': result.name, 'type': 'event', 'url': reverse('major_celebration_historical_event_detail', args=[result.id])}
            for result in event_results
        ])
        suggestions.extend([
            {'name': result.name, 'type': 'community', 'url': reverse('church_community_detail', args=[result.id])}
            for result in community_results
        ])

    return JsonResponse({'suggestions': suggestions})


def search_results(request):
    query = request.GET.get('q', '')
    suggestions = []

    if query:
        # Search each model
        person_results = Person.objects.filter(name__icontains=query)
        institution_results = InstitutionBuilding.objects.filter(name__icontains=query)
        building_results = ChurchAndOtherBuilding.objects.filter(name__icontains=query)
        event_results = MajorCelebrationHistoricalEvent.objects.filter(name__icontains=query)
        community_results = ChurchCommunity.objects.filter(name__icontains=query)

        # Combine results with their respective type and URLs
        suggestions.extend([
            {'name': result.name, 'type': 'person', 'url': reverse('person_detail', args=[result.id])}
            for result in person_results
        ])
        suggestions.extend([
            {'name': result.name, 'type': 'institution', 'url': reverse('institution_building_detail', args=[result.id])}
            for result in institution_results
        ])
        suggestions.extend([
            {'name': result.name, 'type': 'building', 'url': reverse('church_and_other_building_detail', args=[result.id])}
            for result in building_results
        ])
        suggestions.extend([
            {'name': result.name, 'type': 'event', 'url': reverse('major_celebration_historical_event_detail', args=[result.id])}
            for result in event_results
        ])
        suggestions.extend([
            {'name': result.name, 'type': 'community', 'url': reverse('church_community_detail', args=[result.id])}
            for result in community_results
        ])

    return render(request, 'search_results.html', {'suggestions': suggestions})
# ------------------------------------------------------------------------------------------------------------------------ #

def index(request):
    communities=ChurchCommunity.objects.all().order_by('name')
    persons = Person.objects.all().order_by('name')
    institutions = InstitutionBuilding.objects.all().order_by('name')
    buildings = ChurchAndOtherBuilding.objects.all().order_by('name')
    events = MajorCelebrationHistoricalEvent.objects.all().order_by('name')

    articles = list(ChurchAndOtherBuilding.objects.all())
    blog_posts = list(MajorCelebrationHistoricalEvent.objects.all())
    news_items = list(InstitutionBuilding.objects.all())
    person=list(Person.objects.all())
    communnity=list(ChurchCommunity.objects.all())


    # Combine all entries into one list
    all_content = articles + blog_posts + news_items + person + communnity

    # Select a random entry
    random_content = None
    if all_content:
        random_content = random.choice(all_content)
        random_content_about=' '.join(random_content.about.split()[:70])
        random_content_name=random_content.name

        if isinstance(random_content, ChurchCommunity):
            random_content_url = reverse('church_community_detail', args=[random_content.pk])
        elif isinstance(random_content, Person):
            random_content_url = reverse('person_detail', args=[random_content.pk])
        elif isinstance(random_content, InstitutionBuilding):
            random_content_url = reverse('institution_building_detail', args=[random_content.pk])
        elif isinstance(random_content, ChurchAndOtherBuilding):
            random_content_url = reverse('church_and_other_building_detail', args=[random_content.pk])
        elif isinstance(random_content, MajorCelebrationHistoricalEvent):
            random_content_url = reverse('major_celebration_historical_event_detail', args=[random_content.pk])



    return render(request, 'index.html', {
        'persons': persons,
        'institutions': institutions,
        'buildings': buildings,
        'events': events,
        'community':communities,
        'random_article_about':random_content_about,
        'random_article_name':random_content_name,
        'random_article_url': random_content_url,
    })



def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'User already exists')
            else:
                print(form)
                form.save()
                return redirect('login')
    else:
        form = CustomUserCreationForm()
        print('hello')
    return render(request, 'login_register.html', {'register_form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')  # Redirect to a home page or wherever you want
    else:
        form = AuthenticationForm()
    return render(request, 'login_register.html', {'form': form})

def login(request):
    form=CustomUserCreationForm()
    return render(request, 'login_register.html', {'form':form})

def like_or_dislike(request, model_name, object_id, action):
    # Map model names to actual models
    model_mapping = {
        'church_and_other_building': ChurchAndOtherBuilding,
        'person': Person,
        'institution': InstitutionBuilding,
        'community': ChurchCommunity,
        'celebration': MajorCelebrationHistoricalEvent,
    }

    model = model_mapping.get(model_name)
    if not model:
        return JsonResponse({'error': 'Invalid model name'}, status=400)

    obj = get_object_or_404(model, id=object_id)
    user = request.user

    if action == 'like':
        if user in obj.dislikes.all():
            obj.dislikes.remove(user)
        if user in obj.likes.all():
            obj.likes.remove(user)
        else:
            obj.likes.add(user)
    elif action == 'dislike':
        if user in obj.likes.all():
            obj.likes.remove(user)
        if user in obj.dislikes.all():
            obj.dislikes.remove(user)
        else:
            obj.dislikes.add(user)
    else:
        return JsonResponse({'error': 'Invalid action'}, status=400)

    return JsonResponse({
        'likes_count': obj.likes.count(),
        'dislikes_count': obj.dislikes.count(),
        'user_has_liked': user in obj.likes.all(),
        'user_has_disliked': user in obj.dislikes.all()
    })

def load_comments(request, model_name, object_id, offset=0):
    models = {
        'church_and_other_building': ChurchAndOtherBuilding,
        'institution_building': InstitutionBuilding,
        'person': Person,
        'major_celebration_historical_event': MajorCelebrationHistoricalEvent,
        'churchcommunity':ChurchCommunity
    }
    
    model = models.get(model_name)
    obj = get_object_or_404(model, id=object_id)
    
    comments = Comment.objects.filter(content_type__model=model_name, object_id=object_id).order_by('-created_at')[offset:offset+5]
    comments_data = [{
        'user': comment.user.username,
        'comment': comment.comment,
        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M'),
    } for comment in comments]
    return JsonResponse({'comments': comments_data})

@require_POST
def add_comment(request, content_type_id, object_id):
    content_type = ContentType.objects.get(id=content_type_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.content_type = content_type
        comment.object_id = object_id
        comment.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid form submission'})

@login_required
def delete_comment(request, comment_id):
    if request.method == 'POST':
        # Retrieve the comment or return 404 if not found
        comment = get_object_or_404(Comment, id=comment_id)

        # Check if the user is authorized to delete the comment
        if request.user == comment.user or request.user.is_staff:
            try:
                comment.delete()
                return JsonResponse({'success': True})
            except Exception as e:
                # Log the exception for debugging
                print(f"An error occurred while deleting the comment: {e}")
                return JsonResponse({'success': False, 'error': 'An error occurred while deleting the comment'})
        else:
            return JsonResponse({'success': False, 'error': 'You do not have permission to delete this comment'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    


def new_index(request):
    # Fetch all objects and categorize them
    categories = {
        'Person': {
            'Clergy': list(Person.objects.filter(category='Clergy')),
            'Laity': list(Person.objects.filter(category='Laity')),
            'Saints': list(Person.objects.filter(category='Saints')),
            'Eminent Persons': list(Person.objects.filter(category='Eminent Persons')),
        },
        'Institution': {
            'Universities': list(InstitutionBuilding.objects.filter(category='Universities')),
            'Colleges': list(InstitutionBuilding.objects.filter(category='Colleges')),
            'Schools': list(InstitutionBuilding.objects.filter(category='Schools')),
            'Technical Institutions': list(InstitutionBuilding.objects.filter(category='Technical Institutions')),
            'Medical Colleges': list(InstitutionBuilding.objects.filter(category='Medical Colleges')),
            'Hospitals': list(InstitutionBuilding.objects.filter(category='Hospitals')),
            'Charity Institutions': list(InstitutionBuilding.objects.filter(category='Charity Institutions')),
            'Amenity Centres': list(InstitutionBuilding.objects.filter(category='Amenity Centres')),
        },
        'community':{
            'Communities':list(ChurchCommunity.objects.filter(category='Communities')),
            'Diocese':list(ChurchCommunity.objects.filter(category='Diocese')),
            'Congregations':list(ChurchCommunity.objects.filter(category='Congregations')),
            'Pios Associations':list(ChurchCommunity.objects.filter(category='Pios Associations'))
        },
        'church':{
            'Basilica':list(ChurchAndOtherBuilding.objects.filter(category='Basilica')),
            'Cathedrals':list(ChurchAndOtherBuilding.objects.filter(category='Cathedrals')),
            'Parishes':list(ChurchAndOtherBuilding.objects.filter(category='Parishes')),
            'Pilgrime Centers':list(ChurchAndOtherBuilding.objects.filter(category='Pilgrime Centers'))
        },
        'event':{
            'Historical Events':list(MajorCelebrationHistoricalEvent.objects.filter(category='Historical Events')),
            'Major Celebrations':list(MajorCelebrationHistoricalEvent.objects.filter(category='Major Celebrations'))
        }
    }
    
    all_content = (
        list(ChurchAndOtherBuilding.objects.all()) +
        list(MajorCelebrationHistoricalEvent.objects.all()) +
        list(InstitutionBuilding.objects.all()) +
        list(Person.objects.all()) +
        list(ChurchCommunity.objects.all())
    )

    # Select 6 random entries
    random_articles = random.sample(all_content, 6 if len(all_content) >= 6 else len(all_content))

    # Prepare context data with URLs and about text
    articles_data = []
    for article in random_articles:
        if isinstance(article, ChurchCommunity):
            url = reverse('church_community_detail', args=[article.pk])
        elif isinstance(article, Person):
            url = reverse('person_detail', args=[article.pk])
        elif isinstance(article, InstitutionBuilding):
            url = reverse('institution_building_detail', args=[article.pk])
        elif isinstance(article, ChurchAndOtherBuilding):
            url = reverse('church_and_other_building_detail', args=[article.pk])
        elif isinstance(article, MajorCelebrationHistoricalEvent):
            url = reverse('major_celebration_historical_event_detail', args=[article.pk])

        articles_data.append({
            'name': article.name,
            'about': ' '.join(article.about.split()[:25]) + '...',  # Truncated about text
            'url': url,
            'image': article.about_image.url if article.about_image else ''  # Handle missing images
        })

    # Pass the data to the template
    content = {'articles_data': articles_data,'categories': categories}

    return render(request, '2ndindex.html',content)

def category_view(request, category_name):
    # Fetch all content in the selected category
    persons = Person.objects.filter(category=category_name).order_by('name')
    institutions = InstitutionBuilding.objects.filter(category=category_name).order_by('name')
    church_communities = ChurchCommunity.objects.filter(category=category_name).order_by('name')
    celebrations = MajorCelebrationHistoricalEvent.objects.filter(category=category_name).order_by('name')
    churches=ChurchAndOtherBuilding.objects.filter(category=category_name).order_by('name')

    # Create a context dictionary and add only non-empty querysets
    context = {'category_name': category_name}

    if persons.exists():
        grouped_persons = defaultdict(list)
        for person in persons:
            grouped_persons[person.name[0].upper()].append(person)
        context['grouped_persons'] = sorted(grouped_persons.items())

    if institutions.exists():
        grouped_institutions = defaultdict(list)
        for institution in institutions:
            grouped_institutions[institution.name[0].upper()].append(institution)
        context['grouped_institutions'] = sorted(grouped_institutions.items())

    if church_communities.exists():
        grouped_church_communities = defaultdict(list)
        for community in church_communities:
            grouped_church_communities[community.name[0].upper()].append(community)
        context['grouped_church_communities'] = sorted(grouped_church_communities.items())
        print(context['grouped_church_communities'])  # Debug statement

    if celebrations.exists():
        grouped_celebrations = defaultdict(list)
        for celebration in celebrations:
            grouped_celebrations[celebration.name[0].upper()].append(celebration)
        context['grouped_celebrations'] = sorted(grouped_celebrations.items())
        
    if churches.exists():
        grouped_churches = defaultdict(list)
        for churches in churches:
            grouped_churches[churches.name[0].upper()].append(churches)
        context['grouped_churches'] = sorted(grouped_churches.items())
    
    print(context)
    return render(request, 'main/searchres.html', context)



from django.http import HttpResponseRedirect
from django.utils import translation
from django.shortcuts import redirect

def set_language(request):
    # Get the language code from the query parameters (default to 'en')
    language_code = request.GET.get('lang', 'en')

    # Activate the chosen language
    translation.activate(language_code)

    # Store the language code in the session (no need for LANGUAGE_SESSION_KEY)
    request.session['lang'] = language_code

    # Redirect to the next page (default to '/')
    next_url = request.GET.get('next', '/')
    return HttpResponseRedirect(next_url)

def mfa(request):
    return render(request, 'main/verify_otp.html')


def signup(request):
    if request.method == 'POST':
        # Collect form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Basic validation
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Generate and send OTP
        otp = random.randint(100000, 999999)
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp}.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        # Store user details and OTP in the session
        request.session['signup_data'] = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'password': password1,
        }
        request.session['otp'] = otp

        return redirect('verify_otp')

    return render(request, 'login_register.html')

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')
        signup_data = request.session.get('signup_data')  # Get the session data

        if not signup_data:
            messages.error(request, "Session data is missing or expired.")
            return redirect('signup')  # Redirect to signup if session data is missing

        if int(entered_otp) == session_otp:
            # Create the user after OTP verification
            user = User.objects.create_user(
                username=signup_data['username'],
                email=signup_data['email'],
                password=signup_data['password'],
                first_name=signup_data['first_name'],
                last_name=signup_data['last_name']
            )
            user.save()

            # Log the user in
            auth_login(request, user)

            # Clear session data if available
            if 'signup_data' in request.session:
                del request.session['signup_data']
            if 'otp' in request.session:
                del request.session['otp']

            messages.success(request, "Signup successful!")
            return redirect('2index')  # Redirect to a dashboard or home page
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('verify_otp')

    return render(request, 'main/verify_otp.html')
