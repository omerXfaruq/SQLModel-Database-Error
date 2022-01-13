# SQLModel-Database-Error
SQLModel-Database-Error demo using sqlite database.



```
➜  Database-Test uvicorn main:app
INFO:     Started server process [41634]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:53963 - "POST /user/ HTTP/1.1" 200 OK
tick: 8, user: telegram_chat_id=0 active=True id=1 name='string' gmt=0 scheduled_hours='8,20' , reminders: []
tick: 9, user: telegram_chat_id=0 active=True id=1 name='string' gmt=0 scheduled_hours='8,20' reminders=[] , reminders: []
INFO:     127.0.0.1:53964 - "POST /reminder/ HTTP/1.1" 200 OK     ### A Reminder is created at this point with user_id 1
tick: 10, user: telegram_chat_id=0 active=True id=1 name='string' gmt=0 scheduled_hours='8,20' reminders=[] , reminders: []
tick: 11, user: telegram_chat_id=0 active=True id=1 name='string' gmt=0 scheduled_hours='8,20' reminders=[] , reminders: []
tick: 12, user: telegram_chat_id=0 active=True id=1 name='string' gmt=0 scheduled_hours='8,20' reminders=[] , reminders: []
tick: 13, user: telegram_chat_id=0 active=True id=1 name='string' gmt=0 scheduled_hours='8,20' reminders=[] , reminders: []
^CINFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [41634]
➜  Database-Test uvicorn main:app
INFO:     Started server process [41664]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
tick: 1, user: telegram_chat_id=0 active=True id=1 name='string' gmt=0 scheduled_hours='8,20' , reminders: [Reminder(reminder='string1', user_id=1, id=1)]

```