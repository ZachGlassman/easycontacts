from django import forms

class PersonForm(forms.Form):
    def __init__(self, *args, **kwargs):
        person = args[0].pop('person')
        initial = kwargs.get('initial',{})
        initial['employer']= person.employer
        initial['email'] = person.email
        kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

        '''

        self.fields['employer'].initial = person.employer
        self.fields['email'].initial = person.email
        '''
        
        
    employer = forms.CharField(label='Employer',max_length=100)
    email = forms.CharField(label='Email', max_length=100)