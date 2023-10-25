from typing import Annotated

from fastapi import Depends

from src.config import YANDEX_WEATHER_API_TOKEN
from src.utils.uow import UnitOfWork
from src.api.weather import schemas
from src.utils.requests import Request
from src.api.api_source.service import ApiSourceService


class WeatherService:
    def __init__(self, api_source_service: Annotated[ApiSourceService, Depends(ApiSourceService)]):
        self.api_source_service = api_source_service

    @staticmethod
    async def add_region(new_region: schemas.AddRegion):
        async with UnitOfWork() as uow:
            return await uow.weather.add(new_region.model_dump())

    @staticmethod
    async def get_region_by_name(name: str) -> schemas.Region:
        async with UnitOfWork() as uow:
            return await uow.weather.get_region_by_name(name=name)

    async def get_current_weather(self, region: str, api_source: str) -> schemas.Region:
        async with UnitOfWork() as uow:
            region = await uow.weather.get_region_by_name(name=region)
        api_service = await self.api_source_service.get_by_name(name=api_source)

        params = {'lat': region.lat, 'lon': region.lon}
        headers = {api_service.header_key: YANDEX_WEATHER_API_TOKEN}
        result = await Request.get(url=api_service.url, params=params, headers=headers)

        return result.json()
