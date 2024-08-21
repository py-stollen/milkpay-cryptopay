from datetime import datetime

from pydantic import PlainSerializer
from typing_extensions import Annotated

DateTime = Annotated[
    datetime,
    PlainSerializer(
        func=datetime.isoformat,
        return_type=str,
        when_used="always",
    ),
]

StringList = Annotated[
    list[int | str],
    PlainSerializer(
        func=lambda x: ",".join(map(str, x)),
        return_type=str,
        when_used="always",
    ),
]
