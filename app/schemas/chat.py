from typing import Any
from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str
    reasoning_content: str | None = None
    tool_calls: list[Any] | None = None


class ChatRequest(BaseModel):
    message: str


class CompletionsChoices(BaseModel):
    index: int
    text: str | None = None
    logprobs: Any | None = None
    finish_reason: str
    message: ChatMessage | None = None


class CompletionsUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class CompletionsStats(BaseModel):
    tokens_per_second: float | None = None
    time_to_first_token: float | None = None
    generation_time: float | None = None
    stop_reason: str | None = None


class CompletionsModelInfo(BaseModel):
    arch: str
    quant: str
    format: str
    context_length: int


class CompletionsRuntime(BaseModel):
    name: str
    version: str
    supported_formats: list[str]


class Completions(BaseModel):
    id: str
    object: str
    created: int
    model: str

    choices: list[CompletionsChoices]

    usage: CompletionsUsage | None = None
    stats: CompletionsStats | None = None

    model_info: CompletionsModelInfo | None = None
    runtime: CompletionsRuntime | None = None

    system_fingerprint: str | None = None