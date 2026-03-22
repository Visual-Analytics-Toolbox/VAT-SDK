import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..core.pagination import SyncPager
from ..types.image import Image,ImageOffsetPagination
# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ImageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Image:
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
            f"api/images/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Image, _response.json())  # type: ignore
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
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{jsonable_encoder(id)}/",
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
        log: typing.Optional[int] = OMIT,
        camera: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        frame_number: typing.Optional[int] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        blurredness_value: typing.Optional[int] = OMIT,
        brightness_value: typing.Optional[int] = OMIT,
        labelstudio_url: typing.Optional[str] = OMIT,
        validated: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Image:
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
            f"api/images/{jsonable_encoder(id)}/",
            method="PATCH",
            json={
                "log": log,
                "camera": camera,
                "type": type,
                "frame_number": frame_number,
                "image_url": image_url,
                "blurredness_value": blurredness_value,
                "brightness_value": brightness_value,
                "labelstudio_url": labelstudio_url,
                "validated": validated,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Image, _response.json())  # type: ignore
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
    ) -> SyncPager[Image]:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        """
        offset = offset if offset is not None else 0
        limit = limit if limit is not None else 100
        query_params = {k: v for k, v in filters.items()}
        query_params['limit'] = limit
        query_params['offset'] = offset
        _response = self._client_wrapper.httpx_client.request(
            "api/images/",
            method="GET",
            request_options=request_options,
            params=query_params,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = pydantic_v1.parse_obj_as(ImageOffsetPagination,_response.json())

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
        camera: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        frame: typing.Optional[int] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        blurredness_value: typing.Optional[int] = OMIT,
        brightness_value: typing.Optional[int] = OMIT,
        labelstudio_url: typing.Optional[str] = OMIT,
        validated: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Image:
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
            "api/images/",
            method="POST",
            json={
                "camera": camera,
                "type": type,
                "frame": frame,
                "image_url": image_url,
                "blurredness_value": blurredness_value,
                "brightness_value": brightness_value,
                "labelstudio_url": labelstudio_url,
                "validated": validated,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Image, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def bulk_create(
        self,
        *,
        data_list: typing.List[Image] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Image:
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
            "api/images/",
            method="POST",
            json=data_list,
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

    def bulk_update(
        self,
        *,
        data: typing.List[Image] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Image:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',
            api_key="YOUR_API_KEY",
        )
        """
        if data is not OMIT:
            payload = []
            for item in data:
                item_d = item.dict()
                if "frame" in item_d.keys():
                    item_d["frame_id"] = item_d["frame"]
                    del item_d["frame"]
                payload.append(item_d)
        else:
            payload = OMIT

        _response = self._client_wrapper.httpx_client.request(
            "api/image/update/",
            method="PATCH",
            json=payload,
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

    def get_image_count(
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
            "api/image-count/",
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
