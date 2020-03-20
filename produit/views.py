from django.shortcuts import render
from marketPlace.models import Produits
from django.db import transaction
from .forms import ParagraphErrorList,ProduitsForm


