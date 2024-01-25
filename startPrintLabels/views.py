from Tools.scripts.umarshal import Code
from django.shortcuts import render

from startPrintLabels.models import Codes


def index(request):
    all_codes = Codes.objects.all()
    # filter_codes = Codes.objects.filter(printed_out=True)
    # for code in all_codes:
    #     print(code)
    return render(request, 'index.html', context={'all_codes': all_codes})
