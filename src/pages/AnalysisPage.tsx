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

  const handleDownload = () => {
    if (!data) return
    const downloadData = {
      get_metadata: data.get_metadata,
      get_current_address: data.get_current_address,
      get_current_function: data.get_current_function,
      get_entry_points: data.get_entry_points,
      file_entropy: data.file_entropy,
      string_stats: data.string_stats,
      pe_headers: data.pe_headers,
      c_code: data.c_code,
      h_code: data.h_code,
      virustotal: data.virustotal,
    }
    const blob = new Blob([JSON.stringify(downloadData, null, 2)], {
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
      {/* 1. 헤더(Report 버튼) 바로 아래 */}
      <div className="mb-4 text-right">
        <button
          onClick={handleDownload}
          className="bg-green-600 hover:bg-green-700 text-white font-semibold px-4 py-2 rounded"
        >
          Download JSON
        </button>
      </div>

      {/* 2. 본문 */}
      <h1 className="text-2xl font-bold mb-4">Analysis: {filename}</h1>

      {/* 파일 메타데이터 */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">파일 메타데이터</h2>
        <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
          {JSON.stringify(data.get_metadata, null, 2)}
        </pre>
      </section>

      {/* Current Address */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">Current Address</h2>
        <p className="bg-gray-100 p-4 rounded">{data.get_current_address}</p>
      </section>

      {/* Current Function */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">Current Function</h2>
        <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
          {JSON.stringify(data.get_current_function, null, 2)}
        </pre>
      </section>

      {/* Entry Points */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">Entry Points</h2>
        <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
          {JSON.stringify(data.get_entry_points, null, 2)}
        </pre>
      </section>

      {/* 파일 엔트로피 */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">파일 엔트로피</h2>
        <p className="bg-gray-100 p-4 rounded">{data.file_entropy}</p>
      </section>

      {/* String Stats */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">String Stats</h2>
        <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
          {JSON.stringify(data.string_stats, null, 2)}
        </pre>
      </section>

      {/* PE 헤더 */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">PE 헤더</h2>
        <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
          {JSON.stringify(data.pe_headers, null, 2)}
        </pre>
      </section>

      {/* .c 코드 */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">.c 코드</h2>
        <pre className="bg-white p-4 h-64 overflow-auto whitespace-pre-wrap">
          {data.c_code.join('\n')}
        </pre>
      </section>

      {/* .h 코드 */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">.h 코드</h2>
        <pre className="bg-white p-4 h-64 overflow-auto whitespace-pre-wrap">
          {data.h_code.join('\n')}
        </pre>
      </section>

      {/* VirusTotal */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">VirusTotal</h2>
        <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
          {JSON.stringify(data.virustotal, null, 2)}
        </pre>
      </section>

      {/* Summary & YARA 룰 */}
      <section className="mb-8">
        <h2 className="text-lg font-semibold mb-2">Summary &amp; YARA 룰</h2>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <h3 className="font-semibold mb-1">Summary</h3>
            <ul className="list-decimal list-inside bg-white p-4 h-64 overflow-auto border rounded">
              {data.summary.length > 0 ? (
                data.summary.map((line, i) => <li key={i}>{line}</li>)
              ) : (
                <li>요약 내용이 없습니다.</li>
              )}
            </ul>
          </div>
          <div>
            <h3 className="font-semibold mb-1">YARA 룰</h3>
            <pre className="bg-white p-4 h-64 overflow-auto border rounded whitespace-pre-wrap">
              {data.yara_rules || '// YARA 룰이 없습니다.'}
            </pre>
          </div>
        </div>
      </section>
    </div>
  )
}
