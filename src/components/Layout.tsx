import type { ReactNode } from 'react'
import { Link, useNavigate } from 'react-router-dom'

interface Props {
  children: ReactNode
}

export default function Layout({ children }: Props) {
  const navigate = useNavigate()
  return (
    <div className="flex flex-col min-h-screen bg-gray-300">
      {/* Header */}
      <header className="w-full bg-gray-300 border-b-2 border-blue-600">
        <div className="mx-auto max-w-5xl flex items-center justify-between px-8 py-4">
          <h1
            className="text-[2rem] font-bold text-black cursor-pointer"
            onClick={() => navigate('/')}
          >
            YARAAI
          </h1>
          <div className="flex items-center space-x-2">
            <span className="h-[1.5rem] border-l-2 border-blue-600" />
            <Link
              to="/reports"
              className="text-[1rem] text-gray-900 hover:underline"
            >
              Report
            </Link>
            <span className="h-[1.5rem] border-l-2 border-blue-600" />
          </div>
        </div>
      </header>

      {/* Main: 헤더 바로 아래부터 시작 (pt-20 = 80px) */}
      <main className="flex-1 flex flex-col items-center justify-start pt-20 relative">
        {children}

        {/* Chatbot 버튼 (우하단 고정) */}
        <button
          onClick={() => alert('챗봇 기능은 추후 구현 예정입니다')}
          style={{
            position: 'fixed',
            bottom: '48px',
            right: '48px',
            width: '56px',
            height: '56px',
            zIndex: 999,
          }}
          className="bg-blue-600 text-white rounded-full shadow-lg flex items-center justify-center text-2xl hover:bg-blue-700"
          title="챗봇 열기"
        >
          💬
        </button>
      </main>
    </div>
  )
}
