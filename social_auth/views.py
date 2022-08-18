from typing import FrozenSet
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import GoogleSocialAuthSerializer
from rest_framework import status

# Create your views here.


class GoogleSocialAuthView(GenericAPIView):
    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """

        POST with 'auth_token'

        Send an id token as from google to get user information

        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data)["auth_token"]
        return Response(data, status=status.HTTP_200_OK)





# class GetLeaveRequestListAPIView(APIView):
#     pagination_class = CustomPagination
#     def get(self, request):
#         try:
#             paginator = CustomPagination2()
#             leaves_type = request.data["leave_type"].upper()
#             if leaves_type != "":
#                 leave_requests = LeaveRequest.objects.filter(
#                     leave_type__leave_name=leaves_type
#                 )
#                 leaves_list = []
#                 for leave in leave_requests:
#                     leave_dict = {}
#                     leave_dict["employee"] = leave.employee.first_name + " " + leave.employee.last_name
#                     leave_dict["leave_type"] = leave.leave_type.leave_name
#                     leave_dict["start_date"] = leave.start_date
#                     leave_dict["end_date"] = leave.end_date
#                     leave_dict["status"] = leave.status
#                     leave_dict["total"] = int(leave.total)
#                     leave_dict["request_date"] = leave.request_date
#                     leave_dict["leave_request_id"] = leave.id
#                     leave_dict["employee_type"] = leave.employee.employee_type
#                     leaves_list.append(leave_dict)
#                 return Response(
#                 {
#                     "Message": "Leave request list",
#                     "leave_request_list": paginator.paginate_queryset(
#                         leaves_list, request
#                     ),
#                 },
#                 status=status.HTTP_200_OK)
#             else:
#                 leave_request = LeaveRequest.objects.all()
#                 leaves_list = []
#                 for leave in leave_request:
#                     leave_dict = {}
#                     leave_dict["employee"] = leave.employee.first_name
#                     leave_dict["leave_type"] = leave.leave_type.leave_name
#                     leave_dict["start_date"] = leave.start_date
#                     leave_dict["end_date"] = leave.end_date
#                     leave_dict["reason"] = leave.reason
#                     leave_dict["status"] = leave.status
#                     leave_dict["total"] = leave.total
#                     leave_dict["request_date"] = leave.request_date
#                     leave_dict["leave_request_id"] = leave.id
#                     leaves_list.append(leave_dict)
#                 return Response(
#                 {
#                     "Message": "Leave request list",
#                     "leave_request_list": paginator.paginate_queryset(
#                         leaves_list, request
#                     ),
#                 },
#                 status=status.HTTP_200_OK)
#         except LeaveType.DoesNotExist:
#             return Response(
#                 {"Error": "Leave type doesn't exist"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )




# class GetLeaveRequestListAPIView(generics.ListAPIView):
#     serializer_class = GetLeaveRequestSerializer
#     pagination_class = CustomPagination

#     def get(self, request):
#         try:
#             paginator = CustomPagination2()
#             leaves_type = request.data["leave_type"].upper()
#             if leaves_type != "":
#                 leave_requests = LeaveRequest.objects.filter(
#                     leave_type__leave_name=leaves_type
#                 )
#                 serializers = self.serializer_class(leave_requests, many=True)
#                 list_of_leave_requests = []
#                 for leave_request in serializers.data:
#                     list_of_leave_requests.append(leave_request)
#                 return Response(
#                     {
#                         "Message": "Leave request list",
#                         "leave_request_list": paginator.paginate_queryset(
#                             list_of_leave_requests, request
#                         ),
#                     },
#                     status=status.HTTP_200_OK,
#                 )
#             else:
#                 leave_requests = LeaveRequest.objects.all()
#                 serializers = self.serializer_class(leave_requests, many=True)
#                 list_of_leave_requests = []
#                 for leave_request in serializers.data:
#                     list_of_leave_requests.append(leave_request)
#                 return Response(
#                     {
#                         "Message": "Leave request list",
#                         "leave_request_list": paginator.paginate_queryset(
#                             list_of_leave_requests, request
#                         ),
#                     },
#                     status=status.HTTP_200_OK,
#                 )
#         except LeaveRequest.DoesNotExist:
#             return Response(
#                 {"Error": "Leave request does not exist"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
