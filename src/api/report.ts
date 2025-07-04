/** 백엔드가 내려주는 전체 분석 JSON 타입 */
export interface AnalysisJson {
  get_metadata: {
    path: string
    module: string // ex) "abcd1234.exe"
    md5: string
    sha256: string
    sha1?: string
    format?: string // ex) "exe"
    size?: number // 바이트
    filesize?: string // ex) "0x138000"
  }
  // 나중에 필요할 때 추가로 선언하세요
}

/** 화면에서 쓰는 메타데이터 타입 */
export interface Metadata {
  module: string // 실행파일명
  hash: string // SHA256
  submittedAt: string // 날짜 문자열
  md5: string
  sha1?: string
  fileType: string // ex) "exe"
  fileSize: string // ex) "1248.0 KB"
}

/** (임시) 각 섹션에 보내는 fetch 함수
    — 지금은 sectionId, metadata 두 개만 넘겨서
      프론트에서 자리만 잡아둡니다. */
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
