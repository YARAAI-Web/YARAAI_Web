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
      <div className="mt-6">
        <h2 className="text-2xl font-bold mb-2">{filename}</h2>
        <p className="text-lg mb-4">Summary</p>

        <div className="grid grid-cols-2 gap-4">
          <div className="border p-4 bg-white">
            <p className="text-sm whitespace-pre-line">{dummySummary}</p>
          </div>
          <div className="border p-4 bg-white">
            <pre className="text-sm whitespace-pre-wrap">{dummyYara}</pre>
          </div>
        </div>
      </div>

      {/* 챗봇 아이콘 */}
      <div className="fixed bottom-4 right-4">
        <button
          onClick={() => alert('챗봇 연동 예정')}
          className="bg-blue-800 text-white w-12 h-12 rounded-full shadow-lg flex items-center justify-center text-2xl"
        >
          💬
        </button>
      </div>
    </Layout>
  )
}
