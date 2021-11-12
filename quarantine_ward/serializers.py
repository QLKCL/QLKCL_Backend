from rest_framework import serializers
from user_account.models import CustomUser
from .models import (
    QuarantineWard, QuarantineBuilding,
    QuarantineFloor, QuarantineRoom,
)

class BaseCustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['code', 'full_name', 'birthday']

class BaseQuarantineRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuarantineRoom
        fields = ['id', 'name']

class BaseQuarantineFloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuarantineFloor
        fields = ['id', 'name']

class BaseQuarantineBuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuarantineBuilding
        fields = ['id', 'name']

class BaseQuarantineWardSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuarantineWard
        fields = ['id', 'full_name']

class QuarantineWardWithBuildingSerializer(serializers.ModelSerializer):

    main_manager = BaseCustomUserSerializer(many=False) 

    class Meta:
        model = QuarantineWard
        fields = ['id', 'full_name', 'main_manager']

class FilterQuarantineWardSerializer(serializers.ModelSerializer):

    main_manager = BaseCustomUserSerializer(many=False)

    class Meta:
        model = QuarantineWard
        fields = ['id', 'main_manager', 'full_name','created_at', 'updated_at']

class FilterQuarantineBuildingSerializer(serializers.ModelSerializer):

    quarantine_ward = QuarantineWardWithBuildingSerializer(many=False)

    class Meta:
        model = QuarantineBuilding
        fields = ['id', 'name', 'quarantine_ward']

class FilterQuarantineFloorSerializer(serializers.ModelSerializer):

    quarantine_building = BaseQuarantineBuildingSerializer(many=False)

    class Meta:
        model = QuarantineFloor
        fields = ['id', 'name', 'quarantine_building']

class FilterQuarantineRoomSerializer(serializers.ModelSerializer):

    quarantine_floor = BaseQuarantineFloorSerializer(many=False)

    class Meta:
        model = QuarantineRoom
        fields = ['id', 'name', 'capacity', 'quarantine_floor']
