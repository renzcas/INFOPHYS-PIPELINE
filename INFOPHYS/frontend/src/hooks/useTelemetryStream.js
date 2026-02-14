import { useEffect, useRef, useState } from "react"

export function useTelemetryStream(url) {
  const [latest, setLatest] = useState(null)
  const [history, setHistory] = useState([])
  const wsRef = useRef(null)

  useEffect(() => {
    wsRef.current = new WebSocket(url)

    wsRef.current.onmessage = (event) => {
      try {
        const msg = JSON.parse(event.data)
        setLatest(msg)
        setHistory((prev) => [...prev.slice(-499), msg]) // keep last 500
      } catch (e) {
        console.error("Bad telemetry message", e)
      }
    }

    return () => {
      if (wsRef.current) wsRef.current.close()
    }
  }, [url])

  return { latest, history }
}