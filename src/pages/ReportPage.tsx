// src/pages/ReportPage.tsx
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import Layout from '../components/Layout'
import { FaSearch } from 'react-icons/fa'

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
      {/* (1) 검색창 (우측 정렬) */}
      <div className="mx-8 mt-4 flex justify-end">
        <div className="relative w-40">
          <input
            type="text"
            placeholder="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="
              w-full
              bg-transparent placeholder-gray-400
              focus:outline-none text-lg
              pl-10 pb-2
              border-0
            "
          />
          <FaSearch className="absolute top-1/2 -translate-y-1/2  right-[1px] w-5 h-5 text-gray-500" />
        </div>
      </div>

      {/* (2) 검색창 바로 아래 실선 (연두색) */}
      <div
        className="mx-8 mt-4 border-b-2"
        style={{ borderColor: '#A3E635' }}
      />

      {/* (3) REPORT LIST */}
      <ul className="mx-8 mt-6 space-y-4">
        {filtered.map((item, idx) => (
          <li
            key={item}
            onClick={() => navigate(`/reports/${encodeURIComponent(item)}`)}
            className="flex items-center justify-between cursor-pointer text-2xl py-2 border-b-2"
            style={{ borderColor: '#A3E635' }}
          >
            <span className="font-semibold">{idx + 1}.</span>
            <span className="flex-1 mx-4">{item}</span>
          </li>
        ))}

        {filtered.length === 0 && (
          <li className="py-8 text-center text-gray-500 text-2xl">
            검색 결과가 없습니다.
          </li>
        )}
      </ul>
    </Layout>
  )
}
