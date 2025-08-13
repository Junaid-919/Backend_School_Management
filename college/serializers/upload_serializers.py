from rest_framework import serializers
from ..models.uploads import Upload
from ..models.attachments import Attachment
from .attachments_serializers import AttachmentSerializer

class UploadSerializer(serializers.ModelSerializer):

    # ✅ Only used for reading uploaded files
    uploaded_files = AttachmentSerializer(many=True, read_only=True, source='attachments')

    class Meta:
        model = Upload
        # ✅ Include all model fields + uploaded files
        fields = [field.name for field in Upload._meta.fields] + ['uploaded_files']


    def create(self, validated_data):
        request = self.context.get('request')
        visit = Upload.objects.create(**validated_data)

        if request and hasattr(request, 'FILES'):
            files = request.FILES
            print("📁 Incoming files:", files)  # Debug print

            for key in files:
                print("📂 Checking file key:", key)
                if key.startswith('attachments[') and key.endswith('][file]'):
                    Attachment.objects.create(
                        upload=visit,
                        file=files[key]
                    )
                    print("✅ File saved:", files[key].name)

        return visit
    
    def update(self, instance, validated_data):
        request = self.context.get('request')

        # Update instance fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # ✅ Handle file uploads (optional: clear existing files if needed)
        if request and hasattr(request, 'FILES'):
            files = request.FILES
            print("📂 Updating visit files:", files)

            i = 0
            while f'attachments[{i}][file]' in files:
                Attachment.objects.create(
                    visit=instance,
                    file=files[f'attachments[{i}][file]']
                )
                i += 1

        return instance


