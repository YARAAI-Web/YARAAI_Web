// src/components/GPTSection.tsx
import { useEffect, useState } from 'react'
import type { Metadata } from '../api/report'
import { fetchSection } from '../api/report'

interface GPTSectionProps {
  sectionId: number
  metadata: Metadata
}

export default function GPTSection({ sectionId, metadata }: GPTSectionProps) {
  const [content, setContent] = useState<string>('')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    setLoading(true)
    setError(null)
    // 자리만 차지하도록
    fetchSection(sectionId, metadata)
      .then((res) => setContent(res.text))
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [sectionId, metadata])

  if (loading) return <p className="text-gray-500">로딩 중…</p>
  if (error)
    return (
      <p className="text-red-600">
        GPT 응답 불러오는 중 오류:
        <br />
        <code>{error}</code>
      </p>
    )
  return (
    <div className="prose prose-sm text-gray-800">
      {content.split('\n').map((l, i) => (
        <p key={i}>{l}</p>
      ))}
    </div>
  )
}
