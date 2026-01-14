from typing import Self

from _pytest.config.findpaths import ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, Field, BaseModel
from enum import Enum
from typing import Dict



class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"

class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str

class TestData(BaseModel):
    image_png_file: FilePath

class BaseConfig(BaseModel):
    model_config = ConfigDict(
        extra='ignore',  # Игнорируем лишние поля
        validate_default=True
    )

class ViewportSettings(BaseConfig):
    mobile: Dict[str, int] = Field(default_factory=lambda: {"width": 375, "height": 812})
    tablet: Dict[str, int] = Field(default_factory=lambda: {"width": 768, "height": 1024})
    desktop: Dict[str, int] = Field(default_factory=lambda: {"width": 1920, "height": 1080})

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter=".",  # Указываем разделитель для вложенных переменных,
    )
    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    viewport_settings: ViewportSettings
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath
    browser_state_file: FilePath





    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        allure_results_dir = DirectoryPath("./allure-results")
        browser_state_file = FilePath("browser-stage_reg.json")
        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        allure_results_dir.mkdir(exist_ok=True)
        # Создаем файл состояния браузера, если его нет
        browser_state_file.touch(exist_ok=True)  # Если файл существует, то игнорируем ошибку

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file
        )

settings = Settings.initialize()