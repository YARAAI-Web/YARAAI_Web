// src/pages/AnalysisPage.tsx
import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import axios from 'axios'

interface AnalysisResult {
  get_metadata: Record<string, any>
  summary: string[]
  yara_rules: string
  // ... 필요 필드 추가 선언
}

export default function AnalysisPage() {
  const { filename } = useParams<{ filename: string }>()
  const navigate = useNavigate()
  const [data, setData] = useState<AnalysisResult | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (!filename) {
      navigate('/')
      return
    }
    axios
      .get<AnalysisResult>(`http://localhost:8000/reports/${filename}`)
      .then((res) => setData(res.data))
      .catch((e) => setError(e.response?.data?.detail || e.message))
      .finally(() => setLoading(false))
  }, [filename, navigate])

  if (loading) return <div className="p-8">로딩 중…</div>
  if (error) return <div className="p-8 text-red-600">오류: {error}</div>
  if (!data) return <div className="p-8">분석 결과를 찾을 수 없습니다.</div>

  return (
    <div className="p-8">
      {/* Summary & YARA 룰 */}
      <h2 className="text-xl font-bold mb-4">Summary &amp; YARA 룰</h2>
      <div className="grid grid-cols-2 gap-6 mb-8">
        <div
          className="border-2 rounded-lg p-4 h-64 overflow-auto"
          style={{ borderColor: '#A3E635' }}
        >
          <h3 className="font-semibold mb-2 text-sm">Summary</h3>
          <ul className="list-decimal list-inside text-sm">
            {data.summary.length > 0 ? (
              data.summary.map((line, i) => <li key={i}>{line}</li>)
            ) : (
              <li>요약 내용이 없습니다.</li>
            )}
          </ul>
        </div>
        <div
          className="border-2 rounded-lg p-4 h-64 overflow-auto"
          style={{ borderColor: '#A3E635' }}
        >
          <h3 className="font-semibold mb-2 text-sm">YARA 룰</h3>
          <pre className="whitespace-pre-wrap text-sm">
            {data.yara_rules || '// YARA 룰이 없습니다.'}
          </pre>
        </div>
      </div>

      {/* 보고서 생성 버튼 */}
      <div className="flex justify-center">
        <button
          onClick={() => navigate(`/report/${filename}`)}
          className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-3 rounded-lg text-lg"
        >
          보고서 생성
        </button>
      </div>
    </div>
  )
}
