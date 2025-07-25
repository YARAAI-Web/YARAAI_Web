// src/pages/ReportDetailPage.tsx

import { useParams, useNavigate } from 'react-router-dom'
import { useEffect, useState } from 'react'
import axios from 'axios'
import Layout from '../components/Layout'

interface FullReport {
  get_metadata?: {
    md5?: string
    sha1?: string
    sha256?: string
  }
  virustotal?: {
    vhash?: string
    file_type?: string
    magic?: string
    file_size?: number
    analysis?: {
      detectiteasy?: { result: string }
      magika?: { result: string }
    }
    packer?: string
    trid?: Array<{ file_type: string; probability: number }>
  }
  pe_headers?: {
    format?: string
    entry_point?: string
    entry_point_name?: string
    sections?: Array<{ name: string }>
  }
  file_entropy?: number
  string_stats?: {
    total?: number
    avg_length?: number
    max_length?: number
  }
  summary?: string[]
  yara_rule?: string
  [key: string]: any
}

export default function ReportDetailPage() {
  const { filename } = useParams<{ filename: string }>()
  const navigate = useNavigate()

  const [report, setReport] = useState<FullReport | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  // GPT dynamic summary
  const [dynSummary, setDynSummary] = useState<string[]>([])
  const [dynLoading, setDynLoading] = useState(false)
  const [dynError, setDynError] = useState<string | null>(null)

  // fetch static report
  useEffect(() => {
    if (!filename) return
    axios
      .get<FullReport>(`http://localhost:8000/reports/${filename}`)
      .then((res) => setReport(res.data))
      .catch(() => setError('리포트를 불러오는 중 오류가 발생했습니다.'))
      .finally(() => setLoading(false))
  }, [filename])

  // fetch dynamic GPT summary
  useEffect(() => {
    if (!filename) return
    setDynLoading(true)
    const cleanName = filename.replace(/\.exe|\.dll/, '')
    fetch(`http://localhost:8000/api/dynamic-summary/${cleanName}`)
      .then((res) => res.json())
      .then((data) => setDynSummary(data))
      .catch(() => setDynError('요약 정보를 불러오지 못했습니다.'))
      .finally(() => setDynLoading(false))
  }, [filename])

  // download JSON
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
      <div className="max-w-5xl mx-auto px-8 mt-6 space-y-8">
        {/* Header */}
        <div className="flex justify-between items-center">
          <h2 className="text-2xl font-bold">{filename}</h2>
          <button
            onClick={downloadJson}
            className="bg-green-600 hover:bg-green-700 text-white font-semibold px-4 py-2 rounded"
          >
            Download JSON
          </button>
        </div>

        {/* ① Information */}
        <section>
          <h3 className="text-xl font-bold mb-4">① Information</h3>
          {report.summary && report.summary.length > 0 && (
            <pre className="whitespace-pre-wrap mb-6 text-sm leading-relaxed">
              {report.summary.join('\n')}
            </pre>
          )}
          <div className="border border-gray-300 rounded-lg p-4 text-sm space-y-1">
            <p>
              <strong>MD5:</strong> {report.get_metadata?.md5 ?? '—'}
            </p>
            <p>
              <strong>SHA-1:</strong> {report.get_metadata?.sha1 ?? '—'}
            </p>
            <p>
              <strong>SHA-256:</strong> {report.get_metadata?.sha256 ?? '—'}
            </p>
            <p>
              <strong>Vhash:</strong> {report.virustotal?.vhash ?? '—'}
            </p>
            <p>
              <strong>File type:</strong> {report.virustotal?.file_type ?? '—'}
            </p>
            <p>
              <strong>Magic:</strong> {report.virustotal?.magic ?? '—'}
            </p>
            <p>
              <strong>File size:</strong>{' '}
              {report.virustotal?.file_size?.toLocaleString() ?? '—'} bytes
            </p>
            <p>
              <strong>DetectItEasy:</strong>{' '}
              {report.virustotal?.analysis?.detectiteasy?.result ?? '—'}
            </p>
            <p>
              <strong>Magika:</strong>{' '}
              {report.virustotal?.analysis?.magika?.result ?? '—'}
            </p>
            <p>
              <strong>Packer:</strong> {report.virustotal?.packer ?? '—'}
            </p>
            <p>
              <strong>TrID 상위 3개:</strong>{' '}
              {report.virustotal?.trid
                ? report.virustotal.trid
                    .slice(0, 3)
                    .map((t) => `${t.file_type} (${t.probability}%)`)
                    .join(', ')
                : '—'}
            </p>
          </div>
        </section>

        {/* ② 정적 분석 */}
        <section>
          <h3 className="text-xl font-bold mb-4">② 정적 분석</h3>
          <div className="border border-gray-300 rounded-lg p-4 text-sm space-y-4">
            <div>
              <h4 className="font-semibold">PE 헤더 정보</h4>
              <p>
                <strong>- 형식:</strong> {report.pe_headers?.format ?? '—'}
              </p>
              <p>
                <strong>- Entry Point:</strong>{' '}
                {report.pe_headers?.entry_point ?? '—'}
              </p>
              <p>
                <strong>- Entry Point Name:</strong>{' '}
                {report.pe_headers?.entry_point_name ?? '—'}
              </p>
              <p>
                <strong>- 섹션 목록:</strong>{' '}
                {report.pe_headers?.sections?.map((s) => s.name).join(', ') ??
                  '—'}
              </p>
            </div>
            <div>
              <h4 className="font-semibold">문자열 (Strings)</h4>
              <p>
                <strong>- 총 문자열 수:</strong>{' '}
                {report.string_stats?.total ?? '—'}
              </p>
              <p>
                <strong>- 평균 길이:</strong>{' '}
                {report.string_stats?.avg_length ?? '—'}
              </p>
              <p>
                <strong>- 최대 길이:</strong>{' '}
                {report.string_stats?.max_length ?? '—'}
              </p>
            </div>
            <div>
              <h4 className="font-semibold">난독화 / 패킹</h4>
              <p>
                <strong>- 섹션 엔트로피 평균:</strong>{' '}
                {report.file_entropy?.toFixed(2) ?? '—'}
              </p>
            </div>
            <div>
              <h4 className="font-semibold">YARA 룰 매칭</h4>
              <pre className="bg-gray-100 p-2 rounded text-xs whitespace-pre-wrap">
                {report.yara_rule ?? '// YARA 룰이 없습니다.'}
              </pre>
            </div>
          </div>
        </section>

        {/* 🧠 GPT 동적 요약 */}
        <section>
          <h3 className="text-xl font-bold mb-4">🧠 GPT 분석 요약</h3>
          <div className="border border-gray-300 rounded-lg p-4 bg-gray-50 text-sm">
            {dynLoading ? (
              <p>요약 정보를 불러오는 중...</p>
            ) : dynError ? (
              <p className="text-red-500">{dynError}</p>
            ) : dynSummary.length === 0 ? (
              <p>요약 결과가 없습니다.</p>
            ) : (
              <ul className="list-disc list-inside space-y-1">
                {dynSummary.map((line, idx) => (
                  <li key={idx}>{line}</li>
                ))}
              </ul>
            )}
          </div>
        </section>

        {/* 뒤로 가기 */}
        <div className="flex justify-center">
          <button
            onClick={() => navigate('/report')}
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2 rounded-lg"
          >
            목록으로 돌아가기
          </button>
        </div>
      </div>
    </Layout>
  )
}
