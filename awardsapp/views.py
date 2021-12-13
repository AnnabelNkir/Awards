from django.db.models.deletion import PROTECT
from django.http.response import Http404
from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import CommentForm, ProfileForm, ProjectForm, SignupForm, Votes
from .models import Profile, Projects, Rates
from .serializer import ProfileSerializer, ProjectsSerializer
from .permissions import IsAdminOrReadOnly
from .forms import *
import datetime as dt
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.renderers import JSONRenderer


# Create your views here.

def home(request):
    date = dt.date.today()
    projects = Projects.objects.all()
    
    comment_form = CommentForm()
    return render(request, 'home.html',{"date": date,"projects":projects,"comment_form":comment_form})


class ProfileList(APIView):
    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)        

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProfileSerializer(merch)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProfileSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
            merch = self.get_merch(pk)
            merch.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




class ProjectList(APIView):
    def get(self, request, format=None):
        all_merch = Projects.objects.all()
        serializers = ProjectsSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectsSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return ProjectForm.objects.get(pk=pk)
        except PROTECT.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProjectsSerializer(merch)
        return Response(serializers.data)    

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProfileSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
            merch = self.get_merch(pk)
            merch.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@login_required(login_url='/signup')
def profile(request):
    profile = Profile.objects.filter(user=request.user)
    current_user = request.user
    posts = Projects.objects.filter(user=current_user)
    image_form = ProfileForm()
    if request.method == 'POST':
        image_form =ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if image_form.is_valid:
            image_form.save()
        else:
            image_form = ProfileForm()
            return render(request, 'profile.html', {"image_form": image_form,"posts":posts,"profile":profile})
    return render(request, 'profile.html', {"image_form": image_form,"posts":posts,"profile":profile})


def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('/')

    else:
        form = ProjectForm()
    return render(request, 'upload.html', {"form": form , "upload": upload})


def profiles(request,id):
    profile = Profile.objects.get(user_id=id)
    post=Projects.objects.filter(user_id=id)
   
                       
    return render(request,'pros.html',{"profile":profile,"post":post})

def search_results(request):    
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_projects = Projects.objects.filter(name=search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_projects": searched_projects})

    else:
        message = "Please search for a valid Project"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/signup')
def comment(request,id):
    upload = Projects.objects.get(id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.project = upload
            comment.save()
           
        return redirect('/')
    return redirect('/')

def rate_project(request,id):
        post = Projects.objects.get(id=id)
        likes = Rates.objects.filter(post=post)
        design = []
        usability = []
        creativity = []
        content = []
        for x in likes:
                design.append(x.design)
                usability.append(x.usability)
                creativity.append(x.creativity)
                content.append(x.content)
        des = (sum(usability)/len(usability))
        usa = (sum(creativity)/len(creativity))
        crea = (sum(design)/len(design))
        cont = (sum(content)/len(content))
        print (des)
        
        rate = Votes()
        if request.method == 'POST':

                rate = Votes(request.POST)
                if rate.is_valid():

                        design = rate.cleaned_data['design']
                        usability = rate.cleaned_data['usability']
                        content = rate.cleaned_data['content']
                        creativity = rate.cleaned_data['creativity']
                        rating = Rates(design=design,usability=usability,
                                        content=content,creativity=creativity,
                                        user=request.user,post=post)
                        rating.save()
                        return redirect('/')
        return render(request,'review.html',{"post":post,"des":des,"usa":usa,"cont":cont,"crea":crea, "rate":rate})



@login_required(login_url='/signup')
def review(request,id):
        comment_form = CommentForm()
        project = Projects.objects.get(id=id)
        post = Projects.objects.get(id=id)
        likes = Rates.objects.filter(post=post)
        design = []
        usability = []
        creativity = []
        content = []
        for x in likes:
                design.append(x.design)
                usability.append(x.usability)
                creativity.append(x.creativity)
                content.append(x.content)
        des = (sum(usability)*len(usability))
        usa = (sum(creativity)*len(creativity))
        crea = (sum(design)*len(design))
        cont = (sum(content)*len(content))
        # print (des)
        rate = Votes()
        if request.method == 'POST':

                rate = Votes(request.POST)
                if rate.is_valid():

                        design = rate.cleaned_data['design']
                        usability = rate.cleaned_data['usability']
                        content = rate.cleaned_data['content']
                        creativity = rate.cleaned_data['creativity']
                        rating = Rates(design=design,usability=usability,
                                        content=content,creativity=creativity,
                                        user=request.user,post=post)
                        rating.save()
                        return redirect('/')
        rate = Votes()
        profile = Profile.objects.filter(user_id=id)
                               
        return render(request,'review.html',{"profile":profile,"project":project, "rate":rate,"comment_form":comment_form,"des":des,"usa":usa,"cont":cont,"crea":crea})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            profile=Profile(user=user)
            profile.save()            
            return redirect('/accounts/login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})