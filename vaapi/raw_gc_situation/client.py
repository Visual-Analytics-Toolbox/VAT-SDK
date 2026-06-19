import typing
import datetime as dt
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..types.raw_gc_situation import RawGCSituation

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawGCSituationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RawGCSituation:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        my_raw_gc_situation = client.raw_gc_situation.get(id=1)
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/situations/gc/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(RawGCSituation, _response.json())  # type: ignore
            _response_json = _response.json()

        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        client.raw_gc_situation.delete(id=1)
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/situations/gc/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: int,
        *,
        uuid: typing.Optional[str] = OMIT,
        json_data: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RawGCSituation:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        client.raw_gc_situation.update(id=1,...)
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/situations/gc/{jsonable_encoder(id)}/",
            method="PATCH",
            json={
                "uuid": uuid,
                "json_data": json_data,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(RawGCSituation, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self,
        *,
        request_options: typing.Optional[RequestOptions] = None,
        **filters: typing.Any,
    ) -> typing.List[RawGCSituation]:

        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        client.raw_gc_situation.get(<filter here>)
        """
        query_params = {k: v for k, v in filters.items() if v is not None}
        _response = self._client_wrapper.httpx_client.request(
            "api/situations/gc/",
            method="GET",
            request_options=request_options,
            params=query_params,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[RawGCSituation], _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        uuid,
        json_data,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RawGCSituation:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        client.raw_gc_situation.create(...)
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/situations/gc/",
            method="POST",
            json={
                "uuid": uuid,
                "json_data": json_data,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(RawGCSituation, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
