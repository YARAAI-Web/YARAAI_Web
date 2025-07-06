// src/components/Header.tsx
import { useNavigate } from 'react-router-dom'
import Logo from '../assets/YARRAI_LOGO_2.png'

export default function Header() {
  const navigate = useNavigate()

  return (
    <header
      className="w-full border-b-2 bg-white"
      style={{ borderColor: '#A3E635' }}
    >
      <div className="mx-auto max-w-5xl flex items-center justify-between px-8 py-4">
        <img
          src={Logo}
          alt="YARAAI"
          onClick={() => navigate('/')}
          className="w-auto cursor-pointer"
          style={{ height: '5rem' }}
        />

        {/* History 버튼 */}
        <button
          onClick={() => navigate('/history')}
          className="text-[2rem] font-medium text-gray-900 bg-transparent rounded hover:bg-lime-50"
          style={{ border: '2px solid #A3E635', padding: '0.5rem 1rem' }}
        >
          History
        </button>
      </div>
    </header>
  )
}
