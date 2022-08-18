from rest_framework import serializers
from . import google
from .register import register_social_user
import os
from rest_framework.exceptions import AuthenticationFailed


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data["sub"]
        except:
            raise serializers.ValidationError(
                "The token is invalid or expired. Please login again."
            )
        GOOGLE_CLIENT_ID = (
            "575337819904-n3g4sod5jqe25j8jepnj7rpe70ci5q1g.apps.googleusercontent.com"
        )
        if user_data["aud"] != GOOGLE_CLIENT_ID:
            raise AuthenticationFailed("oops, Who are you ?")

        user_id = user_data["sub"]
        email = user_data["email"]
        name = user_data["name"]
        provider = "google"

        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name
        )


# class GetLeaveRequestSerializer(serializers.ModelSerializer):
#     employee_type = serializers.SerializerMethodField()
#     leave_name = serializers.SerializerMethodField()   
#     employee_name = serializers.SerializerMethodField()

#     class Meta:
#         model = LeaveRequest
#         fields = [
#             "id",
#             "total",
#             "start_date",
#             "end_date",
#             "status",
#             "employee_type",
#             "leave_name",
#             "employee_name"
#         ]
# #     def validate(self, attrs):
# #         leave_type = attrs.get("leave_type","")

# #         if leave_type == "":
# #             raise serializers.ValidationError("Leave type cannot be empty")
        
# #         return attrs

#     def get_employee_type(self,obj):
#         return obj.employee.employee_type

#     def get_leave_name(self,obj):
#         return obj.leave_type.leave_name

#     def get_employee_name(self,obj):
#         return obj.employee.first_name + " "+ obj.employee.last_name
        





