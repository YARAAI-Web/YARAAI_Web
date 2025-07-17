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
    "① Information",
    "② 정적 분석",
    "③ 동적 분석",
    "④ Call Graph",
    "⑤ 클러스터링",
    "⑥ MITRE ATT&CK",
    "⑦ CWE"
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

  useEffect(() => {
    if (!rawFilename) {
      navigate('/')
      return
    }
    setFilename(rawFilename)
  }, [rawFilename, navigate])

  useEffect(() => {
    if (!filename) return
    setLoading(true)

    const baseName = filename.replace(/\.[^.]+$/i, '')
    const keySections = `yaraai_sections_${baseName}`
    const keyDate = `yaraai_date_${baseName}`

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

    const savedSecs = sessionStorage.getItem(keySections)
    const savedDate = sessionStorage.getItem(keyDate)
    if (savedSecs) {
      setAllTexts(JSON.parse(savedSecs))
      setSubmissionDate(savedDate || new Date().toLocaleString())

      axios
        .get<AnalysisResult>(`/reports/${filename}`)
        .then((res) => setData(res.data))
        .catch((err) => setError(err.response?.data?.detail || err.message))
        .finally(() => setLoading(false))

      return
    }

    let nowStr = new Date().toLocaleString()
    axios
      .get<AnalysisResult>(`/reports/${filename}`)
      .then((res) => {
        setData(res.data)
        nowStr = new Date().toLocaleString()
        setSubmissionDate(nowStr)
        return Promise.all(
          SECTIONS.map((_, idx) => {
            if (idx === 3) return Promise.resolve('(Call Graph)')
            return axios
              .post<{ text: string }>('/api/section', {
                sectionId: idx + 1,
                filename,
              })
              .then((r) => r.data.text)
              .catch(() => '(불러오기 실패)')
          })
        )
      })
      .then((texts) => {
        setAllTexts(texts)
        sessionStorage.setItem(keySections, JSON.stringify(texts))
        sessionStorage.setItem(keyDate, nowStr)
      })
      .catch((err) => setError(err.response?.data?.detail || err.message))
      .finally(() => setLoading(false))
  }, [filename, location.state])

  if (loading) return <div className="p-8 text-center">로딩 중…</div>
  if (error) return <div className="p-8 text-red-500">오류 발생: {error}</div>
  if (!data || !filename)
    return <div className="p-8">분석 결과를 찾을 수 없습니다.</div>

  const baseName = filename.replace(/\.[^.]+$/i, '')

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
    const html = `<!DOCTYPE html><html lang=\"ko\"><head><meta charset=\"UTF-8\"/><title>보고서 - ${baseName}</title><style>
      body{font-family:sans-serif;padding:20px}
      .header{border:2px solid #000;padding:6px;margin-bottom:10px}
      h2{color:#0F3ADA;margin-top:30px}
      pre{white-space:pre-wrap}
      .iframe-container{border:1px solid #ccc;height:500px}
    </style></head><body>${htmlRef.current.innerHTML}</body></html>`
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
      {/* HTML 내보내기용 숨김 영역 */}
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
        {SECTIONS.map((section, idx) => (
          <div key={idx}>
            <h2>{section}</h2>
            {idx === 2 ? (
              <div className="iframe-container">
                <iframe
                  src={`${window.location.origin}/static/callgraphs/${baseName}.html`}
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

      {/* 실제 화면 UI */}
      <div className="flex flex-col min-h-screen bg-white">
        <div className="px-8 pt-4 pb-0">
          <div className="max-w-5xl mx-auto flex bg-white border shadow rounded-lg p-2 justify-between items-start">
            <div className="w-[200px] bg-orange-500 text-white font-bold text-center flex items-center justify-center text-lg rounded-md p-2">
              Likely Malicious
            </div>
            <div className="flex-1 pl-6 space-y-2">
              <div className="space-y-1 text-sm">
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
                onClick={downloadHTML}
                className="bg-purple-200 hover:bg-purple-300 px-4 py-2 rounded"
              >
                Report
              </button>
              <button
                onClick={downloadJSON}
                className="bg-blue-200 hover:bg-blue-300 px-4 py-2 rounded"
              >
                JSON
              </button>
              <button
                onClick={downloadSuricataJSON}
                className="bg-green-200 hover:bg-green-300 px-4 py-2 rounded"
              >
                Suricata
              </button>
            </div>
          </div>
        </div>

        <div className="flex flex-1 px-8 pt-0 pb-8 gap-6 -mt-1000">
          <nav className="w-[300px] bg-gray-50 flex flex-col h-[calc(100vh-80px)]">
            {SECTIONS.map((label, idx) => (
              <div
                key={idx}
                onClick={() => setCurrentSection(idx)}
                className={`flex-1 cursor-pointer flex items-center justify-start px-4 h-12 transition-colors ${
                  currentSection === idx
                    ? 'bg-[#F2F2F7] text-blue-600 font-semibold'
                    : 'bg-blue-400 text-white hover:bg-[#F2F2F7] hover:text-black'
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
            {currentSection === 3 ? (
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
