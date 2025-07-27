// src/pages/HistoryPage.tsx
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { FaSearch } from 'react-icons/fa'
import Layout from '../components/Layout'

export default function HistoryPage() {
  const navigate = useNavigate()
  const [query, setQuery] = useState('')
  const [reports, setReports] = useState<string[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [hoveredIdx, setHoveredIdx] = useState<number | null>(null)

  useEffect(() => {
    axios
      .get<{ reports: string[] }>('http://localhost:8000/reports')
      .then((res) => {
        const exes = res.data.reports.filter((f) =>
          ['.exe', '.dll'].includes(f.slice(f.lastIndexOf('.')).toLowerCase())
        )
        setReports(exes)
      })
      .catch(() => setError('리포트 목록을 불러오는 중 오류가 발생했습니다.'))
      .finally(() => setLoading(false))
  }, [])

  const filtered = reports.filter((r) =>
    r.toLowerCase().includes(query.toLowerCase())
  )

  if (loading)
    return (
      <Layout>
        <p className="p-8 text-center">로딩 중…</p>
      </Layout>
    )
  if (error)
    return (
      <Layout>
        <p className="p-8 text-red-500">{error}</p>
      </Layout>
    )

  return (
    <Layout>
      <div className="mx-auto max-w-5xl px-8 py-6 space-y-4 mt-[10px]">
        {/* 제목 + 검색창 */}
        <div className="space-y-2">
          {/* Reports 제목 중앙 정렬 */}
          <div className="w-full text-center ">
            <h1 className="relative -top-[5px] text-2xl font-bold uppercase">
              Reports
            </h1>
          </div>
          {/* 검색창 오른쪽 정렬 */}
          <div className="flex justify-end">
            <div className="relative mr-[60px]">
              <input
                type="text"
                placeholder="Search"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                className="
                  w-full
                  h-12
                  rounded-full
                  border border-[rgba(0,0,0,0.15)]
                  bg-[#F2F2F7]
                  py-[10px] px-[4px]
                  pl-[50px]
                  text-base
                  placeholder-gray-400
                  focus:outline-none focus:ring-2 focus:ring-blue-300
                "
              />
              <FaSearch className="absolute top-1/2 left-4 -translate-y-1/2 text-gray-500 w-[50px]" />
            </div>
          </div>
        </div>

        {/* 리스트 컨테이너 (검색창과 겹치지 않도록 아래로 살짝 이동) */}
        <div className="mt-[10px] rounded-[10px] border border-[rgba(0,0,0,0.15)] overflow-hidden">
          {/* 헤더 */}
          <div className="flex bg-[#F2F2F7] px-[15px] py-[15px] font-medium text-gray-700">
            <span className="flex-1">File Name</span>
          </div>
          {/* 바디 */}
          <div className="divide-y divide-[rgba(0,0,0,0.15)]">
            {filtered.map((filename, idx) => (
              <div
                key={filename}
                onClick={() =>
                  navigate(`/analysis/${encodeURIComponent(filename)}`)
                }
                onMouseEnter={() => setHoveredIdx(idx)}
                onMouseLeave={() => setHoveredIdx(null)}
                style={{
                  backgroundColor: hoveredIdx === idx ? '#F2F2F7' : 'white',
                }}
                className="flex items-center px-[15px] py-[5px] cursor-pointer transition-colors"
              >
                <span className="flex-1 text-sm break-all">
                  {idx + 1}. {filename}
                </span>
              </div>
            ))}
            {filtered.length === 0 && (
              <div className="px-[10px] py-6 text-center text-gray-500">
                검색 결과가 없습니다.
              </div>
            )}
          </div>
        </div>
      </div>
    </Layout>
  )
}
