#   * Rearrange models' order DONE
#   * Make sure each model has one field with primary_key=True (Sequence excluded?)
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior. DONE
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table. DONE
# Feel free to rename the models, but don't rename db_table values or field names.
#   * Check for incorrect datatypes (Real > ?) DONE
# from __future__ import unicode_literals NOT NECESSARY YET

from django.db import models

# LUT models


class Colour(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'colour'
        verbose_name = 'kleur'
        verbose_name_plural = 'kleuren'


class ColourIntensity(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'colour_intensity'
        verbose_name = 'kleur intensiteit'
        verbose_name_plural = 'kleur intensiteiten'

#  Item models


class Population(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'population'
        verbose_name = 'herkomst object'
        verbose_name_plural = 'herkomsten object'

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name = 'categorie'
        verbose_name_plural = 'categorieen'


class Subcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, db_column='category')
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'subcategory'
        verbose_name = 'subcategorie'
        verbose_name_plural = 'subcategorieen'


class Subsubcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Subcategory, on_delete=models.PROTECT, db_column='category')
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'subsubcategory'
        verbose_name = 'subsubcategorie'
        verbose_name_plural = 'subsubcategorieen'


class Action(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'action'
        verbose_name = 'actie'
        verbose_name_plural = 'acties'

class Item(models.Model):
    description = models.CharField(max_length=30)
    category = models.ForeignKey(Subsubcategory,  on_delete=models.PROTECT, db_column='category')
    population = models.ForeignKey(Population,  on_delete=models.PROTECT, db_column='population')

    class Meta:
        managed = False
        db_table = 'item'
        verbose_name = 'object'
        verbose_name_plural = 'objecten'


class History(models.Model):
    description = models.CharField(max_length=30, blank=True, null=True)
    action = models.ForeignKey(Action,  on_delete=models.PROTECT, db_column='action')
    item = models.ForeignKey(Item,  on_delete=models.CASCADE, db_column='item')
    party = models.CharField(max_length=30)
    party_reference = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'history'
        verbose_name = 'geschiedenis objecten'
        verbose_name_plural = 'geschiedenis objecten'

# Selection models


class Selection(models.Model):
    description = models.CharField(max_length=30, blank=True, null=True)
    item = models.ForeignKey(Item,  on_delete=models.PROTECT, db_column='item')

    class Meta:
        managed = False
        db_table = 'selection'
        verbose_name = 'selectie'
        verbose_name_plural = 'selecties'

class Image(models.Model):
    selection = models.ForeignKey(Selection,  on_delete=models.CASCADE, db_column='selection')
    description = models.CharField(max_length=40)
    fullname = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    img = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'image'
        verbose_name = 'afbeelding'
        verbose_name_plural = 'afbeeldingen selecties'

# Textile models


class Textilecategory(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30)
    title_descr1 = models.CharField(max_length=30, blank=True, null=True)
    title_descr2 = models.CharField(max_length=30, blank=True, null=True)
    title_num1 = models.CharField(max_length=30, blank=True, null=True)
    title_num2 = models.CharField(max_length=30, blank=True, null=True)
    title_bool1 = models.CharField(max_length=30, blank=True, null=True)
    title_bool2 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'textileCategory'
        verbose_name = 'categorie textiel'
        verbose_name_plural = 'categorieen textiel'


class Origin(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'origin'
        verbose_name = 'herkomst textiel'
        verbose_name_plural = 'herkomsten textiel'


class Pattern(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Textilecategory,  on_delete=models.PROTECT, db_column='category')
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pattern'
        verbose_name = 'textielpatroon'
        verbose_name_plural = 'textielpatronen'


class Textile(models.Model):
    description = models.CharField(max_length=30)
    origin = models.ForeignKey(Origin,  on_delete=models.PROTECT, db_column='origin')
    colour = models.ForeignKey(Colour,  on_delete=models.PROTECT, db_column='colour')
    colour_intensity = models.ForeignKey(ColourIntensity, on_delete=models.PROTECT, db_column='colour_intensity')
    sampled = models.BooleanField(default=False)
    category = models.ForeignKey(Textilecategory, on_delete=models.PROTECT, db_column='category')
    selection = models.ForeignKey(Selection, on_delete=models.PROTECT, db_column='selection')

    class Meta:
        managed = False
        db_table = 'textile'
        verbose_name = 'textiel'
        verbose_name_plural = 'textielen'


class Textilecolour(models.Model):
    description = models.CharField(max_length=30, blank=True, null=True)
    textile = models.ForeignKey(Textile,  on_delete=models.CASCADE, db_column='textile')
    spectrum = models.TextField# This field type is a guess.

    class Meta:
        managed = False
        db_table = 'textileColour'
        verbose_name = 'textielkleur'
        verbose_name_plural = 'textielkleuren'

class Description(models.Model):
    sample = models.ForeignKey(Textile, on_delete=models.CASCADE, db_column='sample', related_name="sample")
    pattern = models.ForeignKey(Pattern,  on_delete=models.PROTECT, db_column='pattern', related_name="pattern")
    description = models.CharField(max_length=30, blank=True, null=True)
    num1 = models.FloatField(blank=True, null=True)
    num2 = models.FloatField(blank=True, null=True)
    bool1 = models.NullBooleanField()
    bool2 = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'description'
        verbose_name = 'textielbeschrijving'
        verbose_name_plural = 'textielbeschrijvingen'

# Thread models


class Application(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'application'
        verbose_name = 'applicatie'
        verbose_name_plural = 'applicaties'


class Structure(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'structure'
        verbose_name = 'structuur'
        verbose_name_plural = 'structuren'


class NumberOfFibres(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'number_of_fibres'
        verbose_name = 'aantal vezels'
        verbose_name_plural = 'aantal vezels'


class Micdelust(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'micdelust'
        verbose_name = 'microscopie pigmentering'
        verbose_name_plural = 'microscopie pigmentering'


class Micid(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'micid'
        verbose_name = 'microscopie identificatie'
        verbose_name_plural = 'microscopie identificatie'


class Micpol(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'micpol'
        verbose_name = 'microscopie polarisatie'
        verbose_name_plural = 'microscopie polarisatie'


class Thread(models.Model):
    textile = models.ForeignKey(Textile,  on_delete=models.PROTECT, db_column='textile')
    application = models.ForeignKey(Application,  on_delete=models.PROTECT, db_column='application')
    thickness = models.FloatField()
    structure = models.ForeignKey(Structure,  on_delete=models.PROTECT, db_column='structure')
    nfibres = models.ForeignKey(NumberOfFibres,  on_delete=models.PROTECT, db_column='nfibres')
    description = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thread'
        verbose_name = 'draad'
        verbose_name_plural = 'draden'


class Microscopy(models.Model):
    thread = models.ForeignKey(Thread,  on_delete=models.CASCADE, db_column='thread')
    type = models.CharField(max_length=40, blank=True, null=True)
    material = models.ForeignKey(Micid,  on_delete=models.PROTECT, db_column='material')
    percentage = models.FloatField()
    colour1 = models.ForeignKey(Colour,  on_delete=models.PROTECT, db_column='colour1', related_name="colour1")
    colour2 = models.ForeignKey(Colour,  on_delete=models.PROTECT, db_column='colour2', related_name="colour2")
    colour_intensity = models.ForeignKey(ColourIntensity,  on_delete=models.PROTECT, db_column='colour_intensity')
    delust = models.ForeignKey(Micdelust,  on_delete=models.DO_NOTHING, db_column='delust')
    pol = models.ForeignKey(Micpol,  on_delete=models.PROTECT, db_column='pol')
    flua_colour = models.ForeignKey(Colour,  on_delete=models.PROTECT, db_column='flua_colour', related_name="flua_colour")
    flua_intensity = models.ForeignKey(ColourIntensity,  on_delete=models.PROTECT, db_column='flua_intensity', related_name="sample")
    flud_colour = models.ForeignKey(Colour,  on_delete=models.PROTECT, db_column='flud_colour', related_name="flud_colour")
    flud_intensity = models.ForeignKey(ColourIntensity,  on_delete=models.PROTECT, db_column='flud_intensity', related_name="flud_intensity")
    flun_colour = models.ForeignKey(Colour,  on_delete=models.PROTECT, db_column='flun_colour', related_name="flun_colour")
    flun_intensity = models.ForeignKey(ColourIntensity,  on_delete=models.PROTECT, db_column='flun_intensity', related_name="flun_intensity")
    rarity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microscopy'
        verbose_name = 'microscopie draad'
        verbose_name_plural = 'microscopie draad'

# Fibre models


class Dye(models.Model):
    id = models.IntegerField(primary_key=True)
    application = models.CharField(max_length=20)
    colour = models.CharField(max_length=20)
    number = models.IntegerField()
    ci_name_add = models.CharField(max_length=25, blank=True, null=True)
    ci_number = models.IntegerField(blank=True, null=True)
    ci_number_add = models.CharField(max_length=25, blank=True, null=True)
    cas = models.CharField(max_length=25, blank=True, null=True)
    remark = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dye'
        verbose_name = 'kleurstof vezel'
        verbose_name_plural = 'kleurstoffen vezel'

class Fibre(models.Model):
    thread_id = models.ForeignKey(Thread,  on_delete=models.PROTECT, db_column='thread')
    fibre_type = models.ForeignKey(Microscopy,  on_delete=models.PROTECT, db_column='fibre_type')

    class Meta:
        managed = False
        db_table = 'fibre'
        verbose_name = 'vezel'
        verbose_name_plural = 'vezels'


class Msp(models.Model):
    fibre = models.ForeignKey(Fibre,  on_delete=models.CASCADE, db_column='fibre')
    spectrum = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = '_msp'
        verbose_name = 'msp vezel'
        verbose_name_plural = 'msp`s vezel'

class DyeAnalysis(models.Model):
    fibre = models.ForeignKey(Fibre,  on_delete=models.CASCADE, db_column='fibre')
    dye = models.ForeignKey(Dye,  on_delete=models.PROTECT, db_column='dye')
    quantity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dye_analysis'
        verbose_name = 'kleuranalyse vezel'
        verbose_name_plural = 'kleuranalyes vezel'


























