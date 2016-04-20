from data_reporter.models import Disease


def disease_menu_context_processor(request):
    return {
        'diseases': Disease.objects.all()
    }
