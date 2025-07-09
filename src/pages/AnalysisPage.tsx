// src/pages/AnalysisPage.tsx
import { useEffect, useState, useRef } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import axios from 'axios'

interface AnalysisResult {
  get_metadata: {
    module: string
    md5: string
    sha256: string
    sha1?: string
    format?: string
    filesize?: string
  }
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

  const [filename, setFilename] = useState<string | null>(null)
  const [data, setData] = useState<AnalysisResult | null>(null)
  const [submissionDate, setSubmissionDate] = useState<string>('')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [currentSection, setCurrentSection] = useState(0)

  // GPT 응답 캐시 (1~7번)
  const [allTexts, setAllTexts] = useState<string[]>(
    Array(SECTIONS.length).fill('로딩 중…')
  )

  // HTML 다운로드용 off-screen 컨테이너
  const htmlRef = useRef<HTMLDivElement>(null)

  // filename 세팅
  useEffect(() => {
    if (!rawFilename) {
      navigate('/')
      return
    }
    setFilename(rawFilename)
  }, [rawFilename, navigate])

  // 메타·섹션 1~7 호출
  useEffect(() => {
    if (!filename) return

    setLoading(true)
    axios
      .get<AnalysisResult>(`/reports/${filename}`)
      .then((res) => {
        setData(res.data)
        setSubmissionDate(new Date().toLocaleString())

        SECTIONS.forEach((_, idx) => {
          // Call Graph(3번)만 건너뛰고 GPT 요청
          if (idx === 2) return

          axios
            .post<{ text: string }>('/api/section', {
              sectionId: idx + 1,
              metadata: {
                module: res.data.get_metadata.module,
                sha256: res.data.get_metadata.sha256,
                fileType: res.data.get_metadata.format || '',
                fileSize: res.data.get_metadata.filesize || '',
              },
            })
            .then((r) => {
              setAllTexts((prev) => {
                const copy = [...prev]
                copy[idx] = r.data.text
                return copy
              })
            })
            .catch(() => {
              setAllTexts((prev) => {
                const copy = [...prev]
                copy[idx] = '(불러오기 실패)'
                return copy
              })
            })
        })
      })
      .catch((err) => setError(err.response?.data?.detail || err.message))
      .finally(() => setLoading(false))
  }, [filename])

  if (loading) return <div className="p-8 text-center">로딩 중…</div>
  if (error) return <div className="p-8 text-red-500">오류 발생: {error}</div>
  if (!data || !filename)
    return <div className="p-8">분석 결과를 찾을 수 없습니다.</div>

  // JSON 다운로드
  const downloadJSON = () => {
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

  // HTML 다운로드
  const downloadHTML = () => {
    if (!htmlRef.current) return
    const content = htmlRef.current.innerHTML
    const full = `<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <title>보고서 - ${filename}</title>
  <style>
    body { font-family: sans-serif; padding: 20px; }
    .header { border:2px solid #000; padding:10px; display:flex; justify-content:space-between; margin-bottom:20px; }
    h2 { color:#0F3ADA; margin-top:30px; }
    .section { margin-bottom: 20px; }
    .iframe-container { border:1px solid #ccc; height:500px; }
    pre { white-space: pre-wrap; }
  </style>
</head>
<body>
  ${content}
</body>
</html>`
    const blob = new Blob([full], { type: 'text/html' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${filename}.html`
    a.click()
    URL.revokeObjectURL(url)
  }

  return (
    <>
      {/* OFF-SCREEN: HTML export */}
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
                  src={`/static/callgraphs/${filename.replace(
                    /\.exe$/i,
                    ''
                  )}.html`}
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

      {/* SCREEN UI */}
      <div className="flex flex-col min-h-screen bg-white">
        <div className="px-8 pt-8 pb-2">
          <div className="max-w-5xl mx-auto flex bg-white border shadow rounded-lg p-4 justify-between items-start">
            <div className="w-[200px] bg-orange-500 text-white font-bold text-center flex items-center justify-center text-lg rounded-md h-full">
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
            </div>
          </div>
        </div>

        <div className="flex flex-1 px-8 pb-8 gap-6">
          <div className="w-[260px] bg-gray-50 border-r p-4 space-y-2">
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
          </div>
          <div className="flex-1 overflow-auto">
            <section className="bg-white shadow rounded-xl border-l-4 border-[#0F3ADA] p-4 h-full">
              <h2 className="text-xl font-bold text-[#0F3ADA] mb-4">
                {SECTIONS[currentSection]}
              </h2>
              {currentSection === 2 ? (
                <iframe
                  key={`callgraph-${filename}`}
                  src={`/static/callgraphs/${filename.replace(
                    /\.exe$/i,
                    ''
                  )}.html`}
                  className="w-full h-[800px] border-none rounded"
                  sandbox="allow-scripts allow-same-origin"
                />
              ) : (
                <pre className="whitespace-pre-wrap">
                  {allTexts[currentSection]}
                </pre>
              )}
            </section>
          </div>
        </div>
      </div>
    </>
  )
}
