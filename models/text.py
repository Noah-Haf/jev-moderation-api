"""All pydatnic models relevant to text moderation route."""

from typing import Literal

from pydantic import BaseModel, Field


class TextModerationRequest(BaseModel):
    """Expected incoming text moderation request."""

    content: str = Field(max_length=500)
    policyName: Literal["General"]  # Must match policies reffered to in settings.py.


class TextModerationResponse(BaseModel):
    """Expected incoming text moderation request."""

    violating: bool
    truthiness: float
