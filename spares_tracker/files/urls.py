from django.urls import path, include

from spares_tracker.files.apis import (
    FileStandardUploadApi,

    FileDirectUploadStartApi,
    FileDirectUploadFinishApi,
    FileDirectUploadLocalApi,
    FileListApi
)

# Depending on your case, you might want to exclude certain urls, based on the values of
# FILE_UPLOAD_STRATEGY and FILE_UPLOAD_STORAGE
# For the sake fo simplicity and to serve as an example project, we are including everything here.

urlpatterns = [
    path(
        "upload/",
        include(([
            path(
                "standard/",
                FileStandardUploadApi.as_view(),
                name="standard"
            ),
            path(
                "direct/",
                include(([
                    path(
                        "start/",
                        FileDirectUploadStartApi.as_view(),
                        name="start"
                    ),
                    path(
                        "finish/",
                        FileDirectUploadFinishApi.as_view(),
                        name="finish"
                    ),
                    path(
                        "local/<str:file_id>/",
                        FileDirectUploadLocalApi.as_view(),
                        name="local"
                    )
                ], "direct"))
            )
        ], "upload"))
    ),
    path('file_list/', FileListApi.as_view(), name='file_list')
]
