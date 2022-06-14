"""View module for handling requests about brewing methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from coffeenotesapi.models import FlavorNote


class FlavorNoteView(ViewSet):
    """Coffee Notes flavors view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single flavors

        Returns:
            Response -- JSON serialized flavors
        """

        try:
            flavor_note = FlavorNote.objects.get(pk=pk)
            serializer = FlavorNoteSerializer(flavor_note)
            return Response(serializer.data)
        except FlavorNote.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all flavor notes

        Returns:
            Response -- JSON serialized list of flavor notes
        """

        flavor_notes = FlavorNote.objects.all()

        flavor_note = request.query_params.get('note', None)
        if flavor_note is not None:
            entries = entries.filter(flavor_note_id=flavor_note)

        serializer = FlavorNoteSerializer(flavor_notes, many=True)
        return Response(serializer.data)


class FlavorNoteSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = FlavorNote
        fields = ('id', 'name')
        # The Meta class hold the configuration for the serializer.
        # We’re telling the serializer to use the FlavorNote model and to include the id and name fields.
