"""
Interface for the synchronization client.

The client or node emits 'push' and 'pull' requests to the server. The
client can also request a registry key if it hasn't been given one
yet.
"""

from dbsync.client.tracking import track
from dbsync.client.settings import configure_networking

# TODO export list