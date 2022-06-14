"""View module for handling requests about brewing methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from coffeenotesapi.models import BrewingMethod


class BrewingMethodView(ViewSet):
    """Coffee Notes brewing method view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single brewing method

        Returns:
            Response -- JSON serialized brewing method
        """

        try:
            brewing_method = BrewingMethod.objects.get(pk=pk)
            serializer = BrewingMethodSerializer(brewing_method)
            return Response(serializer.data)
        except BrewingMethod.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all brewing methods

        Returns:
            Response -- JSON serialized list of brewing methods
        """

        brewing_methods = BrewingMethod.objects.all()

        brewing_method = request.query_params.get('method', None)
        if brewing_method is not None:
            entries = entries.filter(brewing_method_id=brewing_method)

        serializer = BrewingMethodSerializer(brewing_methods, many=True)
        return Response(serializer.data)


class BrewingMethodSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = BrewingMethod
        fields = ('id', 'type')
        # The Meta class hold the configuration for the serializer.
        # We’re telling the serializer to use the BrewingMethod model and to include the id and type fields.
