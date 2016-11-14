#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals

from django.db import models


class _Msp(models.Model):
    fibre = models.ForeignKey('Fibre', models.DO_NOTHING, db_column='fibre')
    spectrum = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = '_msp'


class Action(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'action'


class Application(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'application'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'category'


class Changehistory(models.Model):
    schema_name = models.TextField()
    table_name = models.TextField()
    currentuser = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=25)
    original_data = models.TextField(blank=True, null=True)
    new_data = models.TextField(blank=True, null=True)
    row_id = models.IntegerField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changehistory'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class DyeAnalysis(models.Model):
    fibre = models.ForeignKey('Fibre', models.DO_NOTHING, db_column='fibre')
    dye = models.ForeignKey(Dye, models.DO_NOTHING, db_column='dye')
    quantity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dye_analysis'


class Fibre(models.Model):
    thread = models.ForeignKey('Thread', models.DO_NOTHING)
    fibre_type = models.ForeignKey('Microscopy', models.DO_NOTHING, db_column='fibre_type')

    class Meta:
        managed = False
        db_table = 'fibre'


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


class Image(models.Model):
    selection = models.ForeignKey('Selection', models.DO_NOTHING, db_column='selection')
    description = models.CharField(max_length=40)
    fullname = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    img = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'image'


class Item(models.Model):
    description = models.CharField(max_length=30)
    category = models.ForeignKey('Subsubcategory', models.DO_NOTHING, db_column='category')
    population = models.ForeignKey('Population', models.DO_NOTHING, db_column='population')

    class Meta:
        managed = True
        db_table = 'item'


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


class NumberOfFibres(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'number_of_fibres'


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


class Population(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'population'


class Selection(models.Model):
    description = models.CharField(max_length=30, blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, db_column='item')

    class Meta:
        managed = False
        db_table = 'selection'


class Structure(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'structure'


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