from rest_framework.views import APIView, Response, status
from django.forms.models import model_to_dict
from .models import Content
from .validator import ContentValidator


 

class ContentView(APIView):

    def get(self, request):
        contents = Content.objects.all()
        content_dict = [model_to_dict(content) for content in contents]
        return Response(content_dict)


    def post(self,request):
        
        validador = ContentValidator(**request.data)
        if not validador.is_valid():
            return Response(validador.errors, status.HTTP_400_BAD_REQUEST)

        content = Content.objects.create(**request.data)   
        contentdict = model_to_dict(content)
        return Response(contentdict, status.HTTP_201_CREATED)



class ContentDetailView(APIView):

   def get(self, request, content_id):
    try:
        content = Content.objects.get(id=content_id)
    except Content.DoesNotExist:
        return Response({"detail": "content not found"}, status.HTTP_404_NOT_FOUND)

    content_dict = model_to_dict(content)
    return Response(content_dict)


   
   def patch(self, request, content_id):
    try:
        content = Content.objects.get(id=content_id)
    except Content.DoesNotExist:
        return Response({"detail: Content not found", status.HTTP_404_NOT_FOUND})
    
    for key , value in request.data.items():
        setattr(content, key,value)

        content.save()   
        contentdict = model_to_dict(content)
        return Response(contentdict)

   
   def delete(self, request, content_id):
        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            return Response({"detail": "content not found"}, status.HTTP_404_NOT_FOUND)

        content.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    


class ContentfilterView(APIView):

    def get(self, request):
        title = request.query_params.get('title', None)
        content_obj = Content.objects.filter(title=title)
        content_dict = [model_to_dict(content) for content in content_obj]
        return Response(content_dict)

       
       




           

