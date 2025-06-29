import { useNavigate } from 'react-router-dom'

export default function Header() {
  const navigate = useNavigate()

  return (
    <header
      className="w-full bg-gray-300 border-b-2"
      style={{ borderColor: '#A3E635' }}
    >
      <div className="mx-auto max-w-5xl flex items-center justify-between px-8 py-4">
        {/* 왼쪽 로고 */}
        <h1
          className="text-[2rem] font-bold text-black cursor-pointer"
          onClick={() => navigate('/')}
        >
          YARAAI
        </h1>

        {/* 오른쪽 Report 버튼 */}
        <button
          onClick={() => navigate('/reports')}
          style={{
            border: '2px solid #A3E635',
            padding: '0.5rem 1rem',
          }}
          className="
            text-[1.5rem] font-medium text-gray-900
            bg-transparent rounded hover:bg-lime-50
          "
        >
          Report
        </button>
      </div>
    </header>
  )
}
