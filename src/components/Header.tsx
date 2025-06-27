// src/components/Header.tsx
import React from 'react'

export default function Header() {
  return (
    <header className="flex items-center justify-between px-8 py-4 border-b-2 border-blue-600 bg-gray-100">
      <h1 className="text-2xl font-bold">YARAAI</h1>
      <button className="px-4 py-2 bg-white rounded shadow hover:bg-gray-50">
        Report
      </button>
    </header>
  )
}
