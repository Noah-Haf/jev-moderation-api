"""Handle text moderation."""

from fastapi import APIRouter
from typesafe_sdk import AsyncTypeSafeClient, Noul
from typesafe_sdk._core.response_types import NoulAnswer, SystemOneResponse

from models.policies import Policy
from models.text import TextModerationRequest, TextModerationResponse
from settings import Settings

textRouter = APIRouter()
configuration = Settings()


@textRouter.post(path="/moderate", response_model=TextModerationResponse)
async def moderate_text(body: TextModerationRequest):
    """Moderate text."""
    policy: Policy = configuration.policies[body.policyName]

    async with AsyncTypeSafeClient(api_key=configuration.TYPESAFE_API_KEY) as client:
        result: SystemOneResponse = await client.system_one(
            state=body.content,
            questions={
                "violating": Noul(
                    instructions=policy.instructions,
                    criteria={
                        "true": policy.truthy,
                        "false": policy.falsy,
                    },
                ),
            },
        )

        violatingResult: NoulAnswer = NoulAnswer.model_validate(
            result.answers.get("violating")
        )

        return TextModerationResponse(
            violating=(violatingResult.noul >= policy.acceptance_range),
            truthiness=violatingResult.noul,
        )
