// src/api/fetchCapaResult.ts
export interface CapaReportResponse {
  report: string
}

export async function fetchCapaReport(
  sha256: string
): Promise<CapaReportResponse> {
  const res = await fetch('/api/capa-report', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ sha256 }),
  })
  if (!res.ok) {
    const err = await res.json().catch(() => null)
    throw new Error(err?.detail || 'CAPA 보고서 요청 실패')
  }
  return res.json()
}
