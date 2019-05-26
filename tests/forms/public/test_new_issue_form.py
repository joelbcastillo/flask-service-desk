# -*- coding: utf-8 -*-
"""Test the New Issue form."""

from servicedesk.public.forms import NewFeatureRequestForm


def test_validate_success(app):
    form = NewFeatureRequestForm(
        name="John Doe",
        email="test@email.com",
        subject="Test Issue",
        description="Test Description",
    )

    assert form.validate() is True


def test_validate_missing_name(app):
    """Missing Name."""
    form = NewFeatureRequestForm(
        email="test@email.com", subject="Test Issue", description="Test Description"
    )

    assert form.validate() is False
    assert "This field is required." in form.name.errors


def test_validate_missing_email(app):
    """Missing Email Address."""
    form = NewFeatureRequestForm(
        name="John Doe", subject="Test Issue", description="Test Description"
    )

    assert form.validate() is False
    assert "This field is required." in form.email.errors


def test_validate_missing_subject(app):
    """Missing Request Subject."""
    form = NewFeatureRequestForm(
        name="John Doe", email="test@email.com", description="Test Description"
    )

    assert form.validate() is False
    assert "This field is required." in form.subject.errors


def test_validate_missing_description(app):
    """Missing Request Description."""
    form = NewFeatureRequestForm(
        name="John Doe", email="test@email.com", subject="Test Issue"
    )

    assert form.validate() is False
    assert "This field is required." in form.description.errors
