"""Project settings overview."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from models.policies import Policy


class Settings(BaseSettings):
    """Project settings."""

    TYPESAFE_API_KEY: str = Field(alias="TYPESAFE_API_KEY")

    policies: dict[str, Policy] = {
        "General": Policy(
            name="General",
            instructions="Is this message unsuitable for an audience aged 13+ under the policy below? Content must not be explicit",
            truthy="""A message is considered violating 
            
            if strong and swearing is used often and directly and if words are strong. 
            No graphic refrences to romance or relationships are 
            acceptable. 
            No Graphic violence, gore, or torture 
            No Detailed instructions for self-harm, drugs, weapons, or dangerous acts
            No Gambling mechanics presented as normal or encouraged
            No Content promoting harassment, doxxing, or grooming""",
            falsy="""A message is considered acceptable if 

            Mild language and occasional swearing, often limited to milder words
            Non-graphic references to romance, crushes, or relationships
            Discussion of difficult topics such as bullying, grief, or mental health, handled without graphic detail
            Mild violence in fictional or gaming contexts, without gore
            Non-explicit references to drugs or alcohol, without promotion or detailed use
            """,
            acceptance_range=0.8,
        )
    }
    model_config = SettingsConfigDict(env_file=".env")
