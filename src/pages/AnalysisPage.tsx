// src/pages/AnalysisPage.tsx

import { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import axios from 'axios'

interface AnalysisResult {
  summary: string[]
  yara_rules: string
}

export default function AnalysisPage() {
  const location = useLocation()
  const filename = (location.state as { filename?: string })?.filename
  const navigate = useNavigate()

  const [data, setData] = useState<AnalysisResult | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    ;(async () => {
      if (!filename) {
        navigate('/')
        return
      }
      try {
        const res = await axios.get<AnalysisResult>(
          `http://localhost:8000/reports/${filename}`
        )
        setData(res.data)
      } catch (err: any) {
        setError(err.response?.data?.detail || err.message)
      } finally {
        setLoading(false)
      }
    })()
  }, [filename, navigate])

  const handleDownloadJSON = () => {
    if (!data) return
    const payload = {
      summary: data.summary,
      yara_rules: data.yara_rules,
    }
    const blob = new Blob([JSON.stringify(payload, null, 2)], {
      type: 'application/json',
    })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${filename}.summary.json`
    a.click()
    URL.revokeObjectURL(url)
  }

  const handleDownloadReport = () => {
    // 테스트용 스텁: 나중에 PDF 다운로드 로직으로 대체 예정
    alert('Report PDF 다운로드 테스트용 버튼입니다.')
  }

  if (loading) return <div className="p-8">로딩 중…</div>
  if (error) return <div className="p-8">오류 발생: {error}</div>
  if (!data) return <div className="p-8">분석 결과를 찾을 수 없습니다.</div>

  return (
    <div className="p-8">
      {/* 버튼 영역 */}
      <div className="mb-6 flex justify-end space-x-2">
        <button
          onClick={handleDownloadReport}
          className="border border-green-600 text-green-600 hover:bg-green-50 font-semibold px-4 py-2 rounded"
        >
          Download Report
        </button>
        <button
          onClick={handleDownloadJSON}
          className="bg-green-600 hover:bg-green-700 text-white font-semibold px-4 py-2 rounded"
        >
          Download JSON
        </button>
      </div>

      {/* Summary & YARA 룰 박스 */}
      <h2 className="text-xl font-bold mb-4">Summary &amp; YARA 룰</h2>
      <div className="grid grid-cols-2 gap-6">
        {/* Summary 박스 */}
        <div
          className="border-2 rounded-lg bg-white p-4"
          style={{ borderColor: '#A3E635' }}
        >
          <h3 className="font-semibold mb-2 text-sm">Summary</h3>
          <ul className="list-decimal list-inside text-sm h-64 overflow-auto">
            {data.summary.length > 0 ? (
              data.summary.map((line, i) => <li key={i}>{line}</li>)
            ) : (
              <li>요약 내용이 없습니다.</li>
            )}
          </ul>
        </div>

        {/* YARA 룰 박스 */}
        <div
          className="border-2 rounded-lg bg-white p-4"
          style={{ borderColor: '#A3E635' }}
        >
          <h3 className="font-semibold mb-2 text-sm">YARA 룰</h3>
          <pre className="whitespace-pre-wrap text-sm h-64 overflow-auto">
            {data.yara_rules || '// YARA 룰이 없습니다.'}
          </pre>
        </div>
      </div>
    </div>
  )
}
