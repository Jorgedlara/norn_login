from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fiels = [
            'username',
            'fisrt_name',
            'last_name',
            'email',
        ]

        labels = [
            'Nombre de usuario',
            'Nombre',
            'Apellidos',
            'Correo electronico',
        ]