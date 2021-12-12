from django.shortcuts import render


# Create your views here.
def index(request):
  
    return render(request, 'all-awards/index.html')

# @login_required(login_url='/accounts/login/')
# def upload_project(request):
#     if request.method == "POST":
#         form = PostProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.save()
#         return redirect('/')
#     else:
#         form = PostProjectForm()
#     return render(request, 'upload_project.html', {"form": form})