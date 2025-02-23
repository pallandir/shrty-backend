from pydantic import BaseModel, HttpUrl, Field
from datetime import date


class URL(BaseModel):
    url: HttpUrl
    suggested_shortened_url: str | None = Field(None)


class URLResponse(BaseModel):
    short_url: str
    mapped_url: HttpUrl
    visited: int = Field(0)
    last_visit: date | None = Field(None)
    last_update: date | None = Field(None)
