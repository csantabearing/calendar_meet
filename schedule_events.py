from gcsa.google_calendar import GoogleCalendar
import sched, time
import webbrowser
import os

s = sched.scheduler(time.time, time.sleep)
calendar = GoogleCalendar('camilo@bearing.ai')


def open_event(code):
    os.system("echo 'on 0' | cec-client -s -d 1")
    webbrowser.open(f'meet.google.com/{code}')
    print(code)


def close_event():
    os.system("echo 'standby 0' | cec-client -s -d 1")
    os.system('pkill -o chromium-browser')


def is_global(event):
    if 'raspi' in event.summary: return True
    if len(event.attendees) > 10:
        if event.conference_solution:
            if event.conference_solution.solution_type == 'hangoutsMeet':
                return True
    return False


while True:
    for event in calendar:
        if is_global(event):
            print(event.summary, event.start, event.end)
            s.enterabs(float(event.start.timestamp()),
                       1,
                       open_event,
                       kwargs={'code': event.conference_solution.conference_id})
            s.enterabs(float(event.end.timestamp()), 1, close_event)
    s.run(False)
    time.sleep(30 * 60)
