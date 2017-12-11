from .form import *
from .page import *
from .field import *
from .pagetype import *
from .inputtype import *
from .datatype import *
from .list import *

from django.contrib import admin

admin.autodiscover()

def home(request):
    return render(request, 'home.html')
