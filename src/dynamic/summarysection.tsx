// src/components/dynamic/SummarySection.tsx
import { useEffect, useState } from 'react'
import axios from 'axios'

export default function SummarySection({ uuid }: { uuid: string }) {
  const [data, setData] = useState<any | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    axios
      .get(`/api/report/${uuid}/summary`)
      .then((res) => setData(res.data))
      .catch(() => setError("요약 정보를 불러오지 못했습니다."))
      .finally(() => setLoading(false))
  }, [uuid])

  if (loading) return <div className="text-sm text-gray-500">로딩 중...</div>
  if (error) return <div className="text-sm text-red-500">{error}</div>

  return (
    <div className="text-sm whitespace-pre-wrap bg-gray-50 p-4 rounded border overflow-x-auto">
      {JSON.stringify(data, null, 2)}
    </div>
  )
}
