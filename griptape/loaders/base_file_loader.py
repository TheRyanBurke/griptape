from __future__ import annotations

from abc import ABC
from os import PathLike
from typing import TypeVar, Union

from attrs import Factory, define, field

from griptape.artifacts import BaseArtifact
from griptape.drivers import BaseFileManagerDriver, LocalFileManagerDriver
from griptape.loaders import BaseLoader

A = TypeVar("A", bound=BaseArtifact)


@define
class BaseFileLoader(BaseLoader[Union[str, PathLike], bytes, A], ABC):
    file_manager_driver: BaseFileManagerDriver = field(
        default=Factory(lambda: LocalFileManagerDriver()),
        kw_only=True,
    )
    encoding: str = field(default="utf-8", kw_only=True)

    def fetch(self, source: str | PathLike) -> bytes:
        data = self.file_manager_driver.load_file(str(source)).value
        if isinstance(data, str):
            return data.encode(self.encoding)
        else:
            return data
