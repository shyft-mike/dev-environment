db = db.getSiblingDB("reminderDB");

db.createCollection("reminders");

db.reminders.insertMany([
  {
    title: "helpdev",
    reminderTime: "EVENT_A",
    action: "alert",
  },
]);
