from django.forms import ModelForm
from .models import patient

# Create the form class.
class patientForm(ModelForm):
    class Meta:
        model = patient
        fields = [
            "name",
            "age",
            "gender",
            "mobile",
            "address",
            
            "medicine_detail",
            
            "amount",
            "next_visit"
        ]


# # Creating a form to add an article.
# form = patientForm()

# # Creating a form to change an existing article.
# patient = patient.objects.get(pk=1)
# form = patientForm(instance=patient)





