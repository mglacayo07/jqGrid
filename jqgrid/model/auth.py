# -*- coding: utf-8 -*-
"""
Auth* related model.

This is where the models used by the authentication stack are defined.

It's perfectly fine to re-use this definition in the jqGrid application,
though.

"""
import os
from datetime import datetime
from hashlib import sha256
from sqlalchemy import exc

__all__ = ['User', 'Group', 'Permission']

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import relation, synonym

from jqgrid.model import DeclarativeBase, metadata, DBSession


# This is the association table for the many-to-many relationship between
# groups and permissions.
group_permission_table = Table('tg_group_permission', metadata,
                               Column('group_id', Integer,
                                      ForeignKey('tg_group.group_id',
                                                 onupdate="CASCADE",
                                                 ondelete="CASCADE"),
                                      primary_key=True),
                               Column('permission_id', Integer,
                                      ForeignKey('tg_permission.permission_id',
                                                 onupdate="CASCADE",
                                                 ondelete="CASCADE"),
                                      primary_key=True))


# This is the association table for the many-to-many relationship between
# groups and members - this is, the memberships.
user_group_table = Table('tg_user_group', metadata,
                         Column('user_id', Integer,
                                ForeignKey('tg_user.user_id',
                                           onupdate="CASCADE",
                                           ondelete="CASCADE"),
                                primary_key=True),
                         Column('group_id', Integer,
                                ForeignKey('tg_group.group_id',
                                           onupdate="CASCADE",
                                           ondelete="CASCADE"),
                                primary_key=True))


class Group(DeclarativeBase):
    """
    Group definition

    Only the ``group_name`` column is required.

    """

    __tablename__ = 'tg_group'

    group_id = Column(Integer, autoincrement=True, primary_key=True)
    group_name = Column(Unicode(16), unique=True, nullable=False)
    display_name = Column(Unicode(255))
    created = Column(DateTime, default=datetime.now)
    users = relation('User', secondary=user_group_table, backref='groups')

    def __repr__(self):
        return '<Group: name=%s>' % repr(self.group_name)

    def __unicode__(self):
        return self.group_name


class User(DeclarativeBase):
    """
    User definition.

    This is the loadingData definition used by :mod:`repoze.who`, which requires at
    least the ``user_name`` column.

    """
    __tablename__ = 'tg_user'

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    user_name = Column(Unicode(16), unique=True, nullable=False)
    email_address = Column(Unicode(255), unique=True, nullable=False)
    display_name = Column(Unicode(255))
    _password = Column('password', Unicode(128))
    created = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return '<User: name=%s, email=%s, display=%s>' % (
            repr(self.user_name),
            repr(self.email_address),
            repr(self.display_name)
        )

    def __unicode__(self):
        return self.display_name or self.user_name


    @classmethod
    def add(cls,user_name,email_address,display_name,password):
        try:
            handler = cls()
            handler.user_name = user_name
            handler.email_address = email_address
            handler.display_name = display_name
            handler.password = password
            DBSession.add(handler)
            DBSession.flush()
            return "ok"
        except exc.SQLAlchemyError:
            DBSession.rollback()
            handler = DBSession.query(cls).filter_by(user_name = user_name).all()
            if str(handler) != "[]":
                return "Username already used"
            handler = DBSession.query(cls).filter_by(email_address=email_address).all()
            if str(handler) != "[]":
                return "Email already used"
            return "not ok"

    @classmethod
    def update(cls,user_id,user_name,email_address,display_name,password):
        print("UPDATE")
        handler = DBSession.query(cls).filter_by(user_id=user_id).first()
        if handler != None:
            return "Username doesn't exist"

        handler.user_name = user_name
        print(user_name)
        handler.email_address = email_address
        handler.display_name = display_name
        if password != "" :
            handler.password = password
        DBSession.flush()
        return "ok"

    @classmethod
    def delete(cls,user_id):

        print("ENTRE")
        handler = DBSession.query(cls).filter_by(user_id=user_id).first()
        if handler == None:
            return "Username doesn't exist"

        if handler != None:
            DBSession.delete(handler)
            print("BORRE")
        DBSession.flush()
        return "ok"

    @property
    def permissions(self):
        """Return a set with all permissions granted to the loadingData."""
        perms = set()
        for g in self.groups:
            perms = perms | set(g.permissions)
        return perms

    @classmethod
    def by_email_address(cls, email):
        """Return the loadingData object whose email address is ``email``."""
        return DBSession.query(cls).filter_by(email_address=email).first()

    @classmethod
    def by_user_name(cls, username):
        """Return the loadingData object whose loadingData name is ``username``."""
        return DBSession.query(cls).filter_by(user_name=username).first()

    @classmethod
    def _hash_password(cls, password):
        salt = sha256()
        salt.update(os.urandom(60))
        salt = salt.hexdigest()

        hash = sha256()
        # Make sure password is a str because we cannot hash unicode objects
        hash.update((password + salt).encode('utf-8'))
        hash = hash.hexdigest()

        password = salt + hash


        return password

    def _set_password(self, password):
        """Hash ``password`` on the fly and store its hashed version."""
        self._password = self._hash_password(password)

    def _get_password(self):
        """Return the hashed version of the password."""
        return self._password

    password = synonym('_password', descriptor=property(_get_password,
                                                        _set_password))

    def validate_password(self, password):
        """
        Check the password against existing credentials.

        :param password: the password that was provided by the loadingData to
            try and authenticate. This is the clear text version that we will
            need to match against the hashed one in the database.
        :type password: unicode object.
        :return: Whether the password is valid.
        :rtype: bool

        """
        hash = sha256()
        hash.update((password + self.password[:64]).encode('utf-8'))
        return self.password[64:] == hash.hexdigest()


class Permission(DeclarativeBase):
    """
    Permission definition.

    Only the ``permission_name`` column is required.

    """

    __tablename__ = 'tg_permission'

    permission_id = Column(Integer, autoincrement=True, primary_key=True)
    permission_name = Column(Unicode(63), unique=True, nullable=False)
    description = Column(Unicode(255))

    groups = relation(Group, secondary=group_permission_table,
                      backref='permissions')

    def __repr__(self):
        return '<Permission: name=%s>' % repr(self.permission_name)

    def __unicode__(self):
        return self.permission_name
