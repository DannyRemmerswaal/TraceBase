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
    """History to be added when adding an item"""
    model = History
    extra = 0


class SelectionInline(admin.StackedInline):
    """Selection to be added when adding an item"""
    model = Selection
    extra = 0


class ImageInline(admin.StackedInline):
    """Image to be added when adding a selection"""
    model = Image
    extra = 0


class TextilecolourInline(admin.StackedInline):
    """Textile colour to be added when adding a textile"""
    model = Textilecolour
    extra = 0


class TextileInline(admin.StackedInline):
    """Textile to be added when adding a selection"""
    model = Textile
    extra = 0


class TextileDescriptionInline(admin.StackedInline):
    """Description to be added when adding a textile"""
    model = Description
    extra = 0


class ThreadInline(admin.StackedInline):
    """Thread to be added when adding an textile"""
    model = Thread
    extra = 0


class MicroscopyInline(admin.StackedInline):
    """Microscopy to be added when adding a thread"""
    model = Microscopy
    extra = 0

class FibreInline(admin.StackedInline):
    """Fibre to be added when adding microscopy"""
    model = Fibre
    extra = 0


class MspInline(admin.StackedInline):
    """Msp analysis to be added when adding a fibre"""
    model = Msp
    extra = 0


class DyeAnalysisInline(admin.StackedInline):
    """Dye analysis to be added when adding a fibre"""
    model = DyeAnalysis
    extra = 0


class ItemAdmin(admin.ModelAdmin):

    inlines = [HistoryInline, SelectionInline]


class SelectionAdmin(admin.ModelAdmin):

    inlines = [ImageInline, TextileInline]


class TextileAdmin(admin.ModelAdmin):

    inlines = [TextilecolourInline, TextileDescriptionInline, ThreadInline]


class ThreadAdmin(admin.ModelAdmin):

    inlines = [MicroscopyInline, FibreInline]


class FibreAdmin(admin.ModelAdmin):

    inlines = [MspInline, DyeAnalysisInline]



admin.site.register(Item, ItemAdmin)
admin.site.register(History)
admin.site.register(Selection, SelectionAdmin)
admin.site.register(Image)
admin.site.register(Textilecolour)
admin.site.register(Textile, TextileAdmin)
admin.site.register(Description)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Microscopy)
admin.site.register(Fibre, FibreAdmin)
admin.site.register(Msp)
admin.site.register(DyeAnalysis)
