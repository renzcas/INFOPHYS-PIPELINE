import asyncio

class TelemetryBus:
    def __init__(self):
        self.subscribers = []

    def subscribe(self):
        q = asyncio.Queue()
        self.subscribers.append(q)
        return q

    def unsubscribe(self, q):
        self.subscribers.remove(q)

    async def publish(self, event):
        for q in self.subscribers:
            await q.put(event)