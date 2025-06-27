import type { ReactNode } from 'react'

interface Props {
  children: ReactNode
}

export default function Layout({ children }: Props) {
  return (
    <div className="flex flex-col min-h-screen bg-gray-300">
      {/* 이제 헤더는 여기 없습니다! */}

      {/* Main content */}
      <main className="flex-1 flex flex-col items-center justify-start pt-[30px] relative">
        {children}

        {/* Chatbot 버튼 */}
        <button
          onClick={() => alert('챗봇 기능은 추후 구현 예정입니다')}
          style={{
            position: 'fixed',
            bottom: '48px',
            right: '48px',
            width: '56px',
            height: '56px',
            zIndex: 999,
            border: '2px solid #A3E635', // ← 테두리만 연두색
            backgroundColor: 'white', // ← 배경은 흰색으로 둡니다
          }}
          className="
          text-gray-600 rounded-full flex items-center justify-center text-2xl
          hover:bg-gray-100
        "
          title="챗봇 열기"
        >
          💬
        </button>
      </main>
    </div>
  )
}
