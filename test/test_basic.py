# Generated by CodiumAI
import argparse
import pytest
from unittest.mock import patch
from template_rocker.template_rocker import TemplateRocker


class TestTemplateRocker:
    # Instantiating template_rocker Extension and verifying the name attribute is set correctly
    def test_name_attribute_initialization(self):
        extension = TemplateRocker()
        assert extension.name == "template_rocker"

    def test_register_arguments(self):
        parser = argparse.ArgumentParser()
        TemplateRocker.register_arguments(parser)
        args = parser.parse_args([])
        assert "template_rocker" in vars(args)

    # Handling missing template files in get_snippet method
    def test_get_snippet_missing_template(self):
        extension = TemplateRocker()
        with patch("pkgutil.get_data", return_value=None):
            with pytest.raises(AttributeError):
                extension.get_snippet({})

    # Retrieving the default snippet using get_snippet method
    def test_retrieve_default_snippet(self):
        extension = TemplateRocker()
        snippet = extension.get_snippet(None)

        assert snippet is not None

    # Retrieving the user-specific snippet using get_user_snippet method
    def test_retrieve_user_specific_snippet(self):
        extension = TemplateRocker()
        snippet = extension.get_user_snippet(None)

        assert snippet is not None
