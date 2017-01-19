from django.contrib import admin
from TraceBaseDjango.models import Thread
from TraceBaseDjango.models import Item
from TraceBaseDjango.models import History
from TraceBaseDjango.models import Selection
from TraceBaseDjango.models import Image
from TraceBaseDjango.models import Textile
from TraceBaseDjango.models import Textilecolour
from TraceBaseDjango.models import Description
from TraceBaseDjango.models import Microscopy
from TraceBaseDjango.models import Fibre
from TraceBaseDjango.models import Msp
from TraceBaseDjango.models import DyeAnalysis


admin.site.site_header = 'TraceBrace Administratie'

# Register your models here.


class HistoryInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = History
    extra = 1
    max_num = 1


class SelectionInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = Selection
    extra = 1
    max_num = 1


class ImageInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = Image
    extra = 1
    max_num = 1


class TextilecolourInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = Textilecolour
    extra = 1
    max_num = 1


class TextileInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = Textile
    extra = 1
    max_num = 1


class DescriptionInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = Description
    extra = 1
    max_num = 1


class ThreadInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = Thread
    extra = 1
    max_num = 1


class MicroscopyInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = Microscopy
    extra = 1
    max_num = 1


class FibreInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = Fibre
    extra = 1
    max_num = 1


class MspInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = Msp
    extra = 1
    max_num = 1


class DyeAnalysisInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = DyeAnalysis
    extra = 1
    max_num = 1

admin.site.register(Item)
admin.site.register(History)
admin.site.register(Selection)
admin.site.register(Image)
admin.site.register(Textilecolour)
admin.site.register(Textile)
admin.site.register(Description)
admin.site.register(Thread)
admin.site.register(Microscopy)
admin.site.register(Fibre)
admin.site.register(Msp)
admin.site.register(DyeAnalysis)
