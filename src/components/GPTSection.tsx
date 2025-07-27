// src/components/GPTSection.tsx
import { useEffect, useState } from 'react'
import type { Metadata } from '../api/report'
import { fetchSection } from '../api/report'

interface GPTSectionProps {
  sectionId: number
  metadata: Metadata
}

export default function GPTSection({ sectionId, metadata }: GPTSectionProps) {
  const [content, setContent] = useState<string>('')       // GPT 응답 텍스트
  const [loading, setLoading] = useState(true)             // 로딩 상태
  const [error, setError] = useState<string | null>(null)  // 에러 메시지

  useEffect(() => {
    setLoading(true)
    setError(null)
    fetchSection(sectionId, metadata)
      .then((res) => setContent(res.text))
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [sectionId, metadata])

  if (loading) return <p className="text-gray-500">로딩 중…</p>
  if (error)
    return (
      <p className="text-red-600 whitespace-pre-wrap">
        GPT 응답 불러오는 중 오류:
        <br />
        <code>{error}</code>
      </p>
    )

  return (
    <div className="prose prose-sm text-gray-800">
      {content.split('\n').map((line, i) => (
        <p key={i}>{line}</p>
      ))}
    </div>
  )
}
