from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from attrs import define, field


@define(frozen=True)
class BaseRule(ABC):
    value: Any = field()

    def __str__(self) -> str:
        return self.to_text()

    @abstractmethod
    def to_text(self) -> str: ...