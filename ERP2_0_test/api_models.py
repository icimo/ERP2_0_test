# coding=utf-8
import datetime
from django.utils.timezone import utc
from tastypie.authorization import Authorization
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from django.utils import simplejson
from django.core.serializers import json
from django.conf.urls import url
from ERP2_0_test import serializers
from ERP2_0_test.myModelResources import MyModelResource
from mysqldb_inspect import models as dbModels


class EntEquimentResource(MyModelResource):
    class Meta:
        queryset = dbModels.EntEquipment.objects.all()
        resource_name = 'EntEquipment'
        allFields = dbModels.EntEquipment._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    

class EntItemResource(MyModelResource):
    class Meta:
        queryset = dbModels.EntItem.objects.all()
        resource_name = 'EntItem'
        allFields = dbModels.EntItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    

class EntMachineResource(MyModelResource):
    class Meta:
        queryset = dbModels.EntMachine.objects.all()
        resource_name = 'EntMachine'
        allFields = dbModels.EntMachine._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    

class EntMaterialResource(MyModelResource):
    class Meta:
        queryset = dbModels.EntMaterial.objects.all()
        resource_name = 'EntMaterial'
        allFields = dbModels.EntMaterial._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()


class EntOrderResource(MyModelResource):
    class Meta:
        queryset = dbModels.EntOrder.objects.all()
        resource_name = 'EntOrder'
        allFields = dbModels.EntOrder._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    

class EntRelItemItemResource(MyModelResource):
    class Meta:
        queryset = dbModels.EntRelItemItem.objects.all()
        resource_name = 'EntRelItemItem'
        allFields = dbModels.EntRelItemItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    

class EntRelMathineItemResource(MyModelResource):
    class Meta:
        queryset = dbModels.EntRelMachineItem.objects.all()
        resource_name = 'EntRelMachineItem'
        allFields = dbModels.EntRelMachineItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    

class EntRelStorageItemResource(MyModelResource):
    class Meta:
        queryset = dbModels.EntRelStorageItem.objects.all()
        resource_name = 'EntRelStorageItem'
        allFields = dbModels.EntRelStorageItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    

class EntRelTechnologyItemEquipmentResource(MyModelResource):
    class Meta:
        queryset = dbModels.EntRelTechnologyItemEquipment.objects.all()
        resource_name = 'EntRelTechnologyItemEquipment'
        allFields = dbModels.EntRelTechnologyItemEquipment._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    

class EntSotrageResource(MyModelResource):
    class Meta:
        queryset = dbModels.EntStorage.objects.all()
        resource_name = 'EntStorage'
        allFields = dbModels.EntStorage._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    

class EntTechnologyResource(MyModelResource):
    class Meta:
        queryset = dbModels.EntTechnology.objects.all()
        resource_name = 'EntTechnology'
        allFields = dbModels.EntTechnology._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    

class TmpItemFullRelResource(MyModelResource):
    class Meta:
        queryset = dbModels.TmpItemFullRel.objects.all()
        resource_name = 'TmpItemFullRel'
        allFields = dbModels.TmpItemFullRel._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
