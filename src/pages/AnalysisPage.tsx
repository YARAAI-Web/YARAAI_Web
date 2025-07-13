// AnalysisPage.tsx
import { useEffect, useState, useRef } from 'react'
import { useParams, useNavigate, useLocation } from 'react-router-dom'
import axios from 'axios'
import { saveAs } from 'file-saver'

interface AnalysisResult {
  get_metadata: {
    module: string
    md5: string
    sha256: string
    sha1?: string
    format?: string
    filesize?: string
  }
  get_current_address: string
  get_current_function: Record<string, any>
  get_entry_points: any[]
  file_entropy: number
  string_stats: Record<string, any>
  pe_headers: Record<string, any>
  c_code: string[]
  h_code: string[]
  virustotal: Record<string, any>
  yara_rule: string
  suricata_rule: string
  tags?: string[]
}

const SECTIONS = [
  '❶ 정적 분석 결과파일 구조',
  '❷ 동적 분석 결과 (Behavioral) 프로세스 행위',
  '❸ Call Graph → 인터랙티브 그래프',
  '❹ MITRE ATT&CK 매핑 / ATT&CK ID기법',
  '❺ Artifacts 덤프 파일',
  '❻ 인사이트/위협 및 위험 요약',
  '❼ CWE 기반 보안 권고사항 (Recommendations)',
]

export default function AnalysisPage() {
  const { filename: rawFilename } = useParams<{ filename: string }>()
  const navigate = useNavigate()
  const location = useLocation() as any

  const [filename, setFilename] = useState<string | null>(null)
  const [data, setData] = useState<AnalysisResult | null>(null)
  const [submissionDate, setSubmissionDate] = useState<string>('')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [currentSection, setCurrentSection] = useState(0)
  const [allTexts, setAllTexts] = useState<string[]>(
    Array(SECTIONS.length).fill('로딩 중…')
  )
  const htmlRef = useRef<HTMLDivElement>(null)

  // 1) filename 초기화
  useEffect(() => {
    if (!rawFilename) {
      navigate('/')
      return
    }
    setFilename(rawFilename)
  }, [rawFilename, navigate])

  // 2) 메타 + GPT 섹션 호출 또는 캐시/History state 사용
  useEffect(() => {
    if (!filename) return
    setLoading(true)

    // baseName, storage keys
    const baseName = filename.replace(/\.[^.]+$/i, '')
    const keySections = `yaraai_sections_${baseName}`
    const keyDate = `yaraai_date_${baseName}`

    // 2-0) History state가 있으면 우선 사용
    const histData: AnalysisResult | undefined = location.state?.data
    const histSecs: string[] | undefined = location.state?.sections
    const histDate: string | undefined = location.state?.date
    if (histData && histSecs) {
      setData(histData)
      setAllTexts(histSecs)
      setSubmissionDate(histDate || new Date().toLocaleString())
      setLoading(false)
      return
    }

    // 2-1) sessionStorage 캐시 확인
    const savedSecs = sessionStorage.getItem(keySections)
    const savedDate = sessionStorage.getItem(keyDate)
    if (savedSecs) {
      setAllTexts(JSON.parse(savedSecs))
      // 메타는 캐시하지 않으므로 data는 새로 fetch하게 됩니다
      setSubmissionDate(savedDate || new Date().toLocaleString())
      setLoading(false)
      return
    }

    // 2-2) 캐시 없으면 서버에서 메타 + GPT 섹션 호출
    let fetchedMeta: AnalysisResult
    let nowStr = new Date().toLocaleString()
    axios
      .get<AnalysisResult>(`/reports/${filename}`)
      .then((res) => {
        fetchedMeta = res.data
        setData(res.data)
        nowStr = new Date().toLocaleString()
        setSubmissionDate(nowStr)

        // Promise.all 로 7개 섹션 비동기 호출
        return Promise.all(
          SECTIONS.map((_, idx) => {
            if (idx === 2) {
              // Call Graph 섹션은 HTML iframe로 대체
              return Promise.resolve('(Call Graph)')
            }
            return axios
              .post<{ text: string }>('/api/section', {
                sectionId: idx + 1,
<<<<<<< HEAD
                filename: filename,
=======
                filename: filename
>>>>>>> 5c2aeb67d28118b0e4ebc62e658b0f936d6117c6
              })
              .then((r) => r.data.text)
              .catch(() => '(불러오기 실패)')
          })
        )
      })
      .then((texts) => {
        setAllTexts(texts)
        // 2-3) 호출 완료 후 세션 스토리지에 저장
        sessionStorage.setItem(keySections, JSON.stringify(texts))
        sessionStorage.setItem(keyDate, nowStr)
      })
      .catch((err) => {
        setError(err.response?.data?.detail || err.message)
      })
      .finally(() => {
        setLoading(false)
      })
  }, [filename, location.state])

  // 로딩/에러/없음 처리
  if (loading) return <div className="p-8 text-center">로딩 중…</div>
  if (error) return <div className="p-8 text-red-500">오류 발생: {error}</div>
  if (!data || !filename)
    return <div className="p-8">분석 결과를 찾을 수 없습니다.</div>

  const baseName = filename.replace(/\.[^.]+$/i, '')

  // ▼ 다운로드 함수들
  const downloadJSON = () => {
    const {
      get_metadata,
      get_current_address,
      get_current_function,
      get_entry_points,
      file_entropy,
      string_stats,
      pe_headers,
      c_code,
      h_code,
      virustotal,
    } = data
    const filtered = {
      get_metadata,
      get_current_address,
      get_current_function,
      get_entry_points,
      file_entropy,
      string_stats,
      pe_headers,
      c_code,
      h_code,
      virustotal,
    }
    const blob = new Blob([JSON.stringify(filtered, null, 2)], {
      type: 'application/json',
    })
    saveAs(blob, `${baseName}.json`)
  }
  const downloadHTML = () => {
    if (!htmlRef.current) return
    const html = `<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"/><title>보고서 - ${baseName}</title><style>body{font-family:sans-serif;padding:20px}.header{border:2px solid #000;padding:10px;display:flex;justify-content:space-between;margin-bottom:20px}h2{color:#0F3ADA;margin-top:30px}.section{margin-bottom:20px}.iframe-container{border:1px solid #ccc;height:500px}pre{white-space:pre-wrap}</style></head><body>${htmlRef.current.innerHTML}</body></html>`
    const blob = new Blob([html], { type: 'text/html' })
    saveAs(blob, `${baseName}.html`)
  }
  const downloadSuricataJSON = () => {
    const url = `/meta_json/${baseName}_suricata.json`
    const a = document.createElement('a')
    a.href = url
    a.download = `${baseName}_suricata.json`
    a.click()
  }

  return (
    <>
      {/* Off-screen HTML export */}
      <div
        ref={htmlRef}
        style={{ position: 'absolute', top: -9999, left: -9999, width: 800 }}
      >
        <div className="header">
          <div>
            <strong>Name:</strong> {filename}
          </div>
          <div>
            <strong>SHA-256:</strong> {data.get_metadata.sha256}
          </div>
          <div>
            <strong>Submission Date:</strong> {submissionDate}
          </div>
        </div>
        {SECTIONS.map((title, idx) => (
          <div className="section" key={idx}>
            <h2>{title}</h2>
            {idx === 2 ? (
              <div className="iframe-container">
                <iframe
                  src={`/static/callgraphs/${baseName}.html`}
                  style={{ width: '100%', height: '100%', border: 'none' }}
                  sandbox="allow-scripts allow-same-origin"
                />
              </div>
            ) : (
              <pre>{allTexts[idx]}</pre>
            )}
          </div>
        ))}
      </div>

      {/* Screen UI */}
      <div className="flex flex-col min-h-screen bg-white">
        <div className="px-8 pt-8 pb-2">
          <div className="max-w-5xl mx-auto flex bg-white border shadow rounded-lg p-4 justify-between items-start">
            <div className="w-[200px] bg-orange-500 text-white font-bold text-center flex items-center justify-center text-lg rounded-md">
              Likely Malicious
            </div>
            <div className="flex-1 pl-6 space-y-2">
              <div className="grid grid-cols-2 gap-x-8 gap-y-1 text-sm">
                <div>
                  <strong>Name:</strong> {filename}
                </div>
                <div>
                  <strong>SHA-256:</strong> {data.get_metadata.sha256}
                </div>
                <div>
                  <strong>Submission Date:</strong> {submissionDate}
                </div>
              </div>
            </div>
            <div className="flex flex-col gap-2 ml-4 mt-1">
              <button
                onClick={downloadJSON}
                className="bg-blue-200 hover:bg-blue-300 px-4 py-2 rounded"
              >
                JSON
              </button>
              <button
                onClick={downloadHTML}
                className="bg-purple-200 hover:bg-purple-300 px-4 py-2 rounded"
              >
                HTML
              </button>
              <button
                onClick={downloadSuricataJSON}
                className="bg-green-200 hover:bg-green-300 px-4 py-2 rounded"
              >
                Suricata JSON
              </button>
            </div>
          </div>
        </div>

        <div className="flex flex-1 px-8 pb-8 gap-6">
          <nav className="w-[260px] bg-gray-50 border-r p-4 space-y-2">
            {SECTIONS.map((label, idx) => (
              <div
                key={idx}
                onClick={() => setCurrentSection(idx)}
                className={`cursor-pointer h-12 flex items-center px-4 border-l-4 rounded ${
                  currentSection === idx
                    ? 'bg-white border-blue-600 text-blue-600'
                    : 'bg-blue-400 border-transparent text-white hover:bg-blue-500'
                }`}
              >
                {label}
              </div>
            ))}
          </nav>
          <main className="flex-1 overflow-auto p-4 bg-white rounded-xl shadow border-l-4 border-[#0F3ADA]">
            <h2 className="text-xl font-bold text-[#0F3ADA] mb-4">
              {SECTIONS[currentSection]}
            </h2>
            {currentSection === 2 ? (
              <iframe
                src={`/static/callgraphs/${baseName}.html`}
                className="w-full h-[800px] border-none rounded"
                sandbox="allow-scripts allow-same-origin"
              />
            ) : (
              <pre className="whitespace-pre-wrap">
                {allTexts[currentSection]}
              </pre>
            )}
          </main>
        </div>
      </div>
    </>
  )
}
