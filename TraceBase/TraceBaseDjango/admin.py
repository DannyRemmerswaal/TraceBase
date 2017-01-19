from django.contrib import admin
from TraceBaseDjango.models import *

admin.site.site_header = 'TraceBrace Administratie'

# Register your models here.

admin.site.register(Colour)
admin.site.register(ColourIntensity)
admin.site.register(Population)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Subsubcategory)
admin.site.register(Action)
admin.site.register(Item)
admin.site.register(History)
admin.site.register(Selection)
admin.site.register(Image)
admin.site.register(Textilecategory)
admin.site.register(Textilecolour)
admin.site.register(Origin)
admin.site.register(Pattern)
admin.site.register(Textile)
admin.site.register(Description)
admin.site.register(Application)
admin.site.register(Structure)
admin.site.register(NumberOfFibres)
admin.site.register(Micdelust)
admin.site.register(Micid)
admin.site.register(Micpol)
admin.site.register(Thread)
admin.site.register(Microscopy)
admin.site.register(Dye)
admin.site.register(Fibre)
admin.site.register(Msp)
admin.site.register(DyeAnalysis)
