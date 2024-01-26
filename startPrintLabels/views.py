from Tools.scripts.umarshal import Code
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from startPrintLabels.models import SKU
from startPrintLabels.serializers import SKU_Serializer


def index(request):
    skus = SKU.objects.all()
    # filter_codes = Codes.objects.filter(printed_out=True)
    # for code in all_codes:
    #     print(code)
    return render(request, 'index.html', context={'SKU': skus})


class SKU_View(ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = SKU_Serializer


def sku_app(request):
    skus = SKU.objects.all()
    # filter_codes = Codes.objects.filter(printed_out=True)
    # for code in all_codes:
    #     print(code)
    return render(request, 'main_app.html')