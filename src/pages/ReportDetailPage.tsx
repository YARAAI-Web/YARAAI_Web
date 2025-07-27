import { useParams, useNavigate } from 'react-router-dom'
import { useEffect, useState } from 'react'
import axios from 'axios'
import Layout from '../components/Layout'

interface FullReport {
  get_metadata?: Record<string, any>
  virustotal?: Record<string, any>
  pe_headers?: Record<string, any>
  file_entropy?: number
  string_stats?: Record<string, any>
  yara_rule?: string
  summary?: string[]
  [section: string]: any
}

export default function ReportDetailPage() {
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
      <div className="max-w-5xl mx-auto px-8 mt-6">
        <h2 className="text-2xl font-bold mb-4">① Information</h2>

        {/* ✅ 요약 설명 - AnalysisPage와 동일 스타일 적용 */}
        {report.summary && report.summary.length > 0 && (
          <pre
            className="whitespace-pre-wrap mb-6 text-sm"
            style={{
              fontFamily: 'semibold',
              fontWeight: 350,
              lineHeight: '1.6',
            }}
          >
            {report.summary.join('\n\n')}
          </pre>
        )}

        {/* 기본 정보 테이블 */}
        <div className="border border-gray-300 rounded-lg p-4 text-sm leading-relaxed space-y-1">
          <p>
            <strong>MD5:</strong> {report.get_metadata?.md5 || '—'}
          </p>
          <p>
            <strong>SHA-1:</strong> {report.get_metadata?.sha1 || '—'}
          </p>
          <p>
            <strong>SHA-256:</strong> {report.get_metadata?.sha256 || '—'}
          </p>
          <p>
            <strong>Vhash:</strong> {report.virustotal?.vhash || '—'}
          </p>
          <p>
            <strong>File type:</strong> {report.virustotal?.file_type || '—'}
          </p>
          <p>
            <strong>Magic:</strong> {report.virustotal?.magic || '—'}
          </p>
          <p>
            <strong>File size:</strong>{' '}
            {report.virustotal?.file_size?.toLocaleString() || '—'} bytes
          </p>
          <p>
            <strong>DetectItEasy:</strong>{' '}
            {report.virustotal?.analysis?.detectiteasy?.result || '—'}
          </p>
          <p>
            <strong>Magika:</strong>{' '}
            {report.virustotal?.analysis?.magika?.result || '—'}
          </p>
          <p>
            <strong>Packer:</strong> {report.virustotal?.packer || '—'}
          </p>
          <p>
            <strong>TrID 상위 3개:</strong>{' '}
            {report.virustotal?.trid
              ? report.virustotal.trid
                  .slice(0, 3)
                  .map((t: any) => `${t.file_type} (${t.probability}%)`)
                  .join(', ')
              : '—'}
          </p>
        </div>

        <h2 className="text-2xl font-bold mt-10 mb-4">② 정적 분석</h2>

        <div className="border border-gray-300 rounded-lg p-4 text-sm space-y-2">
          <h4 className="font-semibold">PE 헤더 정보</h4>
          <p>
            <strong>- 형식:</strong> {report.pe_headers?.format || '—'}
          </p>
          <p>
            <strong>- 크기:</strong>{' '}
            {report.virustotal?.file_size?.toLocaleString() || '—'} bytes
          </p>
          <p>
            <strong>- 섹션 목록:</strong>{' '}
            {report.pe_headers?.sections?.map((s: any) => s.name).join(', ') ||
              '—'}
          </p>

          <h4 className="font-semibold mt-4">문자열 (Strings)</h4>
          <p>- 총 문자열 수: {report.string_stats?.total || '—'}</p>
          <p>- 평균 길이: {report.string_stats?.avg_length || '—'}</p>
          <p>- 최대 길이: {report.string_stats?.max_length || '—'}</p>

          <h4 className="font-semibold mt-4">Entry Point 정보</h4>
          <p>- Entry Point Address: {report.pe_headers?.entry_point || '—'}</p>
          <p>
            - Entry Point Name: {report.pe_headers?.entry_point_name || '—'}
          </p>

          <h4 className="font-semibold mt-4">난독화 및 패킹 여부</h4>
          <p>- 섹션 엔트로피 평균: {report.file_entropy?.toFixed(2) || '—'}</p>
          <p>- 패커 탐지 정보: 추후 반영 필요</p>

          <h4 className="font-semibold mt-4">YARA 룰 매칭</h4>
          <pre
            className="bg-gray-100 p-2 rounded text-xs whitespace-pre-wrap"
            style={{
              fontFamily: 'semibold',
              fontWeight: 350,
              lineHeight: '1.6',
            }}
          >
            {report.yara_rule || '// YARA 룰 없음'}
          </pre>
        </div>

        <div className="mt-8 flex justify-center">
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
