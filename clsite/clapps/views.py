from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import BasicAuthentication

from .compling.generator import *
from .compling import main

# Create your views here.
class GenerateSentence(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    authentication_classes = [BasicAuthentication]

    eng = English()
    eng.initGrammar()

    gen = Generator(eng)

    def get(self, request):
        sent = self.gen.generateSentence()
        return JsonResponse({"sentence" : sent.sentStr})

class RunMain(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    authentication_classes = [BasicAuthentication]

    def get(self, request):
        main.main()
        return JsonResponse({"Response" : "ran main in django console"})
