// src/components/Header.tsx
import React from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import Logo from '../assets/YARRAI_LOGO.png'

export default function Header() {
  const navigate = useNavigate()
  const location = useLocation()
  const isHistory = location.pathname === '/history'

  return (
    <header
      className="w-full border-b-1 bg-white relative"
      style={{ borderColor: 'rgba(0, 0, 0, 0.15)', marginTop: '10px' }}
    >
      <div className="mx-auto max-w-5xl flex items-center justify-between relative px-8 py-4">
        <img
          src={Logo}
          alt="YARAAI"
          onClick={() => navigate('/')}
          className="cursor-pointer"
          style={{ height: '3.5rem', width: 'auto' }}
        />

        {/* History 버튼 */}
        <button
          type="button"
          onClick={() => navigate('/history')}
          className="
            relative
            text-[1.2rem] font-medium text-gray-900
            bg-transparent border-0 appearance-none p-0
            hover:bg-lime-50 transition cursor-pointer
            focus:outline-none focus:ring-0
          "
        >
          History
        </button>
      </div>
    </header>
  )
}
