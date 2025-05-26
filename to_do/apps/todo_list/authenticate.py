from rest_framework_simplejwt.authentication import JWTAuthentication

class ValidarCookieJWT(JWTAuthentication):

    def authenticate(self, request):
        # Obtener el token de la cookie
        token = request.COOKIES.get('access')
        # De lo contrario devuelve la autenticacion
        if token is None:
            return None 
        # Autenticar el token
        validated_token = self.get_validated_token(token)
        return self.get_user(validated_token), validated_token