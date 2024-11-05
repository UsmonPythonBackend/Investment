from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import ServiceSerializer, ClientSerializer, AdvisersSerializer, FeaturesSerializer, FAQsSerializer, \
    CommentsSerializer
from .models import Services, Clients, Comments, Features, FAQs, Advisers


class ServiseViewSet(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET', ])
    def seen(self, request, *args, **kwargs):
        service = self.get_object()
        service.seen += 1
        service.save()

        return Response(data={"korilgan": service.seen})


class ClientViewSet(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

    @action(detail=True, methods=['GET', ])
    def clientseen(self, request, *args, **kwargs):
        client = self.get_object()
        client.clientseen += 1
        client.save()

        return Response(data={"korilgan": client.clientseen})


class AdvisersViewSet(ModelViewSet):
    queryset = Advisers.objects.all()
    serializer_class = AdvisersSerializer

    @action(detail=True, methods=['GET', ])
    def advisersseen(self, request, *args, **kwargs):
        advisers = self.get_object()
        advisers.advisersseen += 1
        advisers.save()

        return Response(data={"korilgan": advisers.advisersseen})


class FeaturesViewSet(ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer

    @action(detail=True, methods=['GET', ])
    def featureseen(self, request, *args, **kwargs):
        feature = self.get_object()
        feature.featureseen += 1
        feature.save()

        return Response(data={"korilgan": feature.featureseen})


class FAQsViewSet(ModelViewSet):
    queryset = FAQs.objects.all()
    serializer_class = FAQsSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    @action(detail=True, methods=['GET', ])
    def commentseen(self, request, *args, **kwargs):
        comment = self.get_object()
        comment.commentseen += 1
        comment.save()

        return Response(data={"korilgan": comment.commentseen})
