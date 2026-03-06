from __future__ import annotations

from pydantic import BaseModel


class BattleRequest(BaseModel):
    prompt: str
    category: str = "general"
    model_a: str | None = None
    model_b: str | None = None


class VoteRequest(BaseModel):
    winner: str  # "a", "b", or "tie"
