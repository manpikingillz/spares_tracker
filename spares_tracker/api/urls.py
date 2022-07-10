from django.urls import path, include

urlpatterns = [
    path(
        'auth/', include(('spares_tracker.authentication.urls', 'authentication'))
    ),
    path('users/', include(('spares_tracker.users.urls', 'users'))),
    path('errors/', include(('spares_tracker.errors.urls', 'errors'))),
    path('files/', include(('spares_tracker.files.urls', 'files'))),
]
