"""Subject classes (i.e. people, groups, etc.).

See ICOM-ics-v1.0 "Subject Branch".
"""
from datetime import datetime, timedelta

from flask.ext.login import UserMixin

from sqlalchemy.orm import relationship
from sqlalchemy.orm.query import Query
from sqlalchemy.schema import Column, Table, ForeignKey
from sqlalchemy.types import Integer, UnicodeText, LargeBinary, Boolean, DateTime, Text

from .entities import db, Entity, SEARCHABLE, SYSTEM


# Tables for many-to-many relationships
following = Table(
  'following', db.Model.metadata,
  Column('follower_id', Integer, ForeignKey('user.id')),
  Column('followee_id', Integer, ForeignKey('user.id'))
)
membership = Table(
  'membership', db.Model.metadata,
  Column('user_id', Integer, ForeignKey('user.id')),
  Column('group_id', Integer, ForeignKey('group.id'))
)
administratorship = Table(
  'administratorship', db.Model.metadata,
  Column('user_id', Integer, ForeignKey('user.id')),
  Column('group_id', Integer, ForeignKey('group.id'))
)


class UserQuery(Query):
  def get_by_email(self, email):
    return self.filter_by(email=email).all()[0]


class User(UserMixin, Entity):
  __editable__ = ['first_name', 'last_name', 'job_title', 'department', 'company', 'email', 'password']
  __exportable__ = __editable__ + ['created_at', 'updated_at', 'id']

  query_class = UserQuery
  #query = db.session.query_property(UserQuery)

  # Basic information
  first_name = Column(UnicodeText, info=SEARCHABLE)
  last_name = Column(UnicodeText, info=SEARCHABLE)
  # Should we add gender, salutation ?

  # System information
  locale = Column(Text)

  # Additional information (should be customisable)
  job_title = Column(UnicodeText, info=SEARCHABLE)
  department = Column(UnicodeText, info=SEARCHABLE)
  company = Column(UnicodeText, info=SEARCHABLE)
  location = Column(UnicodeText)
  expertise = Column(UnicodeText)
  interests = Column(UnicodeText)
  # More: education, work experience, etc.

  email = Column(UnicodeText, nullable=False)
  # TODO: encrypt
  password = Column(UnicodeText, nullable=False)

  photo = Column(LargeBinary)

  # TODO: move to a roles or permission table
  is_admin = Column(Boolean, nullable=False, default=False)

  last_active = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, info=SYSTEM)

  # TODO: add if needed:
  # location
  # manager
  # phone numbers (office, mobile)
  # email(s)
  # IM addresses
  # social networking addresses
  # properties
  # profile / interests / job description
  # settings

  id = Entity.id
  followers = relationship("User", secondary=following,
                           primaryjoin=(id == following.c.follower_id),
                           secondaryjoin=(id == following.c.followee_id),
                           backref='followees')
  followees = []

  groups = []

  def follow(self, followee):
    if followee == self:
      raise Exception("User can't follow self")
    self.followees.append(followee)

  def unfollow(self, followee):
    if followee == self:
      raise Exception("User can't follow self")
    i = self.followees.index(followee)
    del self.followees[i]

  def join(self, group):
    if not group in self.groups:
      self.groups.append(group)

  def leave(self, group):
    if group in self.groups:
      del self.groups[self.groups.index(group)]

  #
  # Boolean properties
  #
  def is_following(self, other):
    return other in self.followees

  def is_member_of(self, group):
    return self in group.members

  def is_admin_of(self, group):
    return self in group.admins

  @property
  def is_online(self):
    return datetime.utcnow() - self.last_active <= timedelta(0, 60)

  #
  # Other properties
  #
  @property
  def username(self):
    return (self.first_name or "") + (self.last_name or "")

  @property
  def name(self):
    return (self.first_name or "Unknown") + " " + (self.last_name or "Unknown")

  def __unicode__(self):
    return self.name

  # XXX: Should entities know about their own URL? Eventually, no.
  @property
  def _url(self):
    return "/social/users/%d" % self.id


class Group(Entity):
  __editable__ = ['name', 'description']
  __exportable__ = __editable__ + ['created_at', 'updated_at', 'id']

  name = Column(UnicodeText, nullable=False, info=SEARCHABLE)
  description = Column(UnicodeText, info=SEARCHABLE)

  members = relationship("User", secondary=membership,
                         backref='groups')
  admins = relationship("User", secondary=administratorship)

  photo = Column(LargeBinary)

  # XXX: Should entities know about their own URL? Eventually, no.
  @property
  def _url(self):
    return "/social/groups/%d" % self.id

