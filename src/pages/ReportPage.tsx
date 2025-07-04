// src/pages/ReportPage.tsx
import { useEffect, useState } from 'react'
import { useParams, Navigate } from 'react-router-dom'
import GPTSection from '../components/GPTSection'
import type { Metadata, AnalysisJson } from '../api/report'

export default function ReportPage() {
  const { filename } = useParams<{ filename: string }>()
  const [generatedAt] = useState(() => new Date().toLocaleString())
  const [metadata, setMetadata] = useState<Metadata | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (!filename) return

    fetch(`/reports/${filename}`)
      .then((res) => {
        if (!res.ok) throw new Error(`Report not found (${res.status})`)
        return res.json() as Promise<AnalysisJson>
      })
      .then((json) => {
        const m = json.get_metadata

        let fileType = m.format ?? ''
        if (!fileType && m.module.includes('.')) {
          fileType = m.module.split('.').pop() || ''
        }

        let sizeBytes =
          typeof m.size === 'number' ? m.size : parseInt(m.filesize || '0', 16)
        const fileSizeKB = (sizeBytes / 1024).toFixed(1)

        setMetadata({
          module: m.module,
          hash: m.sha256,
          submittedAt: generatedAt,
          md5: m.md5,
          sha1: m.sha1,
          fileType,
          fileSize: `${fileSizeKB} KB`,
        })
      })
      .catch((e) => setError((e as Error).message))
      .finally(() => setLoading(false))
  }, [filename, generatedAt])

  if (!filename) return <Navigate to="/" replace />
  if (loading) return <p className="p-8">메타데이터 로딩 중…</p>
  if (error) return <p className="p-8 text-red-600">에러: {error}</p>
  if (!metadata) return null

  const sections = [
    { id: 1, title: '정적 분석 결과 구조' },
    { id: 2, title: '동적 분석 결과 (Behavioral) 프로세스 행위' },
    { id: 3, title: 'Call Graph' },
    { id: 4, title: 'MITRE ATT&CK 매핑' },
    { id: 5, title: 'Artifacts 덤프 파일' },
    { id: 6, title: '인사이트 및 위협 요약' },
    { id: 7, title: '보안 권고 사항' },
    { id: 8, title: '부록 (분석 JSON)' },
  ]

  return (
    <div className="flex flex-col items-center bg-gray-50 py-8 px-4">
      <div className="w-full max-w-3xl bg-white shadow-lg rounded-2xl overflow-hidden">
        <header className="px-8 py-6 border-b border-gray-200">
          <h1 className="text-3xl font-bold">Malware Analysis Report</h1>
        </header>
        <main className="px-8 py-6 space-y-12">
          <section>
            <h2 className="text-lg font-semibold mb-2">
              실행 파일명:{' '}
              <span className="font-medium">{metadata.module}</span>
            </h2>
          </section>
          <section>
            <h2 className="text-lg font-semibold mb-2">
              Sample Metadata{' '}
              <span className="text-gray-500">(샘플 기본 정보)</span>
            </h2>
            <ul className="ml-6 list-disc text-gray-600 space-y-1">
              <li>제출 일시: {metadata.submittedAt}</li>
              <li>Hash: {metadata.hash}</li>
              <li>
                파일 형식: {metadata.fileType || 'N/A'}, 크기:{' '}
                {metadata.fileSize}
              </li>
              <li>
                MD5: {metadata.md5}
                {metadata.sha1 ? `, SHA-1: ${metadata.sha1}` : null}
              </li>
            </ul>
          </section>

          {sections.map(({ id, title }) => (
            <section key={id}>
              <h3 className="text-xl font-semibold mb-4">
                {id}. {title}
              </h3>
              <GPTSection sectionId={id} metadata={metadata} />
            </section>
          ))}
        </main>
      </div>
    </div>
  )
}
