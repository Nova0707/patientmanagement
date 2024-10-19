from rest_framework.response import Response
def common_response(status_code,data=None,error=None,message=None):
    if not data:
        data={}
    if not error:
        error=""
    if not message:
        message=""
    return Response({"status_code":status_code,"data":data,"error":error,"message":message})