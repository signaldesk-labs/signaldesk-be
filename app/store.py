from datetime import datetime

EVENTS = [
    {"id": "evt-1", "title": "event triage", "status": "requested", "severity": "high", "updatedAt": datetime.utcnow().date().isoformat()},
    {"id": "evt-2", "title": "saved filters", "status": "approved", "severity": "medium", "updatedAt": datetime.utcnow().date().isoformat()},
]

METRICS = [
    {"key": "event_p95_ms", "label": "event p95 ms", "value": 184, "unit": "ms", "target": 220},
    {"key": "chart_render_ms", "label": "chart render ms", "value": 92, "unit": "%", "target": 90},
    {"key": "legacy_api_match_rate", "label": "legacy api match rate", "value": 37, "unit": "events", "target": 30},
]
