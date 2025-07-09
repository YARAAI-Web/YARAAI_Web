import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import Layout from '../components/Layout'
import { FaSearch } from 'react-icons/fa'

export default function HistoryPage() {
  const navigate = useNavigate()
  const [query, setQuery] = useState('')
  const [reports, setReports] = useState<string[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    axios
      .get<{ reports: string[] }>('http://localhost:8000/reports')
      .then((res) => {
        // .exe, .dll 만 필터링
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
      {/* 검색창 */}
      <div className="mx-8 mt-4 flex justify-end">
        <div className="relative w-40">
          <input
            type="text"
            placeholder="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="w-full bg-transparent placeholder-gray-400 focus:outline-none text-lg pl-10 pb-2 border-0"
          />
          <FaSearch className="absolute top-1/2 -translate-y-1/2 right-[1px] w-5 h-5 text-gray-500" />
        </div>
      </div>
      <div
        className="mx-8 mt-4 border-b-2"
        style={{ borderColor: '#A3E635' }}
      />

      {/* 실행파일 리스트 */}
      <ul className="mx-8 mt-6 space-y-4">
        {filtered.map((item, idx) => (
          <li
            key={item}
            onClick={() => navigate(`/analysis/${encodeURIComponent(item)}`)}
            className="flex items-center cursor-pointer text-2xl py-2 border-b-2"
            style={{ borderColor: '#A3E635' }}
          >
            <span className="font-semibold mr-4">{idx + 1}.</span>
            <span className="flex-1">{item}</span>
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
