// src/pages/ReportDetailPage.tsx
import { useLocation } from 'react-router-dom'
import Layout from '../components/Layout'

export default function ReportDetailPage() {
  const { state } = useLocation() as { state: { filename: string } }
  const filename = state?.filename ?? 'Unknown File'

  // TODO: 실제 데이터 fetch 예정
  const dummySummary =
    '이 파일은 외부 서버와 통신하며, 악성 행위를 포함할 가능성이 높습니다.'
  const dummyYara = `rule suspicious_behavior {
  meta:
    author = "yarai"
    description = "sample yara rule"
  strings:
    $a = "malware"
  condition:
    $a
}`

  return (
    <Layout>
      <div className="w-full max-w-5xl mx-auto px-8 mt-6">
        <h2 className="text-2xl font-bold mb-4">{filename}</h2>

        <p className="text-lg mb-2">Summary</p>
        <div className="grid grid-cols-2 gap-6">
          {/* Summary 박스 */}
          <div
            className="border-2 rounded-lg bg-white p-4"
            style={{ borderColor: '#A3E635' }}
          >
            <p className="text-sm whitespace-pre-line">{dummySummary}</p>
          </div>

          {/* YARA 룰 박스 */}
          <div
            className="border-2 rounded-lg bg-white p-4"
            style={{ borderColor: '#A3E635' }}
          >
            <pre className="text-sm whitespace-pre-wrap">{dummyYara}</pre>
          </div>
        </div>
      </div>
    </Layout>
  )
}
