from tastypie.authentication import ApiKeyAuthentication


class CustomAuthetication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True

        return super().is_authenticated(request, **kwargs)
