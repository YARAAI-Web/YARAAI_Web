import { useNavigate } from 'react-router-dom'
import Layout from '../components/Layout'

export default function ReportPage() {
  const navigate = useNavigate()

  return (
    <Layout>
      <div className="flex flex-col items-center justify-center h-full p-8">
        <h2 className="text-3xl font-bold mb-4">🚧 Report Page (Test)</h2>
        <p className="mb-6">여기에 실제 보고서 요약 UI를 넣으시면 됩니다.</p>
        <button
          onClick={() => navigate('/history')}
          className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2 rounded"
        >
          ← History로 돌아가기
        </button>
      </div>
    </Layout>
  )
}
