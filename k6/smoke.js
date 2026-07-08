import http from "k6/http";
import { check } from "k6";

export const options = { thresholds: { http_req_duration: ["p(95)<250"] } };

export default function () {
  const res = http.get("http://localhost:8000/api/dashboard");
  check(res, { "dashboard ok": (r) => r.status === 200 });
}
