from pydantic import Field

from ..base import SecureVuBaseModel

__all__ = ["CameraUiConfig"]


class CameraUiConfig(SecureVuBaseModel):
    order: int = Field(
        default=0,
        title="UI order",
        description="Numeric order used to sort the camera in the UI (default dashboard and lists); larger numbers appear later.",
    )
    dashboard: bool = Field(
        default=True,
        title="Show in UI",
        description="Toggle whether this camera is visible everywhere in the SecureVu UI. Disabling this will require manually editing the config to view this camera in the UI again.",
    )
