from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from .common_response import APIResponse


class CommonListModelMixin(ListModelMixin):

    def list(self, request, *args, **kwargs) -> APIResponse:
        result = super().list(request, *args, **kwargs)

        return APIResponse(result=result.data)
