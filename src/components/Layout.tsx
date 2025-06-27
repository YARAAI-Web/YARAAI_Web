import type { ReactNode } from 'react'
import { useNavigate } from 'react-router-dom'

interface Props {
  children: ReactNode
}

export default function Layout({ children }: Props) {
  const navigate = useNavigate()

  return (
    <div className="flex flex-col min-h-screen bg-gray-300">
      {/* 헤더 */}
      <header className="flex-shrink-0 w-full bg-gray-300 border-b border-blue-600">
        <div className="max-w-5xl mx-auto flex items-center justify-between px-6 py-4">
          <h1
            className="text-3xl font-bold text-black cursor-pointer"
            onClick={() => navigate('/')}
          >
            YARAAI
          </h1>
          <button
            onClick={() => navigate('/reports')}
            className="px-4 py-2 bg-white text-black border border-blue-600 rounded hover:bg-blue-50"
          >
            Report
          </button>
        </div>
      </header>

      {/* 본문 */}
      <main className="flex-1 flex items-center justify-center">
        {children}
      </main>

      {/* 챗봇 버튼 */}
      <div className="fixed bottom-6 right-6">
        <button
          onClick={() => alert('챗봇 기능은 추후 구현 예정입니다')}
          className="w-14 h-14 bg-blue-600 text-white rounded-full shadow-lg flex items-center justify-center text-3xl hover:bg-blue-700"
          title="챗봇 열기"
        >
          💬
        </button>
      </div>
    </div>
  )
}
