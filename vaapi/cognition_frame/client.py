import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..types.cognition_frame import CognitionFrame, CognitionFrameOffsetPagination
from ..core.pagination import SyncPager

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CognitionFrameClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CognitionFrame:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/cognitionframe/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CognitionFrame, _response.json())  # type: ignore
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
        client.cognitionframe.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/cognitionframe/{jsonable_encoder(id)}/",
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
        log_id: typing.Optional[int] = OMIT,
        frame_number: typing.Optional[int] = OMIT,
        frame_time: typing.Optional[int] = OMIT,
        closest_motion_frame: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CognitionFrame:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        client.cognitionframe.update(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/cognitionframe/{jsonable_encoder(id)}/",
            method="PATCH",
            json={
                "log_id": log_id,
                "frame_number": frame_number,
                "frame_time": frame_time,
                "closest_motion_frame": closest_motion_frame,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CognitionFrame, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
        **filters: typing.Any,
    ) -> typing.List[CognitionFrame]:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        client.cognitionframe.list(
            id=1,
        )
        """
        offset = offset if offset is not None else 0
        limit = limit if limit is not None else 100
        query_params = {k: v for k, v in filters.items() if v is not None}
        query_params['limit'] = limit
        query_params['offset'] = offset
        _response = self._client_wrapper.httpx_client.request(
            "api/cognitionframe/",
            method="GET",
            request_options=request_options,
            params=query_params,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = pydantic_v1.parse_obj_as(CognitionFrameOffsetPagination,_response.json())
                _has_next = _parsed_response.next != None
                _get_next = lambda: self.list(
                    offset=offset + limit,  # Increase offset by limit to get the next page
                    limit=limit,
                    request_options=request_options,
                    **filters
                ) if _has_next else None
                
                _items = _parsed_response.results
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next,count=_parsed_response.count)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        log_id: typing.Optional[int] = OMIT,
        frame_number: typing.Optional[int] = OMIT,
        frame_time: typing.Optional[int] = OMIT,
        closest_motion_frame: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CognitionFrame:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        client.cognitionframe.create(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/cognitionframe/",
            method="POST",
            json={
                "log_id": log_id,
                "frame_number": frame_number,
                "frame_time": frame_time,
                "closest_motion_frame": closest_motion_frame,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CognitionFrame, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def bulk_create(
        self,
        *,
        frame_list: typing.List[CognitionFrame] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CognitionFrame:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        client.cognitionframe.bulk_create(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/cognitionframe/",
            method="POST",
            json=frame_list,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CognitionFrame, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def bulk_update(
        self,
        *,
        data: typing.List[CognitionFrame] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CognitionFrame:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        client.cognitionframe.bulk_update(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/cognitionframe/update/",
            method="PATCH",
            json=data,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return _response.json()
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_frame_count(
        self,
        request_options: typing.Optional[RequestOptions] = None,
        **filters: typing.Any,
    ) -> typing.Optional[int]:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        """
        query_params = {k: v for k, v in filters.items() if v is not None}
        _response = self._client_wrapper.httpx_client.request(
            "api/cognitionframe/count/",
            method="GET",
            request_options=request_options,
            params=query_params,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(
                    typing.Dict[str, typing.Any], _response.json()
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
