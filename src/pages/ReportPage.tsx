// src/pages/ReportPage.tsx
import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import Layout from '../components/Layout'

export default function ReportPage() {
  const navigate = useNavigate()
  const [query, setQuery] = useState('')
  const [reports] = useState([
    'example1.exe',
    'malicious.dll',
    'trojan_sample.exe',
  ])

  const filtered = reports.filter((r) =>
    r.toLowerCase().includes(query.toLowerCase())
  )

  return (
    <Layout>
      {/* 검색 바 */}
      <div className="flex items-center border-b mb-6">
        <input
          type="text"
          placeholder="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="flex-1 bg-transparent border-0 focus:ring-0 focus:outline-none text-lg px-2"
        />
        <span className="px-2 text-xl">🔍</span>
      </div>

      {/* 리포트 리스트 */}
      <ul className="divide-y">
        {filtered.map((item, i) => (
          <li
            key={i}
            className="py-2 cursor-pointer hover:underline"
            onClick={() =>
              navigate('/report/detail', { state: { filename: item } })
            }
          >
            {i + 1}. {item}
          </li>
        ))}
      </ul>

      {/* 간단 챗봇 UI */}
      <div className="fixed bottom-4 right-4 w-64 border rounded-xl bg-white shadow-md p-2">
        <div className="h-24 overflow-y-auto text-sm">
          💬 챗봇 대화내용 표시
        </div>
        <div className="flex items-center mt-2">
          <input
            type="text"
            placeholder="메시지를 입력하세요"
            className="flex-1 px-2 py-1 border rounded-l text-sm focus:outline-none"
          />
          <button className="px-3 py-1 bg-blue-600 text-white rounded-r">
            ➤
          </button>
        </div>
      </div>
    </Layout>
  )
}
