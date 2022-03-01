from gcsa.google_calendar import GoogleCalendar
import sched, time
import webbrowser
s = sched.scheduler(time.time, time.sleep)
calendar = GoogleCalendar('camilo@bearing.ai')


def open_event(code):
    #os.system("echo 'on 0' | cec-client -s -d 1")
    #webbrowser.open(f'meet.google.com/{code}')
    print(code)


def close_chrome():
    os.system("echo 'standby 0' | cec-client -s -d 1")
    os.system('pkill -o chromium-browser')


while True:
    for event in calendar:
        if event.conference_solution:
            if event.conference_solution['solution_type'] == 'hangoutsMeet':
                s.enterabs(event.start,
                           1,
                           open_event,
                           kwargs={'code': event.conference_solution['conference_id']})
        s.run(False)