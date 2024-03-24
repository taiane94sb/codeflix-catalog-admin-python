import pytest

from unittest.mock import MagicMock

from uuid import UUID
import uuid

from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest, CreateCategoryResponse
from src.core.category.application.exceptions import InvalidCategoryData
from src.core.category.application.create_category import CategoryRepository
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.domain.category import Category


class TestInMemoryCategoryRepository:
    def test_can_save_Category(self):
        repository = InMemoryCategoryRepository()
        category = Category(
            name="Filme", 
            description="Categoria para filmes",
        )

        repository.save(category)

        assert len(repository.categories) == 1
        assert repository.categories[0] == category
    