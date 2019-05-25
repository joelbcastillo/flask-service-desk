# -*- coding: utf-8 -*-
"""Unit tests for the User model."""
import datetime as dt

import pytest

from servicedesk.user.models import Role, User

from tests.factories import UserFactory

def test_get_by_id(db):
    """Get user by ID."""
    user = User("foo", "foo@bar.com")
    user.save()

    retrieved = User.get_by_id(user.id)
    assert retrieved == user

def test_created_at_defaults_to_datetime(db):
    """Test creation date."""
    user = User(username="foo", email="foo@bar.com")
    user.save()
    assert bool(user.created_at)
    assert isinstance(user.created_at, dt.datetime)

def test_password_is_nullable(db):
    """Test null password."""
    user = User(username="foo", email="foo@bar.com")
    user.save()
    assert user.password is None

def test_factory(db):
    """Test user factory."""
    user = UserFactory(password="myprecious")
    db.session.commit()
    assert bool(user.username)
    assert bool(user.email)
    assert bool(user.created_at)
    assert user.is_admin is False
    assert user.active is True
    assert user.check_password("myprecious")

def test_check_password(db):
    """Check password."""
    user = User.create(username="foo", email="foo@bar.com", password="foobarbaz123")
    assert user.check_password("foobarbaz123") is True
    assert user.check_password("barfoobaz") is False

def test_full_name(db):
    """User full name."""
    user = UserFactory(first_name="Foo", last_name="Bar")
    assert user.full_name == "Foo Bar"

def test_roles(db):
    """Add a role to a user."""
    role = Role(name="admin")
    role.save()
    user = UserFactory()
    user.roles.append(role)
    user.save()
    assert role in user.roles