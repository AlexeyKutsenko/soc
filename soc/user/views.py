import clearbit
from rest_auth.registration.views import RegisterView as BaseRegisterView
from rest_framework import status
from rest_framework.response import Response


class RegisterView(BaseRegisterView):

    def create(self, request, *args, **kwargs):
        """
        Default create function with clearbit enrichment
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        clearbit_enrich = clearbit.Enrichment.find(email=request.data.get('email'), stream=True)
        try:
            user.first_name = clearbit_enrich['person'].get('name').get('givenName')
            user.last_name = clearbit_enrich['person'].get('name').get('familyName')
            user.save()
        except TypeError:
            pass

        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)
