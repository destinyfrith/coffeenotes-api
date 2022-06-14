from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from coffeenotesapi.models import Entry


class EntryView(ViewSet):
    """Level up Entry view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single entry

        Returns:
            Response -- JSON serialized entry
        """

        try:
            entry = Entry.objects.get(pk=pk)
            serializer = EntrySerializer(entry)
            return Response(serializer.data)
        except Entry.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all entries

        Returns:
            Response -- JSON serialized list of entries
        """

        entries = Entry.objects.all()

        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized entry instance
        """
        # user = request.auth.user
        serializer = CreateEntrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(flavor_profile=request.data["flavor_profile"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an entry

        Returns:
            Response -- Empty body with 204 status code
        """
        entry = Entry.objects.get(pk=pk)
        serializer = CreateEntrySerializer(entry, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        entry = Entry.objects.get(pk=pk)
        entry.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class EntrySerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Entry
        fields = ('id', 'name', 'image', 'grind_setting',
                  'rating', 'notes', 'brewing_method', 'flavor_profile')
        depth = 2
        # The Meta class hold the configuration for the serializer.
        # We’re telling the serializer to use the Entry model and to include all fields


class CreateEntrySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Entry
        fields = ('id', 'name', 'image', 'grind_setting',
                  'rating', 'notes', 'brewing_method', 'flavor_profile')
        # Include all fields that the client will put in
