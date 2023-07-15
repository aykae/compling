from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import BasicAuthentication

from .compling.generator import *

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
