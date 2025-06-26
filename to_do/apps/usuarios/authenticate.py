from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response


# Middleware para validar el token de acceso en cada solicitud
class SesionJWT:

    def __init__(self, get_response):
        self.response = get_response
        pass

    # Recibir la respuesta de la peticion
    def __call__(self, request):
        cookie = request.COOKIES.get('access')
        refresh = request.COOKIES.get('refresh')
        try:
            token = AccessToken(cookie) # Validar si el token de acceso es valido de lo contrario disprara la excepcion
        except Exception as error:
            if 'expired' in str(error):
                nuevo_token = RefreshToken(refresh) # Generar un nuevo token con el refresh
                response = self.response(request)
                response.set_cookie(
                    key='access',
                    value=str(nuevo_token.access_token),
                    max_age=3600,
                    httponly=True,
                    secure=True,
                    samesite='Strict'
                )
                print(nuevo_token.access_token)
                return response

        return self.response(request)


        