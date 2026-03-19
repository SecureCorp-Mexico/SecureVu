from typing import Union

from pydantic import Field

from .base import SecureVuBaseModel

__all__ = ["IPv6Config", "ListenConfig", "NetworkingConfig"]


class IPv6Config(SecureVuBaseModel):
    enabled: bool = Field(
        default=False,
        title="Enable IPv6",
        description="Enable IPv6 support for SecureVu services (API and UI) where applicable.",
    )


class ListenConfig(SecureVuBaseModel):
    internal: Union[int, str] = Field(
        default=5000,
        title="Internal port",
        description="Internal listening port for SecureVu (default 5000).",
    )
    external: Union[int, str] = Field(
        default=8971,
        title="External port",
        description="External listening port for SecureVu (default 8971).",
    )


class NetworkingConfig(SecureVuBaseModel):
    ipv6: IPv6Config = Field(
        default_factory=IPv6Config,
        title="IPv6 configuration",
        description="IPv6-specific settings for SecureVu network services.",
    )
    listen: ListenConfig = Field(
        default_factory=ListenConfig,
        title="Listening ports configuration",
        description="Configuration for internal and external listening ports. This is for advanced users. For the majority of use cases it's recommended to change the ports section of your Docker compose file.",
    )
