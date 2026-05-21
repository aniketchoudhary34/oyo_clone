from rest_framework import serializers
from .models import CustomUser
class RegisterSerializer(serializers.ModelSerializer):
#                                ↑
#                    ModelSerializer = 
#                    Model se automatically
#                    fields le leta hai!

    password = serializers.CharField(write_only=True)
#                                    ↑
#                    write_only = 
#                    Password sirf likhne ke liye
#                    Response mein nahi aayega!
#                    Security ke liye! 🔒

    class Meta:
        model = CustomUser    # Konsa model use karo
        fields = [
            'id',
            'username',
            'email',
            'password',  # write_only hai
            'role',
            'phone'
        ]

    def create(self, validated_data):
    #          ↑
    #   Jab serializer.save() call hoga
    #   Ye function chalega!
    
        user = CustomUser.objects.create_user(
        #                        ↑
        #              create_user = 
        #              Password automatically
        #              hash ho jaata hai! 🔒
            **validated_data
        #   ↑
        #   Matlab saara validated data
        #   pass kar do!
        )
        return user