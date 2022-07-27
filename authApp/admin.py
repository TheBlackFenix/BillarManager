from django.contrib import admin
from .models.user import User
from .models.tipoMesa import TipoMesa
from .models.tarifa import Tarifa
from .models.estado import Estado
from .models.cliente import Cliente
from .models.mesa import Mesa
from .models.tiempo import Tiempo

# Register your models here.
admin.site.register(User)
admin.site.register(TipoMesa)
admin.site.register(Tarifa)
admin.site.register(Estado)
admin.site.register(Cliente)
admin.site.register(Mesa)
admin.site.register(Tiempo)