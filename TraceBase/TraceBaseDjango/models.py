#   * Rearrange models' order DONE
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals NOT NECESSARY YET

from django.db import models

# LUT models

class Colour(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'colour'


class ColourIntensity(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'colour_intensity'

# Item models

class Population(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'population'


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'category'


class Subcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'subcategory'


class Subsubcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Subcategory, models.DO_NOTHING, db_column='category')
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'subsubcategory'


class Action(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'action'


class Item(models.Model):
    description = models.CharField(max_length=30)
    category = models.ForeignKey('Subsubcategory', models.DO_NOTHING, db_column='category')
    population = models.ForeignKey('Population', models.DO_NOTHING, db_column='population')

    class Meta:
        managed = True
        db_table = 'item'


class History(models.Model):
    description = models.CharField(max_length=30, blank=True, null=True)
    action = models.ForeignKey(Action, models.DO_NOTHING, db_column='action')
    item = models.ForeignKey('Item', models.DO_NOTHING, db_column='item')
    party = models.CharField(max_length=30)
    party_reference = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'history'

# Selection models

class Selection(models.Model):
    description = models.CharField(max_length=30, blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, db_column='item')

    class Meta:
        managed = False
        db_table = 'selection'


class Image(models.Model):
    selection = models.ForeignKey('Selection', models.DO_NOTHING, db_column='selection')
    description = models.CharField(max_length=40)
    fullname = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    img = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'image'

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


class Textilecolour(models.Model):
    description = models.CharField(max_length=30, blank=True, null=True)
    textile = models.ForeignKey(Textile, models.DO_NOTHING, db_column='textile')
    spectrum = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'textileColour'


class Origin(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'origin'


class Pattern(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey('Textilecategory', models.DO_NOTHING, db_column='category')
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pattern'


class Textile(models.Model):
    description = models.CharField(max_length=30)
    origin = models.ForeignKey(Origin, models.DO_NOTHING, db_column='origin')
    colour = models.ForeignKey(Colour, models.DO_NOTHING, db_column='colour')
    colour_intensity = models.ForeignKey(ColourIntensity, models.DO_NOTHING, db_column='colour_intensity')
    sampled = models.BooleanField()
    category = models.ForeignKey('Textilecategory', models.DO_NOTHING, db_column='category')
    selection = models.ForeignKey(Selection, models.DO_NOTHING, db_column='selection')

    class Meta:
        managed = False
        db_table = 'textile'


class Description(models.Model):
    sample = models.ForeignKey('Textile', models.DO_NOTHING, db_column='sample')
    pattern = models.ForeignKey('Pattern', models.DO_NOTHING, db_column='pattern')
    description = models.CharField(max_length=30, blank=True, null=True)
    num1 = models.FloatField(blank=True, null=True)
    num2 = models.FloatField(blank=True, null=True)
    bool1 = models.NullBooleanField()
    bool2 = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'description'

# Thread models

class Application(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'application'


class Structure(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'structure'


class NumberOfFibres(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'number_of_fibres'


class Micdelust(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'micdelust'


class Micid(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'micid'


class Micpol(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'micpol'


class Thread(models.Model):
    textile = models.ForeignKey(Textile, models.DO_NOTHING, db_column='textile')
    application = models.ForeignKey(Application, models.DO_NOTHING, db_column='application')
    thickness = models.FloatField()
    structure = models.ForeignKey(Structure, models.DO_NOTHING, db_column='structure')
    nfibres = models.ForeignKey(NumberOfFibres, models.DO_NOTHING, db_column='nfibres')
    description = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thread'


class Microscopy(models.Model):
    thread = models.ForeignKey('Thread', models.DO_NOTHING, db_column='thread')
    type = models.CharField(max_length=40, blank=True, null=True)
    material = models.ForeignKey(Micid, models.DO_NOTHING, db_column='material')
    percentage = models.FloatField()
    colour1 = models.ForeignKey(Colour, models.DO_NOTHING, db_column='colour1')
    colour2 = models.ForeignKey(Colour, models.DO_NOTHING, db_column='colour2')
    colour_intensity = models.ForeignKey(ColourIntensity, models.DO_NOTHING, db_column='colour_intensity')
    delust = models.ForeignKey(Micdelust, models.DO_NOTHING, db_column='delust')
    pol = models.ForeignKey(Micpol, models.DO_NOTHING, db_column='pol')
    flua_colour = models.ForeignKey(Colour, models.DO_NOTHING, db_column='flua_colour')
    flua_intensity = models.ForeignKey(ColourIntensity, models.DO_NOTHING, db_column='flua_intensity')
    flud_colour = models.ForeignKey(Colour, models.DO_NOTHING, db_column='flud_colour')
    flud_intensity = models.ForeignKey(ColourIntensity, models.DO_NOTHING, db_column='flud_intensity')
    flun_colour = models.ForeignKey(Colour, models.DO_NOTHING, db_column='flun_colour')
    flun_intensity = models.ForeignKey(ColourIntensity, models.DO_NOTHING, db_column='flun_intensity')
    rarity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microscopy'

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


class Fibre(models.Model):
    thread = models.ForeignKey('Thread', models.DO_NOTHING)
    fibre_type = models.ForeignKey('Microscopy', models.DO_NOTHING, db_column='fibre_type')

    class Meta:
        managed = False
        db_table = 'fibre'


class _Msp(models.Model):
    id = models.IntegerField(primary_key=True)
    fibre = models.ForeignKey('Fibre', models.DO_NOTHING, db_column='fibre')
    spectrum = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = '_msp'


class DyeAnalysis(models.Model):
    fibre = models.ForeignKey('Fibre', models.DO_NOTHING, db_column='fibre')
    dye = models.ForeignKey(Dye, models.DO_NOTHING, db_column='dye')
    quantity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dye_analysis'


























