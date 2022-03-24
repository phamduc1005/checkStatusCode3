# from django.shortcuts import render
# from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from .models import CheckUrl, UrlError
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CheckUrlSerializer


@api_view(['GET'])
def checkLastUrlAllError(request):
    nameTest = ['pmp', 'cna', 'aws', 'drivingtheory', 'ged', 'ptce', 'realestate', 'teas', 'servsafe']
    listobjects = []
    
    for element in nameTest:
        Checkurl = CheckUrl.objects.filter(test = element).last()
        listobjects.append(Checkurl)
    
    serializer = CheckUrlSerializer(listobjects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def checksAllUrlErrorOfAWeb(request, nameTest):
    checkurl = CheckUrl.objects.filter(test = nameTest).order_by('-time')
    serializer = CheckUrlSerializer(checkurl, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def checkOfAWebsite(request):
    def getUrlsFromSitemap(xmlUrl):
        r = requests.get(xmlUrl)
        xml = r.text
        soup = BeautifulSoup(xml)

        links = []
        for link in soup.findAll('loc'):
            linkStr = link.getText('', True)
            links.append(linkStr)
        return links


    addTest = CheckUrlSerializer(data=request.data)
    if addTest.is_valid():
        addTest.save()
    
    idTest = addTest.data['id']
    newTest = CheckUrl.objects.get(id = idTest)

    if newTest.test == 'pmp':
        listUrls = ['https://pmp-testprep.com/page-sitemap.xml']
    
    elif newTest.test == 'cna':
        listUrls = ['https://cna-prep.com/post-sitemap.xml', 'https://cna-prep.com/page-sitemap.xml']
    
    elif newTest.test == 'aws':
        listUrls = ['https://aws-prep.com/post-sitemap.xml', 'https://aws-prep.com/page-sitemap.xml']
    
    elif newTest.test == 'drivingtheory':
        listUrls = ['https://drivingtheory-tests.com/post-sitemap.xml', 'https://drivingtheory-tests.com/page-sitemap.xml']
    
    elif newTest.test == 'ged':
        listUrls = ['https://ged-testprep.com/post-sitemap.xml', 'https://ged-testprep.com/page-sitemap.xml']
    
    elif newTest.test == 'ptce':
        listUrls = ['https://ptceprep.com/post-sitemap.xml', 'https://ptceprep.com/page-sitemap.xml']
    
    elif newTest.test == 'realestate':
        listUrls = ['https://realestate-prep.com/post-sitemap.xml', 'https://realestate-prep.com/page-sitemap.xml']
    
    elif newTest.test == 'teas':
        listUrls = ['https://teas-prep.com/post-sitemap.xml', 'https://teas-prep.com/page-sitemap.xml']
    
    elif newTest.test == 'servsafe':
        listUrls = ['https://servsafe-prep.com/post-sitemap.xml', 'https://servsafe-prep.com/page-sitemap.xml']
    
    elif newTest.test == 'asvab':
        listUrls = ['https://asvab-prep.com/post-sitemap.xml', 'https://asvab-prep.com/page-sitemap.xml'] 


    for xmlUrl in listUrls:
        links = getUrlsFromSitemap(xmlUrl)
        
        for link in links:
            response = requests.get(link)
            statusCode = response.status_code
            
            if statusCode not in range(200, 300):
                newTest.error.create(status = statusCode, url = link)
  
    serializer = CheckUrlSerializer(newTest)

    return Response(serializer.data)