// src/components/Header.tsx
import React from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import Logo from '../assets/YARRAI_LOGO.png'

export default function Header() {
  const navigate = useNavigate()
  const location = useLocation()
  const isHistory = location.pathname === '/history'

  return (
    <header className="w-full bg-white">
      {/* ──── 로고 + 히스토리 버튼 컨테이너 ──── */}
      <div className="mx-auto max-w-5xl flex items-center justify-between px-[10px] py-4">
        <img
          src={Logo}
          alt="YARAAI"
          onClick={() => navigate('/')}
          className="cursor-pointer"
          style={{ height: '3.5rem', width: 'auto' }}
        />
        <button
          type="button"
          onClick={() => navigate('/history')}
          className="
            mr-[30px]
            relative
            text-[1.2rem] font-medium text-gray-900
            bg-transparent border-0 appearance-none p-0
            hover:bg-lime-50 transition cursor-pointer
            focus:outline-none focus:ring-0
          "
        >
          History
          {isHistory && (
            <span
              className={`
                absolute
                bottom-0           /* 버튼 바로 아래 */
                left-1/2
                -translate-x-1/2
                w-12
                border-b-2
                border-[#1b65fe]
              `}
            />
          )}
        </button>
      </div>

      {/* ──── 분리된 밑줄 (라인) ──── */}
      <div
        className="mx-auto max-w-5xl"
        style={{
          borderBottom: '1.2px solid rgba(0,0,0,0.15)',
          marginTop: '12px', // ← 이 값을 조절해서 라인 위치만 내림
        }}
      />
    </header>
  )
}
