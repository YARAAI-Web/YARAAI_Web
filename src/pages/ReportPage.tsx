// src/api/report.ts
/**
 * 각 섹션에 보내는 fetch 함수
 * - 두 번째 인자에 전체 report(JSON)를 넘깁니다.
 */
export async function fetchSection(
  sectionId: number,
  filename: string
): Promise<{ text: string }> {
  const res = await fetch('/api/section', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    // 기존 metadata 대신 전체 report 객체를 metadata 필드로 보냅니다
    body: JSON.stringify({ sectionId, filename }),
  })
  if (!res.ok) {
    const err = await res.text()
    throw new Error(`Section fetch failed (${res.status}): ${err}`)
  }
  return res.json()
}
