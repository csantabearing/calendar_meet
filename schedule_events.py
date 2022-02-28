from gcsa.google_calendar import GoogleCalendar
import webbrowser


def open_event(code):
    os.system("echo 'on 0' | cec-client -s -d 1")
    webbrowser.open(f'meet.google.com/{code}')


def close_chrome():
    os.system("echo 'standby 0' | cec-client -s -d 1")
    os.system('pkill -o chromium-browser')