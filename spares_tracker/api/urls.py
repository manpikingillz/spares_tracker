from django.urls import path, include

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
]
