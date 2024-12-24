import base64

from rest_framework.response import Response as HTTPResponse
from rest_framework.views import APIView
from utils.sc_interface import SCInterface


class ScholeDeviceRegistrationView(APIView):

    def __init__(self):
        self.contract = SCInterface()

    def post(self, request):
        try:

            data = request.data
            body = {
                "iot_public_key": data["public_key"].encode("utf-8"),
            }
            for key, value in body.items():
                body[key] = base64.b64encode(value).decode()
            self.contract.sendInput(body)
            return HTTPResponse(status=200)
        except Exception as e:
            return HTTPResponse(status=500, data={"error": str(e)})
