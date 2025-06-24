import type { ReactNode } from 'react'
import { useNavigate } from 'react-router-dom'

interface Props {
  children: ReactNode
}

export default function Layout({ children }: Props) {
  const navigate = useNavigate()

  return (
    <div className="flex flex-col min-h-screen bg-[#f4f7fc]">
      <header className="w-full flex items-center justify-between p-4 bg-white border-b">
        <h1
          className="text-xl font-semibold cursor-pointer"
          onClick={() => navigate('/')}
        >
          YARAAI
        </h1>
        <nav>
          <button
            onClick={() => navigate('/report')}
            className="text-gray-700 hover:underline"
          >
            Report
          </button>
        </nav>
      </header>
      <main className="flex-1 p-6">{children}</main>
    </div>
  )
}
