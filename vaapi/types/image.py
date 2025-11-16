import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .cognition_frame import CognitionFrame

class Image(pydantic_v1.BaseModel):
    #: Id assigned by django
    id: typing.Optional[int] = None

    #: Foreign key to the frame the image belongs to
    # FIXME: how can use int for setting id on write and CognitionFrame on read???
    frame: typing.Optional[CognitionFrame] = None

    # Use an alias for the input/write case where you only pass an integer ID
    # The 'frame' field in the database will be set using this value
    frame_id_on_write: typing.Optional[int] = pydantic_v1.Field(None, alias='frame')

    #: camera
    camera: typing.Optional[str] = None

    #: type
    type: typing.Optional[str] = None

    #: image_url
    image_url: typing.Optional[str] = pydantic_v1.Field(default=None)

    #: blurredness_value
    blurredness_value: typing.Optional[int] = pydantic_v1.Field(default=None)

    @pydantic_v1.root_validator(pre=True)
    def handle_read_write_difference(cls, values):
        """
        Transforms the input data for the 'frame' field based on its type
        to handle both reading (full object) and writing (integer ID).
        """
        frame_data = values.get('frame')
        
        # 1. READ (Server sends the full object):
        # If 'frame_data' is a dictionary (the full CognitionFrame object), 
        # Pydantic will proceed to validate it against the 'CognitionFrame' model.
        if isinstance(frame_data, dict):
            return values
        
        # 2. WRITE (User sends an integer ID):
        # If 'frame_data' is an integer (the ID), we put it into a new 
        # field/alias that is only used for setting the ID on write.
        elif isinstance(frame_data, int):
            # Move the integer ID to the field/alias 'frame_id_on_write'
            values['frame'] = None # Clear the original frame field
            values['frame_id_on_write'] = frame_data
        
        # Handle the case where frame is None (e.g., optional field)
        elif frame_data is None:
            values['frame_id_on_write'] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        kwargs_with_defaults_exclude_none: typing.Any = {
            "by_alias": True,
            "exclude_none": True,
            **kwargs,
        }

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset),
            super().dict(**kwargs_with_defaults_exclude_none),
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}

class ImageOffsetPagination(pydantic_v1.BaseModel):
    """
    Offset/limit paginated response for tasks
    """
    results: typing.List[Image]
    count: int
    next: typing.Any
    previous: typing.Any
    
    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow