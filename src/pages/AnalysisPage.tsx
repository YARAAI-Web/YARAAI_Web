// src/pages/AnalysisPage.tsx

import { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import axios from 'axios'
import Layout from '../components/Layout'

interface AnalysisResult {
  virustotal: { [k: string]: any }
  c_code: string[]
  h_code: string[]
  pe_headers: Record<string, any>
  get_metadata: Record<string, any>
  get_current_address: string | null
  get_current_function: Record<string, any>
  get_entry_points: any[]
  file_entropy: number
  string_stats: Record<string, any>
  mcp_strings: Record<string, any>
  summary: string[]
  yara_rules: string
}

export default function AnalysisPage() {
  const location = useLocation()
  const filename = (location.state as { filename?: string })?.filename
  const navigate = useNavigate()

  const [data, setData] = useState<AnalysisResult | null>(null)
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (!filename) {
      navigate('/') // filename 없으면 메인으로
      return
    }

    axios
      .get<AnalysisResult>(`http://localhost:8000/reports/${filename}`)
      .then((res) => setData(res.data))
      .catch((err) => setError(err.response?.data?.detail || err.message))
      .finally(() => setLoading(false))
  }, [filename, navigate])

  if (loading) return <Layout>로딩 중…</Layout>
  if (error) return <Layout>오류 발생: {error}</Layout>
  if (!data) return <Layout>분석 결과를 찾을 수 없습니다.</Layout>

  return (
    <Layout>
      {/* 타이틀 */}
      <h1 className="text-2xl font-bold mb-4">Analysis: {filename}</h1>

      {/* VirusTotal */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">VirusTotal</h2>
        <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
          {JSON.stringify(data.virustotal, null, 2)}
        </pre>
      </section>

      {/* .c / .h 코드 */}
      <div className="grid grid-cols-2 gap-4 mb-6">
        <div>
          <h2 className="font-semibold mb-1">.c 코드</h2>
          <pre className="bg-white p-4 h-64 overflow-auto whitespace-pre-wrap">
            {data.c_code.join('\n')}
          </pre>
        </div>
        <div>
          <h2 className="font-semibold mb-1">.h 코드</h2>
          <pre className="bg-white p-4 h-64 overflow-auto whitespace-pre-wrap">
            {data.h_code.join('\n')}
          </pre>
        </div>
      </div>

      {/* PE 헤더 */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">PE 헤더</h2>
        <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
          {JSON.stringify(data.pe_headers, null, 2)}
        </pre>
      </section>

      {/* 메타데이터 */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">파일 메타데이터</h2>
        <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
          {JSON.stringify(data.get_metadata, null, 2)}
        </pre>
      </section>

      {/* 엔트로피 & 문자열 통계 */}
      <section className="mb-6 flex space-x-8">
        <div>
          <h2 className="text-lg font-semibold">파일 엔트로피</h2>
          <p className="mt-1">{data.file_entropy}</p>
        </div>
        <div className="flex-1">
          <h2 className="text-lg font-semibold">String Stats</h2>
          <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
            {JSON.stringify(data.string_stats, null, 2)}
          </pre>
        </div>
      </section>

      {/* MCP 문자열 통계 */}
      <section className="mb-6">
        <h2 className="text-lg font-semibold">MCP 문자열 통계</h2>
        <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">
          {JSON.stringify(data.mcp_strings, null, 2)}
        </pre>
      </section>

      {/* Summary & YARA 룰 */}
      <section className="mb-8">
        <h2 className="text-lg font-semibold mb-2">Summary &amp; YARA 룰</h2>
        <div className="grid grid-cols-2 gap-4">
          {/* Summary */}
          <div>
            <h3 className="font-semibold mb-1">Summary</h3>
            <ul className="list-decimal list-inside bg-white p-4 h-64 overflow-auto border border-blue-300 rounded">
              {data.summary.length > 0 ? (
                data.summary.map((line, idx) => <li key={idx}>{line}</li>)
              ) : (
                <li>요약 내용이 아직 없습니다.</li>
              )}
            </ul>
          </div>

          {/* YARA 룰 */}
          <div>
            <h3 className="font-semibold mb-1">YARA 룰</h3>
            <pre className="bg-white p-4 h-64 overflow-auto border border-blue-300 rounded whitespace-pre-wrap">
              {data.yara_rules || '// YARA 룰이 아직 생성되지 않았습니다.'}
            </pre>
          </div>
        </div>
      </section>
    </Layout>
  )
}
