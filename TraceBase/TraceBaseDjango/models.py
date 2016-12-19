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

    def __str__(self):
        return self.description


class ColourIntensity(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'colour_intensity'
        verbose_name = 'kleur intensiteit'
        verbose_name_plural = 'kleur intensiteiten'

    def __str__(self):
        return self.description

#  Item models


class Population(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'population'
        verbose_name = 'herkomst object'
        verbose_name_plural = 'herkomsten object'

    def __str__(self):
        return self.description


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name = 'categorie'
        verbose_name_plural = 'categorieen'

    def __str__(self):
        return self.description


class Subcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, db_column='category')
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'subcategory'
        verbose_name = 'subcategorie'
        verbose_name_plural = 'subcategorieen'

    def __str__(self):
        return self.description


class Subsubcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Subcategory, on_delete=models.PROTECT, db_column='category')
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'subsubcategory'
        verbose_name = 'subsubcategorie'
        verbose_name_plural = 'subsubcategorieen'

    def __str__(self):
        return self.description


class Action(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'action'
        verbose_name = 'actie'
        verbose_name_plural = 'acties'

    def __str__(self):
        return self.description


class Item(models.Model):
    description = models.CharField(max_length=30)
    category = models.ForeignKey(Subsubcategory,  on_delete=models.PROTECT, db_column='category')
    population = models.ForeignKey(Population,  on_delete=models.PROTECT, db_column='population')

    class Meta:
        managed = False
        db_table = 'item'
        verbose_name = 'object'
        verbose_name_plural = 'objecten'

    def __str__(self):
        return self.description


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

    def __str__(self):
        return self.description

# Selection models


class Selection(models.Model):
    description = models.CharField(max_length=30, blank=True, null=True)
    item = models.ForeignKey(Item,  on_delete=models.PROTECT, db_column='item')

    class Meta:
        managed = False
        db_table = 'selection'
        verbose_name = 'selectie'
        verbose_name_plural = 'selecties'

    def __str__(self):
        return 'Naam object : ' + str(self.item) + '  Beschrijving selectie : ' + self.description


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

    def __str__(self):
        return 'Selectie : ' + self.selection + '  Description : ' + self.description

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

    def __str__(self):
        return self.description


class Origin(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'origin'
        verbose_name = 'herkomst textiel'
        verbose_name_plural = 'herkomsten textiel'

    def __str__(self):
        return self.description


class Pattern(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Textilecategory,  on_delete=models.PROTECT, db_column='category')
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pattern'
        verbose_name = 'textielpatroon'
        verbose_name_plural = 'textielpatronen'

    def __str__(self):
        return self.description


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

    def __str__(self):
        return self.description + '  Naam Selectie  ' + str(self.selection)


class Textilecolour(models.Model):
    description = models.CharField(max_length=30, blank=True, null=True)
    textile = models.ForeignKey(Textile,  on_delete=models.CASCADE, db_column='textile')
    spectrum = models.TextField  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'textileColour'
        verbose_name = 'textielkleur'
        verbose_name_plural = 'textielkleuren'

    def __str__(self):
        return self.description + '  Textiel : ' + str(self.textile)


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

    def __str__(self):
        return 'Textiel :  ' + str(self.sample) + '  Beschrijving : ' + self.description

# Thread models


class Application(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'application'
        verbose_name = 'applicatie'
        verbose_name_plural = 'applicaties'

    def __str__(self):
        return self.description


class Structure(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'structure'
        verbose_name = 'structuur'
        verbose_name_plural = 'structuren'

    def __str__(self):
        return self.description


class NumberOfFibres(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'number_of_fibres'
        verbose_name = 'aantal vezels'
        verbose_name_plural = 'aantal vezels'

    def __str__(self):
        return self.description


class Micdelust(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'micdelust'
        verbose_name = 'microscopie pigmentering'
        verbose_name_plural = 'microscopie pigmentering'

    def __str__(self):
        return self.description


class Micid(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'micid'
        verbose_name = 'microscopie identificatie'
        verbose_name_plural = 'microscopie identificatie'

    def __str__(self):
        return self.description


class Micpol(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'micpol'
        verbose_name = 'microscopie polarisatie'
        verbose_name_plural = 'microscopie polarisatie'

    def __str__(self):
        return self.description


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

    def __str__(self):
        return self.description


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
        verbose_name = 'microscopiemeting draad'
        verbose_name_plural = 'microscopiemetingen draad'

    def __str__(self):
        return 'Thread ID : ' + str(self.thread) + '  ID : ' + str(self.id)

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

    def __str__(self):
        return 'Applicatie : ' + self.application + '  Kleur : ' + self.colour + '  CI Nummer ' + str(self.ci_number)


class Fibre(models.Model):
    thread_id = models.ForeignKey(Thread,  on_delete=models.PROTECT, db_column='thread_id')
    fibre_type = models.ForeignKey(Microscopy,  on_delete=models.PROTECT, db_column='fibre_type')

    class Meta:
        managed = False
        db_table = 'fibre'
        verbose_name = 'vezel'
        verbose_name_plural = 'vezels'

    def __str__(self):
        return 'Naam draad : ' + str(self.thread_id) + '  ID vezel: ' + str(self.id)


class Msp(models.Model):
    fibre = models.ForeignKey(Fibre,  on_delete=models.CASCADE, db_column='fibre')
    spectrum = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = '_msp'
        verbose_name = 'msp vezel'
        verbose_name_plural = 'msp`s vezel'

    def __str__(self):
        return 'Naam vezel : ' + str(self.fibre)


class DyeAnalysis(models.Model):
    fibre = models.ForeignKey(Fibre,  on_delete=models.CASCADE, db_column='fibre')
    dye = models.ForeignKey(Dye,  on_delete=models.PROTECT, db_column='dye')
    quantity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dye_analysis'
        verbose_name = 'kleuranalyse vezel'
        verbose_name_plural = 'kleuranalyes vezel'

    def __str__(self):
        return 'Naam vezel : ' + str(self.fibre) + '  Kleurstof : ' + str(self.dye)


























