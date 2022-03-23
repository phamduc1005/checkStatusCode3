# from django.shortcuts import render
# from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from .models import CheckUrl, UrlError
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CheckUrlSerializer


# def testUrlsFromSitemaps(request, nameTest):
#     def getUrlsFromSitemap(xmlUrl):
#         r = requests.get(xmlUrl)
#         xml = r.text
#         soup = BeautifulSoup(xml)

#         links = []
#         for link in soup.findAll('loc'):
#             linkStr = link.getText('', True)
#             links.append(linkStr)
#         return links


#     newTest = CheckUrl.objects.create(test = nameTest)

#     if newTest.test == 'pmp':
#         listUrls = ['https://pmp-testprep.com/post-sitemap.xml']
#     elif newTest.test == 'cna':
#         listUrls = ['https://cna-prep.com/post-sitemap.xml', 'https://cna-prep.com/page-sitemap.xml']
#     elif newTest.test == 'aws':
#         listUrls = ['https://aws-prep.com/post-sitemap.xml', 'https://aws-prep.com/page-sitemap.xml']
#     elif newTest.test == 'drivingtheory':
#         listUrls = ['https://drivingtheory-tests.com/post-sitemap.xml', 'https://drivingtheory-tests.com/page-sitemap.xml']
#     elif newTest.test == 'ged':
#         listUrls = ['https://ged-testprep.com/post-sitemap.xml', 'https://ged-testprep.com/page-sitemap.xml']
#     elif newTest.test == 'ptce':
#         listUrls = ['https://ptceprep.com/post-sitemap.xml', 'https://ptceprep.com/page-sitemap.xml']
#     elif newTest.test == 'realestate':
#         listUrls = ['https://realestate-prep.com/post-sitemap.xml', 'https://realestate-prep.com/page-sitemap.xml']
#     elif newTest.test == 'teas':
#         listUrls = ['https://teas-prep.com/post-sitemap.xml', 'https://teas-prep.com/page-sitemap.xml']
#     elif newTest.test == 'servsafe':
#         listUrls = ['https://servsafe-prep.com/post-sitemap.xml', 'https://servsafe-prep.com/page-sitemap.xml']

#     for xmlUrl in listUrls:
#         links = getUrlsFromSitemap(xmlUrl)
        
#         for link in links:
#             response = requests.get(link)
#             statusCode = response.status_code
            
#             if statusCode in range(200, 300):
#                 newTest.error.create(status = statusCode, url = link)

#     checkNewTest = UrlError.objects.filter(checkUrl = newTest.id)

#     data = {
#         'test': newTest.test,
#         'time': newTest.time,
#         'errors': list(checkNewTest.values('status', 'url'))
#     }

#     return JsonResponse(data)




# def allCheck(request, nameTest):

#     dataAll = []
#     checkNameTest = CheckUrl.objects.filter(test = nameTest).order_by('-time')
    
#     for element in checkNameTest:
#         getIdObject = element.id
#         checkObject = list(UrlError.objects.filter(checkUrl = getIdObject).values('status', 'url'))

#         data = {
#             'test': element.test,
#             'time' : element.time,
#             'errors' : checkObject
#         }

#         dataAll.append(data)

#     return JsonResponse(dataAll, safe=False)



@api_view(['GET'])
def checkLastUrlAllError(request):
    # nameTest = ['pmp', 'cna', 'aws', 'drivingtheory', 'ged', 'ptce', 'realestate', 'teas', 'servsafe']
    nameTest = ['pmp', 'servsafe']
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


    a = CheckUrlSerializer(data=request.data)
    if a.is_valid():
        a.save()
    
    b = a.data['id']
    c = CheckUrl.objects.get(id = b)

    if c.test == 'pmp':
        listUrls = ['https://pmp-testprep.com/post-sitemap.xml']
    elif c.test == 'cna':
        listUrls = ['https://cna-prep.com/post-sitemap.xml', 'https://cna-prep.com/page-sitemap.xml']
    elif c.test == 'aws':
        listUrls = ['https://aws-prep.com/post-sitemap.xml', 'https://aws-prep.com/page-sitemap.xml']
    elif c.test == 'drivingtheory':
        listUrls = ['https://drivingtheory-tests.com/post-sitemap.xml', 'https://drivingtheory-tests.com/page-sitemap.xml']
    elif c.test == 'ged':
        listUrls = ['https://ged-testprep.com/post-sitemap.xml', 'https://ged-testprep.com/page-sitemap.xml']
    elif c.test == 'ptce':
        listUrls = ['https://ptceprep.com/post-sitemap.xml', 'https://ptceprep.com/page-sitemap.xml']
    elif c.test == 'realestate':
        listUrls = ['https://realestate-prep.com/post-sitemap.xml', 'https://realestate-prep.com/page-sitemap.xml']
    elif c.test == 'teas':
        listUrls = ['https://teas-prep.com/post-sitemap.xml', 'https://teas-prep.com/page-sitemap.xml']
    elif c.test == 'servsafe':
        listUrls = ['https://servsafe-prep.com/post-sitemap.xml']
    # elif c.test == 'all':
    #     listUrls = []


    for xmlUrl in listUrls:
        links = getUrlsFromSitemap(xmlUrl)
        
        for link in links:
            response = requests.get(link)
            statusCode = response.status_code
            
            if statusCode in range(200, 300):
                c.error.create(status = statusCode, url = link)

    d = CheckUrl.objects.get(id = b)
    serializer = CheckUrlSerializer(d)

    return Response(serializer.data)