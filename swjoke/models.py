import uuid
from django.db import models
# Create your models here.

class SithPlanets(models.Model):
    planet_name = models.CharField(max_length=40, unique = True)
    ASHAS_REE = 'Ashas Ree'
    ATHISS = 'Athiss'
    BEGEREN = 'Begeren'
    BOSTHIRDA = 'Bosthirda'
    CHHODOS = 'Ch\'hodos'
    DROMUND_FELS = 'Dromund Fels'
    DROMUND_IXIN = 'Dromund Ixin'
    DROMUND_KAAS = 'Dromund Kaas'
    DROMUND_KALAKAR = 'Dromund Kalakar'
    KALAKAR_SIX = 'Kalakar Six'
    DROMUND_TYNE = 'Dromund Tyne'
    JAGUADA = 'Jaguada'
    JAGUADAS_MOON = 'Jaguada\'s moon'
    KALSUNOR = 'Kalsunor'
    KHAR_DELBA = 'Khar Delba'
    KHAR_SHIAN = 'Khar Shian'
    KORRIBAN = 'Korriban'
    KORRIZ = 'Korriz'
    KRAYISS_TWO = 'Krayiss Two'
    NFOLGAI = 'Nfolgai'
    RHELG = 'Rhelg'
    ZIOST = 'Ziost'

    choices = [
        (ASHAS_REE, 'Ashas Ree'),
        (ATHISS, 'Athiss'),
        (BEGEREN, 'Begeren'),
        (BOSTHIRDA, 'Bosthirda'),
        (CHHODOS, 'Ch\'hodos'),
        (DROMUND_FELS, 'Dromund Fels'),
        (DROMUND_IXIN, 'Dromund Ixin'),
        (DROMUND_KAAS, 'Dromund Kaas'),
        (DROMUND_KALAKAR, 'Dromund Kalakar'),
        (KALAKAR_SIX, 'Kalakar Six'),
        (DROMUND_TYNE, 'Dromund Tyne'),
        (JAGUADA, 'Jaguada'),
        (JAGUADAS_MOON, 'Jaguada\'s moon'),
        (KALSUNOR, 'Kalsunor'),
        (KHAR_DELBA, 'Khar Delba'),
        (KHAR_SHIAN, 'Khar Shian'),
        (KORRIBAN, 'Korriban'),
        (KORRIZ, 'Korriz'),
        (KRAYISS_TWO, 'Krayiss Two'),
        (NFOLGAI, 'Nfolgai'),
        (RHELG, 'Rhelg'),
        (ZIOST, 'Ziost'),
    ]



class Recruit(models.Model):

    recruit_planet = models.CharField(
        max_length=20,
        choices=SithPlanets.choices,
        default=SithPlanets.ASHAS_REE,
    )
    recruit_name = models.CharField(max_length=100)
    recruit_age = models.PositiveIntegerField()
    recruit_email = models.EmailField(max_length=100)


class Sith(models.Model):

    sith_name = models.CharField(max_length=100)
    sith_planet = models.CharField(
        max_length=20,
        choices=SithPlanets.choices,
        default=SithPlanets.ASHAS_REE,
    )

class Test(models.Model):
    question_text = models.CharField(max_length=200)
    unique_sith_order_code = models.UUIDField(
        default = uuid.uuid4, 
        editable = False

    )
    
