from dataclasses import dataclass, field
from datetime import datetime, date, time
from platform import system
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


# TODO: Implement Reminder class here
@dataclass
class Reminder:
    date_time: datetime
    EMAIL: str = "email"
    SYSTEM: str = "system"
    type: str = EMAIL

    def __str__(self) -> str:
        return f"Reminder on {self.date_time} of type {self.type}"


# TODO: Implement Event class here
@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time
    reminders: list[Reminder] = field(default_factory=list)
    id: str = field(default_factory=generate_unique_id)

    def add_reminder(self, date_time: datetime, type: str):
        reminder = Reminder(date_time, type)
        self.reminders.append(reminder)

    def delete_reminder(self, reminder_index: int):
        if 0 <= reminder_index < len(self.reminders):
            self.reminders.pop(reminder_index)
        else:
            reminder_not_found_error()

    def __str__(self) -> str:
        return (f"ID: {self.id}\n"
                f"Event title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Time: {self.start_at} - {self.end_at}")








# TODO: Implement Day class here


# TODO: Implement Calendar class here