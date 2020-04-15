from django.template.defaultfilters import slugify
import factory
import factory.fuzzy
#from ..models import Cheese


#"""NB THIS SHOULD BE DELETED AND SHOULD REFER TO MODELS.PY IN CHEESES"""
class Cheese(TimeStampedModel):
    name = models.CharField("Name of Cheese", max_length=255)
    slug = AutoSlugField("Cheese Address", unique = True, always_update = False, populate_from = "name")
    description = models.TextField("Decription", blank = True)

    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"
    #Should this line be indented?
    firmness = models.CharField("Firmness", max_length = 20, choices = Firmness.choices, default = Firmness.UNSPECIFIED)
    def __str__(self):
        return self.name




class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    firmness = factory.fuzzy.FuzzyChoice([x[0] for x in Cheese.Firmness.choices])
    class Meta:
        model = Cheese