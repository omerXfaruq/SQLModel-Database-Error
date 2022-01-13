from fastapi import FastAPI, Depends, Query
from typing import List
import asyncio

from db import User, UserRead, UserCreate, Reminder, ReminderCreate, ReminderRead, Session, create_db_and_tables, get_session, select, db_read_users, delete_memory, add_hours_to_the_schedule

name = "temp_name"
chat_id = -1101

app = FastAPI()


async def main_event() -> None:
    """
    Main Event Loop

    Runs in a while loop, Triggers Events.send_user_hourly_memories at every hour.
    """
    tick = 0
    while True:
        tick += 1
        await asyncio.sleep(10)
        users = db_read_users(limit=100000)
        for user in users:
            print(f"tick: {tick}, user: {user} , reminders: {user.reminders}")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    asyncio.create_task(main_event())


@app.post("/addhours/", response_model=UserRead)
def addhours(*, session: Session = Depends(get_session)):
    user = UserCreate(
        name="string",
        telegram_chat_id=0,
    )

    add_hours_to_the_schedule(user, [2, 2, 2], session)


@app.post("/user/", response_model=UserRead)
def create_user(*, session: Session = Depends(get_session), user: UserCreate):
    user = User.from_orm(user)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.get("/users/", response_model=List[UserRead])
def read_users(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@app.post("/reminder/", response_model=ReminderRead)
def create_reminder(
    *, session: Session = Depends(get_session), reminder: ReminderCreate
):
    db_reminder = Reminder.from_orm(reminder)
    session.add(db_reminder)
    session.commit()
    session.refresh(db_reminder)
    return db_reminder


@app.get("/reminders/", response_model=List[ReminderRead])
def read_reminders(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    reminders = session.exec(select(Reminder).offset(offset).limit(limit)).all()
    return reminders


def delete_reminder(*, session: Session = Depends(get_session), user: UserCreate, memory_id: int):
    delete_memory(user, memory_id, session)
