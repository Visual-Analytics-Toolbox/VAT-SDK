import typing
from pathlib import Path
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import SyncClientWrapper
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)

class ModelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upload(
        self,
        file,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Examples
        --------
        client.model.upload('path/to/file/')
        """
        if Path(file).is_file():
            with open(file,mode="rb") as f:
                _response = self._client_wrapper.httpx_client.request(
                    "api/upload/model/",
                    method="POST",
                    files={"file":f},
                    request_options=request_options,
                    omit=OMIT,
                )
                try:
                    if 200 <= _response.status_code < 300:
                        return pydantic_v1.parse_obj_as(Event, _response.json())  # type: ignore
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(status_code=_response.status_code, body=_response.text)
                raise ApiError(status_code=_response.status_code, body=_response_json)
        else: 
            raise FileNotFoundError
   
