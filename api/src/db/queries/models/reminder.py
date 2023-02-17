from dataclasses import dataclass


@dataclass
class Reminder:
    title: str
    reminder_time: str
    action: str

    @staticmethod
    def from_document(document):
        return Reminder(
            title=document["title"],
            reminder_time=document["reminderTime"],
            action=document["action"],
        )

    @staticmethod
    def to_response(reminder):
        return {
            "title": reminder.title,
            "reminderTime": reminder.reminder_time,
            "action": reminder.action,
        }
