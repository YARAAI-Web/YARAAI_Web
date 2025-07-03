// src/pages/HistoryDetailPage.tsx

import { useParams, useNavigate } from 'react-router-dom'
import { useEffect, useState } from 'react'
import axios from 'axios'
import Layout from '../components/Layout'

interface FullReport {
  summary?: string[]
  yara_rules?: string
  [key: string]: any
}

export default function HistoryDetailPage() {
  const { filename } = useParams<{ filename: string }>()
  const navigate = useNavigate()
  const [report, setReport] = useState<FullReport | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (!filename) return
    axios
      .get<FullReport>(`http://localhost:8000/reports/${filename}`)
      .then((res) => setReport(res.data))
      .catch(() => setError('리포트를 불러오는 중 오류가 발생했습니다.'))
      .finally(() => setLoading(false))
  }, [filename])

  // JSON 다운로드
  const downloadJson = () => {
    if (!report) return
    const blob = new Blob([JSON.stringify(report, null, 2)], {
      type: 'application/json',
    })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${filename}.json`
    a.click()
    URL.revokeObjectURL(url)
  }

  if (loading)
    return (
      <Layout>
        <p className="p-8 text-center">로딩 중…</p>
      </Layout>
    )
  if (error)
    return (
      <Layout>
        <p className="p-8 text-red-500">{error}</p>
      </Layout>
    )
  if (!report)
    return (
      <Layout>
        <p className="p-8">보고서를 찾을 수 없습니다.</p>
      </Layout>
    )

  return (
    <Layout>
      <div className="w-full max-w-5xl mx-auto px-8 mt-6 relative">
        {/* 헤더: 파일명 + 버튼 */}
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-2xl font-bold">{filename}</h2>
          <button
            onClick={downloadJson}
            className="bg-green-600 hover:bg-green-700 text-white font-semibold px-4 py-2 rounded"
          >
            Download JSON
          </button>
        </div>

        {/* Summary & YARA 룰 섹션 */}
        <h3 className="text-xl font-bold mb-4">Summary &amp; YARA 룰</h3>
        <div className="grid grid-cols-2 gap-6">
          {/* Summary 박스 */}
          <div
            className="border-2 rounded-lg bg-white p-4 min-h-[200px] overflow-auto"
            style={{ borderColor: '#A3E635' }}
          >
            <h4 className="font-semibold mb-2">Summary</h4>
            <ul className="list-decimal list-inside text-sm">
              {report.summary && report.summary.length > 0 ? (
                report.summary.map((line, i) => <li key={i}>{line}</li>)
              ) : (
                <li>요약 내용이 없습니다.</li>
              )}
            </ul>
          </div>

          {/* YARA 룰 박스 */}
          <div
            className="border-2 rounded-lg bg-white p-4 min-h-[200px] overflow-auto"
            style={{ borderColor: '#A3E635' }}
          >
            <h4 className="font-semibold mb-2">YARA 룰</h4>
            <pre className="whitespace-pre-wrap text-sm">
              {report.yara_rules || '// YARA 룰이 없습니다.'}
            </pre>
          </div>
        </div>

        {/* 뒤로 가기 버튼 */}
        <div className="mt-8 flex justify-center">
          <button
            onClick={() => navigate('/history')}
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-3 rounded-lg text-lg"
          >
            History로 돌아가기
          </button>
        </div>
      </div>
    </Layout>
  )
}
