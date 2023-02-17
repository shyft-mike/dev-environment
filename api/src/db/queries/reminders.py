from dataclasses import dataclass
from typing import List
from db.client import connection

from db.queries.models.reminder import Reminder

db = connection.get_database("reminderDB")


@dataclass
class ReminderResponse:
    reminders: List[Reminder]

    def to_response(self):
        return {
            "reminders": [Reminder.to_response(reminder) for reminder in self.reminders]
        }


def get_reminders() -> ReminderResponse:
    return ReminderResponse(
        [
            Reminder.from_document(reminder_document)
            for reminder_document in db.reminders.find()
        ]
    )
