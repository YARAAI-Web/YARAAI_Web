// src/dynamic/SummarySection.tsx

import React, { useEffect, useState } from 'react'

interface Props {
  uuid: string
}

export default function SummarySection({ uuid }: Props) {
  const [summary, setSummary] = useState<string[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (!uuid) return
    setLoading(true)
    fetch(`http://localhost:8000/api/report/${uuid}/summary-ai`)
      .then((res) => res.json())
      .then((data) => setSummary(data.summary || []))
      .catch(() => setError('요약 정보를 불러오지 못했습니다.'))
      .finally(() => setLoading(false))
  }, [uuid])

  if (loading) return <p className="text-sm text-gray-500">요약 불러오는 중...</p>
  if (error) return <p className="text-sm text-red-500">{error}</p>

  return (
    <div className="bg-gray-50 border border-gray-300 rounded-lg p-4 text-sm leading-relaxed space-y-2 whitespace-pre-wrap">
      {summary.map((line, idx) => (
        <p key={idx}>{line}</p>
      ))}
    </div>
  )
}
