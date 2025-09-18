"""
Enphase Model and Pydantic Schema

This module defines:
- The SQLAlchemy ORM model for persisting enphase data.
- The Pydantic schema for validating API requests when creating an enphase record.
"""

from sqlalchemy import Column, DateTime, Integer, String
from framework.db import Base
from datetime import datetime, timezone
from pydantic import BaseModel
from typing import Optional


class Enphase(Base):
    """
    SQLAlchemy ORM model representing an Enphase record.

    Attributes:
        id (int): Primary key, unique identifier for the record.
        system_id (int): Unique system ID.
        current_power (int): Current power output in watts.
        energy_lifetime (int): Lifetime energy generated in Wh.
        energy_today (int): Energy generated today in Wh.
        last_interval_end_at (int): Unix timestamp of last interval end.
        last_report_at (int): Unix timestamp of last report.
        modules (int): Number of modules in the system.
        operational_at (int): Unix timestamp when system became operational.
        size_w (int): System size in watts.
        status (str): System status (e.g., "normal").
        summary_date (str): Summary date in YYYY-MM-DD format.
        events (str | None): Optional events log.
        alarms (str | None): Optional alarms log.
        create_date (datetime): Timestamp when the record was created (UTC).
        update_date (datetime): Timestamp when the record was last updated (UTC).
    """

    __tablename__ = "enphase"

    id = Column(Integer, primary_key=True, index=True)
    system_id = Column(Integer, unique=True, nullable=False, index=True)
    current_power = Column(Integer, nullable=False)
    energy_lifetime = Column(Integer, nullable=False)
    energy_today = Column(Integer, nullable=False)
    last_interval_end_at = Column(Integer, nullable=False)
    last_report_at = Column(Integer, nullable=False)
    modules = Column(Integer, nullable=False)
    operational_at = Column(Integer, nullable=False)
    size_w = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    summary_date = Column(String(10), nullable=False)
    events = Column(String, nullable=True)
    alarms = Column(String, nullable=True)
    create_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    update_date = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<Enphase(system_id={self.system_id}, status='{self.status}', summary_date='{self.summary_date}')>"


class EnphaseCreate(BaseModel):
    """
    Pydantic schema for creating a new Enphase record.

    Attributes:
        system_id (int): Unique system ID.
        current_power (int): Current power output in watts.
        energy_lifetime (int): Lifetime energy generated in Wh.
        energy_today (int): Energy generated today in Wh.
        last_interval_end_at (int): Unix timestamp of last interval end.
        last_report_at (int): Unix timestamp of last report.
        modules (int): Number of modules in the system.
        operational_at (int): Unix timestamp when system became operational.
        size_w (int): System size in watts.
        status (str): System status.
        summary_date (str): Summary date in YYYY-MM-DD format.
        events (str | None): Optional events log.
        alarms (str | None): Optional alarms log.
    """

    system_id: int
    current_power: int
    energy_lifetime: int
    energy_today: int
    last_interval_end_at: int
    last_report_at: int
    modules: int
    operational_at: int
    size_w: int
    status: str
    summary_date: str
    events: Optional[str] = None
    alarms: Optional[str] = None
