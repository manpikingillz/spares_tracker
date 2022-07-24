from spares_tracker.files.models import File


def file_list():
    return File.objects.all()