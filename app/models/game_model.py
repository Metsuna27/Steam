from pydantic import BaseModel, ConfigDict, model_validator


class GameAttribute(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    description: str


class GamePatch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str | None = None
    release_year: int | None = None
    is_free: bool | None = None

    @model_validator(mode="after")
    def validate_fields(self):
        for field in self.model_fields_set:
            if getattr(self, field) is None:
                raise ValueError(f"Field '{field}' cannot be null")
        return self


class GameReplace(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    required_age: int = 0
    is_free: bool
    description: str | None = None
    image: str | None = None
    website: str | None = None
    developers: list[str] = []
    publishers: list[str] = []
    platforms: list[str] = []
    metacritic_score: int | None = None
    categories: list[GameAttribute] = []
    genres: list[GameAttribute] = []
    recommendations: int | None = None
    release_date: str | None = None
    release_year: int | None = None

