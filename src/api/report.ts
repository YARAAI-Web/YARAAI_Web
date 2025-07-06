// src/api/report.ts

/** 백엔드가 내려주는 전체 분석 JSON 타입 */
export interface AnalysisJson {
  get_metadata: {
    path: string
    module: string
    md5: string
    sha256: string
    sha1?: string
    format?: string
    size?: number
    filesize?: string
  }
}

/** 화면에서 쓰는 메타데이터 타입 */
export interface Metadata {
  module: string
  hash: string
  submittedAt: string
  md5: string
  sha1?: string
  fileType: string
  fileSize: string
}

/** 각 섹션에 보내는 fetch 함수 */
export async function fetchSection(
  sectionId: number,
  metadata: Metadata
): Promise<{ text: string }> {
  const res = await fetch('/api/section', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ sectionId, metadata }),
  })
  if (!res.ok) {
    const err = await res.text()
    throw new Error(`Section fetch failed (${res.status}): ${err}`)
  }
  return res.json()
}
