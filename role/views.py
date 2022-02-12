from django.db import models
from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.decorators import action
from .models import Role
from .serializers import RoleSerializer
from utils import exceptions, messages, validators
from utils.views import AbstractView

import datetime
import pytz
from form.models import Test
from form.serializers import TestSerializer
from user_account.models import CustomUser, Member
from utils.enums import CustomUserStatus, MemberQuarantinedStatus, TestType

# Create your views here.

class RoleAPI(AbstractView):

    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    @action(methods=['POST'], url_path='init', detail=False)
    def init_role(self, request):
        """Init some base role

        Args:
            None
        """

        try:
            user = request.user
            if not user.role.name == 'ADMINISTRATOR':
                raise exceptions.AuthenticationException()
            
            try:
                validators.ModelInstanceExistenceValidator.valid(
                    model_cls=Role,
                    query_expr=Q(name='SUPER_MANAGER'),
                )
            except:
                super_manager_role = Role(name='SUPER_MANAGER', created_by=user)
                super_manager_role.save()
                
            try:
                validators.ModelInstanceExistenceValidator.valid(
                    model_cls=Role,
                    query_expr=Q(name='MANAGER'),
                )
            except:
                manager_role = Role(name='MANAGER', created_by=user)
                manager_role.save()

            try:
                validators.ModelInstanceExistenceValidator.valid(
                    model_cls=Role,
                    query_expr=Q(name='STAFF'),
                )
            except:
                staff_role = Role(name='STAFF', created_by=user)
                staff_role.save()

            try:
                validators.ModelInstanceExistenceValidator.valid(
                    model_cls=Role,
                    query_expr=Q(name='MEMBER'),
                )
            except:
                member_role = Role(name='MEMBER', created_by=user)
                member_role.save()

            return self.response_handler.handle(data=messages.SUCCESS)
        except Exception as exception:
            return self.exception_handler.handle(exception)

    @csrf_exempt
    @action(methods=['POST'], url_path='filter', detail=False)
    def filter_role(self, request):
        """Get a list of roles

        Args:
            None
        """

        try:
            serializer = RoleSerializer(Role.objects.all(), many=True)

            return self.response_handler.handle(data=serializer.data)
        except Exception as exception:
            return self.exception_handler.handle(exception)

class DebugAPI(AbstractView):

    @csrf_exempt
    @action(methods=['POST'], url_path='debug', detail=False)
    def debug(self, request):
        """For debug

        Args:
            
        """

        try:
            # request_extractor = self.request_handler.handle(request)
            # receive_fields = request_extractor.data
            # vntz = pytz.timezone('Asia/Saigon')
            # time_now = datetime.datetime.now(vntz)
            # # print(time_now)
            # # new_time = time_now.astimezone(pytz.timezone('US/Eastern'))
            # # print(new_time)
            # # new_time = datetime.fromisoformat('2000-08-01T00:00:00.000')
            # time_1 = datetime.datetime.strptime('2000-08-01T00:00:00.123456Z', '%Y-%m-%dT%H:%M:%S.%f%z')
            # # time_2 = datetime.strptime('2000-08-01T00:01:00.123456Z', '%Y-%m-%dT%H:%M:%S.%f%z')
            # time_1 = time_1.astimezone(vntz)
            # # new_time = new_time.astimezone(vntz)
            # time_2 = datetime.datetime(time_1.year, time_1.month, time_1.day)
            # time_2 = time_2.astimezone(pytz.timezone('Asia/Saigon'))
            # time_3 = time_2 + datetime.timedelta(1)
            # # print(time_1)
            # # print(time_2)
            # # print(time_3)
            # # print(timezone.now())
            # this_user = CustomUser.objects.filter(status=CustomUserStatus.REFUSED, member_x_custom_user__quarantine_room__isnull=False)
            # print(list(this_user))
            # members = Member.objects.filter(quarantined_status=MemberQuarantinedStatus.COMPLETED, quarantine_room__isnull=True)
            # print('haha')
            # print(list(members))
            user = CustomUser.objects.get(id=20)
            tests_to_check = Test.objects.filter(user = user, type=TestType.RT_PCR).order_by('-created_at')[:3]
            print(list(tests_to_check))

            return self.response_handler.handle(data="fSuccess")
        except Exception as exception:
            return self.exception_handler.handle(exception)
