from __future__ import unicode_literals
import random

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index



# Model for Quotes
# Quotes Folder, have function to get the quotes
class QuotesContainer(Page):

    subpage_types = ['home.Quotes']


    # function for getting quotes
    def get_quote(self):

        # ramdomly get quote from QuotesContainer's object's childs
        quote = random.choice(Quotes.objects.live())    
        return quote


# Quote model
class Quotes(Page):

    quote = models.CharField(max_length=511)
    author = models.CharField(max_length=511)

    content_panels = Page.content_panels + [
        FieldPanel('quote', classname="full"),
        FieldPanel('author', classname="full")
    ]

    parent_page_types = ['home.QuotesContainer']



# Model for HomePage
# HomePage model
class HomePage(Page):
    body = RichTextField(blank=True)
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('profile_image'),
    ]

    
    # HomePage template can use this attribute to refer QuoteContainer
    # It returns a list of "live" QuoteContainer Objects
    quote_container_object_list = QuotesContainer.objects.live()

    subpage_types = ['AboutmePage', 'ResumePage']
   



# Model for aboutme
# Aboutme folder, about catagory can be interest, hobbis
class AboutmeContainer(Page):
    # Title: interest, personality, hobbies...
    subpage_types = ['home.AboutElement']
    parent_page_types = ['home.AboutmePage']


# about element (physics, electronic, hiking....)
class AboutElement(Page):

    element = models.CharField(max_length=255)
    element_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel('element', classname="full"),
        ImageChooserPanel('element_image'),
    ]

    subpage_types = []
    parent_page_types = ['home.AboutmeContainer']


# About me model
class AboutmePage(Page):
    body = RichTextField(blank=True)
    aboutme_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('aboutme_image'),
    ]

    # get all the objects in AboutmeContainer eg. interest, hobbies, personality.....
    aboutme_container_object_list = AboutmeContainer.objects.live()
    quote_container_object_list = QuotesContainer.objects.live()

    subpage_types = ['AboutmeContainer']



# Model for Resume
class ResumePage(Page):

    subpage_types = ['Experience', 'Education']

    # get all Experience
    def get_experience(self):
        return Experience.objects.live()

    # get all Education
    def get_education(self):
        return Education.objects.live()

    # get quote that show at the bottom
    quote_container_object_list = QuotesContainer.objects.live()

#Experience
class Experience(Page):
    company = models.CharField(max_length=255)
    locations = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    details = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('company', classname="full"),
        FieldPanel('locations', classname="full"),
        FieldPanel('duration', classname="full"),
        FieldPanel('job_title', classname="full"),
        FieldPanel('details', classname="full"),
    ]
    parent_page_types = ['ResumePage']


# Education
class Education(Page):
    school = models.CharField(max_length=255)
    locations = models.CharField(max_length=255)
    program = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('school', classname="full"),
        FieldPanel('locations', classname="full"),
        FieldPanel('program', classname="full"),
        FieldPanel('duration', classname="full"),
    ]
    parent_page_types = ['ResumePage']