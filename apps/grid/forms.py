from django.forms import ModelForm

from grid.models import  Element, Feature, Grid, GridHack

class GridForm(ModelForm):
    
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()    
    
    class Meta:
        model = Grid
        fields = ['title', 'slug', 'description']

class ElementForm(ModelForm):

    class Meta:
        model = Element
        fields = ['text',]

class FeatureForm(ModelForm):

    class Meta:
        model = Feature
        fields = ['title', 'description',]
        
class GridHackForm(ModelForm):

    class Meta:
        model = GridHack
        fields = ['hack']