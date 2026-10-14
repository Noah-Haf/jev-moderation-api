"""Policy models."""

from pydantic import BaseModel


class Policy(BaseModel):
    """Each policy defines what jev would classify as violating text.

    instructions: Generalised instructions for jev
    name: Name of policy
    truthy: What text must contain to be considered violating
    falsy: What text must contain to be considered non-violating.
    acceptange_range: At what truthiness content is considered violating.

    """

    instructions: str
    name: str
    truthy: str
    falsy: str
    acceptance_range: float
