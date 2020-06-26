from sticker.models import Sticker, CourtForSticker
from rest_framework import serializers


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtForSticker
        fields = ['id', 'name']


class StickerSerializer(serializers.ModelSerializer):
    court = CourtSerializer(read_only=True)
    #court = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Sticker
        fields = ['id','court', 'device_name','invent_number','serial_number', 'production_date', 'malfunction', 'delivery_date']
        depth = 1


