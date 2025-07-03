// src/pages/AnalysisPage.tsx

import { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import axios from 'axios'

interface AnalysisResult {
  get_metadata: Record<string, any>
  get_current_address: string
  get_current_function: Record<string, any>
  get_entry_points: any[]
  file_entropy: number
  string_stats: Record<string, any>
  pe_headers: Record<string, any>
  c_code: string[]
  h_code: string[]
  virustotal: Record<string, any>
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

  const handleDownloadJSON = async () => {
    if (!filename || !data) return

    // fetch original JSON report
    const res = await axios.get<AnalysisResult>(
      `http://localhost:8000/reports/${filename}`
    )
    const orig = res.data

    // build in desired order, omitting summary & yara_rules
    const ordered: Partial<AnalysisResult> = {
      get_metadata: orig.get_metadata,
      get_current_address: orig.get_current_address,
      get_current_function: orig.get_current_function,
      get_entry_points: orig.get_entry_points,
      file_entropy: orig.file_entropy,
      string_stats: orig.string_stats,
      pe_headers: orig.pe_headers,
      c_code: orig.c_code,
      h_code: orig.h_code,
      virustotal: orig.virustotal,
      // summary & yara_rules omitted
    }

    const blob = new Blob([JSON.stringify(ordered, null, 2)], {
      type: 'application/json',
    })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${filename}.json`
    a.click()
    URL.revokeObjectURL(url)
  }

  if (loading) return <div className="p-8">로딩 중…</div>
  if (error) return <div className="p-8">오류 발생: {error}</div>
  if (!data) return <div className="p-8">분석 결과를 찾을 수 없습니다.</div>

  return (
    <div className="p-8">
      {/* Download 버튼 */}
      <div className="mb-6 text-right">
        <button
          onClick={handleDownloadJSON}
          className="bg-green-600 hover:bg-green-700 text-white font-semibold px-4 py-2 rounded"
        >
          Download JSON
        </button>
      </div>

      {/* Summary & YARA 룰 UI 그대로 */}
      <h2 className="text-xl font-bold mb-4">Summary &amp; YARA 룰</h2>
      <div className="grid grid-cols-2 gap-6">
        <div
          className="border-2 rounded-lg bg-white p-4 h-64 overflow-auto"
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
          className="border-2 rounded-lg bg-white p-4 h-64 overflow-auto"
          style={{ borderColor: '#A3E635' }}
        >
          <h3 className="font-semibold mb-2 text-sm">YARA 룰</h3>
          <pre className="whitespace-pre-wrap text-sm">
            {data.yara_rules || '// YARA 룰이 없습니다.'}
          </pre>
        </div>
      </div>
    </div>
  )
}
