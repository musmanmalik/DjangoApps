from django.contrib.auth.models import User
from django.contrib.messages.storage import session
from django.shortcuts import render
from django.http import HttpResponse;
from django.template import  loader
from random import randint
from django.shortcuts import render, get_object_or_404, redirect #for redirecting
from django.views.generic.edit import CreateView, DeleteView, UpdateView # For Creating Model View
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, Add_Song, loginForm
from django.core.mail import send_mail
from .forms import forms
from django.urls import resolvers,reverse_lazy #to redirect to other
from .models import Album, Song
from django.views import generic  # foR gENERIC views
from django.contrib.auth.decorators import login_required
# Create your views here.
# def index(request):
#     all_albums = Album.objects.all()
#     # #dynamic html generation
#     # html = ''
#     # for album in all_albums:
#     #     url = '/music/' + str(album.id) + '/'
#     #     html += '<a href="'+ url +'">'+album.album_title+'</a>'
#     #     html += '<br>'
#
#
#
#
#     #use of template instead of rendering html from view
#     template = loader.get_template('music/index.html')
#
#     #data we want to send on template view in the form of dictionary this can be sent like that {'all_albums': all_albums}
#     contex = {
#         'all_albums': all_albums
#     }
#    # return HttpResponse(template.render(contex, request));
#
#    #use of django shortcut
#     return render(request, 'music/index.html', contex )

####################################################

#generic view

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class Forgot_Password(generic.View):
    template_name = 'music/forgot_password.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        code = randint(0, 9999)
        request.session['code'] = code
        send_mail('Password Resetting', 'Your Password verification code is : '+str(code), 'm.usman@arbisoft.com', ['m.usman@arbisoft.com'], fail_silently=True)

        return render(request, 'music/verify_secrect_code.html')





class Verify(generic.View):

    template_name = 'music/verify_secrect_code.html'

    def get(self, request):
        print("usman")
        error = "Your code is not valid"
        return render(request, self.template_name,  {'error':error})

    def post(self, request):
        error = ""
        code = request.POST.get('s_code', "")
        if(code == request.session['code']):
             return render(request, self.template_name)
        else:
            error = "Your code is not valid"
            return render(request, self.template_name, {'error':error})




class ContactView(generic.ListView):

    template_name = 'music/contact.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    success_url = reverse_lazy('music:index')

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')



def index1(request):
    #return HttpResponse('<h1> Welcom to Music World</h>');
    return render(request,'music/index1.html')


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album,
                                                     'error_message': "You did not select a vaalig song"})

    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

def detail(request, album_id):
    if (request.session['login'] == ''):
        return render(request, 'music/login.html')
    #return HttpResponse('<h1>Details for album' + str(album_id) + '</h>');
    else:
    #for raising 404 page not found
        try:
            album = Album.objects.get(pk=album_id)
        except:
            raise Http404("Album does not exist")
        return render(request, 'music/detail.html', {'album': album})

        ########################################
        #Alternate of try except statement
        #album = get_object_or_404(Album, pk=album_id)
def logout_view(request):
    logout(request)
    request.session['login'] = ''
    form = loginForm
    return render(request, 'music/login.html', {'form':form})


class Add_Song(View):



    form_class = Add_Song
    template_name = 'music/add_song.html'


    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(None)

        form = self.form_class(request.POST)
        if form.is_valid():
            song = Song()
#            song.pk = form.cleaned_data['id']
            # cleaned(Normalized data
           # (int)


            song.album = Album.objects.get(pk=6)
            song.file_type = form.cleaned_data['file_type']
            song.song_title = form.cleaned_data['song_title']
           # song.song_id = (int)form.cleaned_data["album_id"]

            song.save()


        return render(request, self.template_name, {'form':form})






class LoginView(View):

    form_class =loginForm
    error = ""
    template_name = 'music/login.html'


    def get(self, request):
        request.session['login'] = ''
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
        # to tackle post request

    def post(self, request):
        request.session['login'] = ''
        form = self.form_class(request.POST)
        #
        # if form.is_valid():
        #     # cleaned(Normalized data
        #     print("Valid User")
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        #     print(username)
        #     # user authentication
        #     user = User()

        username = request.POST.get('username', "")
        password = request.POST.get('password', "")

        user = authenticate(username=username, password=password)
        if user is not None:

            request.session['login'] = username


            return render(request, 'music/index.html',{'login':request.session['login']})
        else:
            error = "User not Exist"
            return render(request, self.template_name, {'form': form,'error':error})




class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'


    # to display blank form #or to respond get request
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    #to tackle post request
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            #cleaned(Normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)

            user.save()


        # user authentication
            user = authenticate(username=username, password=password)
            if user is not None:
                request.session.login = username

                if user.is_active:
                    login(request, user)

                    return redirect('music:index')
        return render(request, self.template_name, {'form':form})
