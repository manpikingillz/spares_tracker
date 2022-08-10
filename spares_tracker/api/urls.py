from django.urls import path, include
from django.conf import settings
from django.contrib import admin

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    path(
        'auth/', include(('spares_tracker.authentication.urls', 'authentication'))
    ),
    path('users/', include(('spares_tracker.users.urls', 'users'))),
    path('errors/', include(('spares_tracker.errors.urls', 'errors'))),
    path('files/', include(('spares_tracker.files.urls', 'files'))),
    path('vehicles/', include(('spares_tracker.vehicles.urls', 'vehicles'))),
    path('setup/', include(('spares_tracker.setup.urls', 'setup'))),
    path('suppliers/', include(('spares_tracker.suppliers.urls', 'suppliers'))),
    path('employees/', include(('spares_tracker.employee.urls', 'employees'))),
    path('spareparts/', include(('spares_tracker.spareparts.urls', 'spareparts'))),
    path('repairs/', include(('spares_tracker.repairs.urls', 'repairs'))),
]
