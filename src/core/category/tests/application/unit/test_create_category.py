import pytest

from unittest.mock import MagicMock

from uuid import UUID
import uuid

from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest, CreateCategoryResponse
from src.core.category.application.exceptions import InvalidCategoryData
from src.core.category.application.create_category import CategoryRepository
from src.core.category.domain.category import Category


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)
        request = CreateCategoryRequest(
            name="Filme", 
            description="Categoria para filmes",
            is_active=True
        )

        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response, CreateCategoryResponse)
        assert isinstance(response.id, UUID)
        assert mock_repository.save.called is True
    
    def test_create_category_with_invalid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)

        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exc_info:
            use_case.execute(CreateCategoryRequest(name=""))

        assert exc_info.type is InvalidCategoryData
        assert str(exc_info.value) == "name cannot be empty"
    