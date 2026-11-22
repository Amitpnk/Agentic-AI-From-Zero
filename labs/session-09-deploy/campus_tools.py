# campus_tools.py: the tools our agent can use (fake college data + one real weather API)
import datetime
import requests

EXAMS = {
    "DBMS": {"subject": "DBMS", "date": "2026-12-12", "day": "Saturday", "time": "10 AM", "hall": "Hall B"},
    "OS":   {"subject": "OS",   "date": "2026-12-14", "day": "Monday",   "time": "2 PM",  "hall": "Hall A"},
    "CN":   {"subject": "CN",   "date": "2026-12-16", "day": "Wednesday", "time": "10 AM", "hall": "Hall C"},
}


def get_exam_date(subject: str) -> dict:
    """Get the date, day, time and hall of a student's semester exam. subject: DBMS, OS or CN."""
    exam = EXAMS.get(subject.strip().upper())
    if exam is None:
        return {"error": f"No exam found for '{subject}'. Known subjects: DBMS, OS, CN."}
    return exam


def get_library_hours(date: str) -> dict:
    """Get the central library's opening hours for one date. date: YYYY-MM-DD."""
    try:
        d = datetime.date.fromisoformat(date)
    except ValueError:
        return {"error": "Use the date format YYYY-MM-DD, for example 2026-12-13."}
    day = d.strftime("%A")
    if d.weekday() == 6:                      # Sunday
        if d.month in (5, 12):                # exam months
            return {"date": date, "day": day, "open": "10:00", "close": "16:00",
                    "note": "Sunday opening during exam month"}
        return {"date": date, "day": day, "open": None, "close": None, "note": "Closed on Sundays"}
    return {"date": date, "day": day, "open": "08:00", "close": "20:00"}


BOOKINGS = []


def book_study_room(date: str, start: str, hours: int) -> dict:
    """Book a library study room. date: YYYY-MM-DD, start: HH:MM in 24-hour time, hours: 1 to 3."""
    hours = int(hours)                        # the model may send 2.0 instead of 2
    if not 1 <= hours <= 3:
        return {"status": "failed", "reason": "You can book between 1 and 3 hours only."}
    lib = get_library_hours(date)
    if "error" in lib:
        return {"status": "failed", "reason": lib["error"]}
    if lib["open"] is None:
        return {"status": "failed", "reason": f"The library is closed on {lib['day']} {date}."}
    start_h = int(start.split(":")[0])
    if start_h < int(lib["open"][:2]) or start_h + hours > int(lib["close"][:2]):
        return {"status": "failed", "reason": f"The library is only open {lib['open']}-{lib['close']} that day."}
    room = f"S{len(BOOKINGS) + 1}"
    BOOKINGS.append({"room": room, "date": date, "start": start, "hours": hours})
    return {"status": "confirmed", "room": room, "date": date, "start": start, "hours": hours}


def get_weather(city: str) -> dict:
    """Get the current temperature and today's and tomorrow's rain chance for a city (free Open-Meteo API, no key)."""
    geo = requests.get("https://geocoding-api.open-meteo.com/v1/search",
                       params={"name": city, "count": 1}, timeout=10).json()
    if not geo.get("results"):
        return {"error": f"City '{city}' not found."}
    place = geo["results"][0]
    wx = requests.get("https://api.open-meteo.com/v1/forecast", params={
        "latitude": place["latitude"], "longitude": place["longitude"],
        "current": "temperature_2m",
        "daily": "precipitation_probability_max,temperature_2m_max,temperature_2m_min",
        "timezone": "auto", "forecast_days": 2,
    }, timeout=10).json()
    daily = wx["daily"]
    days = [{"date": daily["time"][i],
             "rain_chance_pct": daily["precipitation_probability_max"][i],
             "max_c": daily["temperature_2m_max"][i],
             "min_c": daily["temperature_2m_min"][i]} for i in range(2)]
    return {"city": place["name"], "now_c": wx["current"]["temperature_2m"], "today": days[0], "tomorrow": days[1]}
