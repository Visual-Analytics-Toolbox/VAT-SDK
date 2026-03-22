import typing
import datetime as dt
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..types.game import Game

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GameClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Game:
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
            f"api/games/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Game, _response.json())  # type: ignore
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
            f"api/games/{jsonable_encoder(id)}/",
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
        event: typing.Optional[int] = OMIT,
        team1: typing.Optional[str] = OMIT,
        team2: typing.Optional[str] = OMIT,
        half: typing.Optional[str] = OMIT,
        is_testgame: typing.Optional[bool] = OMIT,
        referees: typing.Optional[str] = OMIT,
        field: typing.Optional[str] = OMIT,
        start_time: typing.Optional[dt.datetime] = OMIT,
        score: typing.Optional[str] = OMIT,
        game_folder: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        game_type: typing.Optional[str] = OMIT,
        division: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Game:
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
            f"api/games/{jsonable_encoder(id)}/",
            method="PATCH",
            json={
                "event": event,
                "team1": team1,
                "team2": team2,
                "half": half,
                "is_testgame": is_testgame,
                "referees": referees,
                "field": field,
                "start_time": start_time,
                "score": score,
                "game_folder": game_folder,
                "comment": comment,
                "game_type": game_type,
                "division": division,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Game, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self,
        *,
        request_options: typing.Optional[RequestOptions] = None,
        **filters: typing.Any,
    ) -> typing.List[Game]:
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
            "api/games/",
            method="GET",
            request_options=request_options,
            params=query_params,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[Game], _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        event: typing.Optional[int] = OMIT,
        team1: typing.Optional[str] = OMIT,
        team2: typing.Optional[str] = OMIT,
        half: typing.Optional[str] = OMIT,
        is_testgame: typing.Optional[bool] = OMIT,
        referees: typing.Optional[str] = OMIT,
        field: typing.Optional[str] = OMIT,
        start_time: typing.Optional[dt.datetime] = OMIT,
        score: typing.Optional[str] = OMIT,
        game_folder: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        game_type: typing.Optional[str] = OMIT,
        division: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Game:
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
            "api/games/",
            method="POST",
            json={
                "event": event,
                "team1": team1,
                "team2": team2,
                "half": half,
                "is_testgame": is_testgame,
                "referees": referees,
                "field": field,
                "start_time": start_time,
                "score": score,
                "game_folder": game_folder,
                "comment": comment,
                "game_type": game_type,
                "division": division,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Game, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
