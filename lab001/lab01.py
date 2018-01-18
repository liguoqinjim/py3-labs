from raven import Client

client = Client('https://f65897ed2a5641d192d41c3ba68c1f34:0cb123e09d9f48dd89dabb26c8c720c8@sentry.io/273593')

client.captureMessage('Something went fundamentally wrong')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()