import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import axios from 'axios'
import GPTSection from '../components/GPTSection'

interface AnalysisResult {
  get_metadata: {
    module: string
    md5: string
    sha256: string
    sha1?: string
    format?: string
    filesize?: string
  }
  summary?: string[]
  yara_rules?: string
  tags?: string[]
  report_id?: string
  submitted_at?: string
}

const SECTIONS = [
  '❶ 정적 분석 결과파일 구조',
  '❷ 동적 분석 결과 (Behavioral) 프로세스 행위',
  '❸ Call Graph → 이거 어떻게 할지 미정(코드를 짜긴함)',
  '❹ MITRE ATT&CK 매핑 / ATT&CK ID기법',
  '❺ Artifacts 덤프 파일',
  '❻ 인사이트/위협 및 위험 요약',
  '❼ CWE 기반 보안 권고사항 (Recommendations)',
  '❽ 부록 (분석 JSON)',
]

export default function AnalysisPage() {
  const { filename: rawFilename } = useParams<{ filename: string }>()
  const navigate = useNavigate()

  const [filename, setFilename] = useState<string | null>(null)
  const [data, setData] = useState<AnalysisResult | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [currentSection, setCurrentSection] = useState(0)

  useEffect(() => {
    if (!rawFilename) {
      navigate('/')
      return
    }
    setFilename(rawFilename)
  }, [rawFilename, navigate])

  useEffect(() => {
    if (!filename) return
    axios
      .get<AnalysisResult>(`http://localhost:8000/reports/${filename}`)
      .then(res => setData(res.data))
      .catch(err => setError(err.response?.data?.detail || err.message))
      .finally(() => setLoading(false))
  }, [filename])

  const handleDownloadJSON = () => {
    if (!data || !filename) return
    const blob = new Blob([JSON.stringify(data, null, 2)], {
      type: 'application/json',
    })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${filename}.json`
    a.click()
    URL.revokeObjectURL(url)
  }

  if (loading) return <div className="p-8 text-center">로딩 중…</div>
  if (error) return <div className="p-8 text-red-500">오류 발생: {error}</div>
  if (!data || !filename) return <div className="p-8">분석 결과를 찾을 수 없습니다.</div>

  const metadataForGPT = {
    module: data.get_metadata.module,
    hash: data.get_metadata.sha256,
    submittedAt: data.submitted_at || new Date().toLocaleString(),
    md5: data.get_metadata.md5,
    sha1: data.get_metadata.sha1,
    fileType: data.get_metadata.format || '',
    fileSize: data.get_metadata.filesize || '',
  }

  return (
    <div className="flex flex-col min-h-screen bg-white">
      {/* 상단 요약 박스 */}
      <div className="px-8 pt-8 pb-2">
        <div className="max-w-5xl mx-auto flex bg-white border shadow rounded-lg p-4 justify-between items-start">
          <div className="w-[200px] bg-orange-500 text-white font-bold text-center flex items-center justify-center text-lg rounded-md shadow-inner h-full">
            Likely Malicious
          </div>
          <div className="flex-1 pl-6 space-y-2">
            <div className="grid grid-cols-2 gap-x-8 gap-y-1 text-sm text-gray-800">
              <div><strong>Name:</strong> {filename}</div>
              <div><strong>SHA-256:</strong> {data.get_metadata.sha256}</div>
              <div><strong>Report ID:</strong> {data.report_id || '—'}</div>
              <div><strong>Submission Date:</strong> {data.submitted_at || '—'}</div>
            </div>
            <div className="flex flex-wrap gap-2 pt-2">
              {(data.tags || []).map((tag, i) => (
                <span
                  key={i}
                  className="px-3 py-1 text-xs rounded border bg-gray-100 text-gray-700"
                >
                  {tag}
                </span>
              ))}
            </div>
          </div>
          <button
            onClick={handleDownloadJSON}
            className="ml-4 mt-1 bg-[#A0C3FF] hover:bg-[#B8D4FF] text-[#0F3ADA] font-semibold px-4 py-2 rounded shadow"
          >
            ⬇ JSON
          </button>
        </div>
      </div>

      {/* 본문: 좌측 네비 + 우측 콘텐츠 */}
      <div className="flex flex-1 px-8 pb-8 gap-6">
        {/* 좌측 섹션 네비 */}
        <div className="w-[260px] bg-gray-50 border-r p-4 space-y-2">
          {SECTIONS.map((label, idx) => (
            <div
              key={idx}
              onClick={() => setCurrentSection(idx)}
              className={`cursor-pointer h-[48px] flex items-center px-4 border-l-4 text-sm font-medium transition-all rounded-md ${
                currentSection === idx
                  ? 'bg-white border-[#0F3ADA] text-[#0F3ADA] shadow-sm'
                  : 'bg-[#6DA2F9] border-transparent text-white hover:bg-[#2F5BFD]'
              }`}
            >
              {label}
            </div>
          ))}
        </div>

        {/* 우측 콘텐츠 */}
        <div className="flex-1 overflow-auto">
          <section className="bg-white shadow rounded-xl border-l-4 border-[#0F3ADA] p-4 h-full">
            <h2 className="text-xl font-bold text-[#0F3ADA] mb-4">
              {SECTIONS[currentSection]}
            </h2>

            {currentSection === 2 ? (
              <iframe
                key={`callgraph-${filename}`}
                src={`http://localhost:8000/static/callgraphs/${filename.replace(/\.exe$/i, '')}.html`}
                title="Call Graph"
                className="w-full h-[800px] border-none rounded"
                sandbox="allow-scripts allow-same-origin"
              />
            ) : (
              <GPTSection
                sectionId={currentSection + 1}
                metadata={metadataForGPT}
              />
            )}
          </section>
        </div>
      </div>
    </div>
  )
}
