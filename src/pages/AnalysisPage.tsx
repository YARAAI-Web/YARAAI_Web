// src\pages\AnalysisPage.tsx
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
  pe_headers: {
    number_of_sections?: number
    sections?: { name: string }
    imports?: { dll: string }
    [key: string]: any
  }
  c_code: string[]
  h_code: string[]
  virustotal: Record<string, any>
  yara_rule: string
  suricata_rule: string
  tags?: string[]
}

const SECTIONS = [
  '① Information',
  '② 정적 분석',
  '③ 동적 분석',
  '④ Call Graph',
  '⑤ MITRE ATT&CK',
  '⑥ CWE',
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
  const [showPeDetails, setShowPeDetails] = useState(false)

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
    const html = `<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"/>
<title>보고서 - ${baseName}</title>
<style>
  body {
    font-family: 'Segoe UI', 'Malgun Gothic', sans-serif;
    padding: 20px;
    font-size: 14px;
  }
  .header {
    border: 2px solid #000;
    padding: 6px;
    margin-bottom: 10px;
  }
  h2 {
    color: #0F3ADA;
    margin-top: 30px;
  }
  pre {
    white-space: pre-wrap;
    font-family: 'Segoe UI', 'Malgun Gothic', sans-serif;
    font-weight: 350;
    line-height: 1.6;
    margin-top: 8px;
  }
  .iframe-container {
    border: 1px solid #ccc;
    height: 500px;
  }
</style>
</head><body>${htmlRef.current.innerHTML}</body></html>`

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
            {idx === 0 ? (
              <>
                <table className="vt-table mt-4">
                  <tbody>
                    <tr>
                      <th>MD5</th>
                      <td>{data.virustotal.hashes.md5}</td>
                    </tr>
                    <tr>
                      <th>SHA-1</th>
                      <td>{data.virustotal.hashes.sha1 ?? '—'}</td>
                    </tr>
                    <tr>
                      <th>SHA-256</th>
                      <td>{data.virustotal.hashes.sha256}</td>
                    </tr>
                    <tr>
                      <th>Vhash</th>
                      <td>{data.virustotal.hashes.vhash ?? '—'}</td>
                    </tr>
                    <tr>
                      <th>File type</th>
                      <td>{data.virustotal.file_type}</td>
                    </tr>
                    <tr>
                      <th>Magic</th>
                      <td>{data.virustotal.magic}</td>
                    </tr>
                    <tr>
                      <th>File size</th>
                      <td>
                        {data.virustotal.file_size.toLocaleString()} bytes
                      </td>
                    </tr>
                    {data.virustotal.trid && (
                      <tr>
                        <th>TrID 상위 3개</th>
                        <td>
                          {data.virustotal.trid
                            .slice(0, 3)
                            .map(
                              (t: any) => `${t.file_type} (${t.probability}%)`
                            )
                            .join(', ')}
                        </td>
                      </tr>
                    )}
                    <tr>
                      <th>DetectItEasy</th>
                      <td>
                        {data.virustotal.analysis.detectiteasy?.result ?? '—'}
                      </td>
                    </tr>
                    <tr>
                      <th>Magika</th>
                      <td>{data.virustotal.analysis.magika?.result ?? '—'}</td>
                    </tr>
                    <tr>
                      <th>Packer</th>
                      <td>{data.virustotal.packer ?? '—'}</td>
                    </tr>
                  </tbody>
                </table>
                <pre>{allTexts[idx].split('<VirusTotal')[0].trim()}</pre>
              </>
            ) : idx === 3 ? (
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
        {/* 상단 요약 헤더 */}
        <div className="px-8 pt-4 pb-0">
          <div className="max-w-5xl mx-auto relative flex bg-white p-2 justify-start items-start gap-6">
            <div className="w-[200px] bg-orange-500 text-white font-bold text-center flex items-center justify-center text-lg rounded-md p-2">
              Likely Malicious
            </div>
            <div className="flex-none pl-5 space-y-2 -mt-[3px] -ml-4">
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
            <div className="absolute -top-[20px] right-[30px] flex flex-col space-y-[2px]">
              <button
                onClick={downloadHTML}
                className="
                  bg-[#1b65fe]          /* 메인 배경색 (원하시는 색으로) */
                  hover:bg-[#F2F2F7]    /* 호버 시 색 진해짐 */
                  text-[#FFFFFF]           /* 글자색 흰색 */
                  font-bold            /* 글자 굵게 */
                  text-xl              /* 큰 글자 크기 */
                  transition
                  px-[20px]                 /* 좌우 여백: 2rem */
                  py-[7px]                 /* 상하 여백: 1rem */
                  rounded-full         /* 완전한 pill(캡슐) 모양 */
                  border-[0.1px]
                  border-[rgba(0,0,0,0.15)]
                "
              >
                Report
              </button>
              <button
                onClick={downloadJSON}
                className="
                  bg-[#1b65fe]          /* 메인 배경색 (원하시는 색으로) */
                  hover:bg-[#F2F2F7]    /* 호버 시 색 진해짐 */
                  text-[#FFFFFF]           /* 글자색 흰색 */
                  font-bold            /* 글자 굵게 */
                  text-xl              /* 큰 글자 크기 */
                  transition
                  px-[20px]                 /* 좌우 여백: 2rem */
                  py-[7px]                 /* 상하 여백: 1rem */
                  rounded-full         /* 완전한 pill(캡슐) 모양 */
                  border-[0.1px]
                  border-[rgba(0,0,0,0.15)]
                "
              >
                JSON
              </button>
              <button
                onClick={downloadSuricataJSON}
                className="
                  bg-[#1b65fe]          /* 메인 배경색 (원하시는 색으로) */
                  hover:bg-[#F2F2F7]    /* 호버 시 색 진해짐 */
                  text-[#FFFFFF]           /* 글자색 흰색 */
                  font-bold            /* 글자 굵게 */
                  text-xl              /* 큰 글자 크기 */
                  transition
                  px-[20px]                 /* 좌우 여백: 2rem */
                  py-[7px]                 /* 상하 여백: 1rem */
                  rounded-full         /* 완전한 pill(캡슐) 모양 */
                  border-[0.1px]
                  border-[rgba(0,0,0,0.15)]
                "
              >
                Suricata
              </button>
            </div>
          </div>
        </div>

        <div
          style={{
            height: '1px',
            backgroundColor: 'rgba(0,0,0,0.15)',
            margin: '1.5rem 0rem 0rem',
          }}
        />

        {/* 사이드 네비 + 메인 컨텐츠 */}
        <div className=" flex flex-1 px-8 pt-0 pb-8 gap-6">
          <nav className="relative w-[220px] bg-gray-50 flex flex-col h-[calc(100vh-80px)] border-r-4 border-[#0F3ADA]">
            <div className="absolute top-0 left-full right-0 h-px bg-gray-300" />
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
            <div
              className="
                absolute
                top-0
                left-full
                right-0
                border-t
                border-gray-300
              "
            />
          </nav>

          <main className="flex-1 overflow-auto p-4 bg-white rounded-xl shadow border-l-4 border-[#0F3ADA] pl-[40px] pr-[40px]">
            <h2 className="text-xl font-bold text-[#0F3ADA] mb-4 tracking-wide">
              {SECTIONS[currentSection]}
            </h2>

            {currentSection === 3 ? (
              <iframe
                src={`/static/callgraphs/${baseName}.html`}
                className="w-full h-[800px] border-none rounded"
                sandbox="allow-scripts allow-same-origin"
              />
            ) : currentSection === 0 ? (
              /* ① Information */
              <>
                {/* 1) VirusTotal 테이블 */}
                <table className="vt-table mt-4">
                  <tbody>
                    <tr>
                      <th>MD5</th>
                      <td>{data.virustotal.hashes.md5}</td>
                    </tr>
                    <tr>
                      <th>SHA-1</th>
                      <td>{data.virustotal.hashes.sha1 ?? '—'}</td>
                    </tr>
                    <tr>
                      <th>SHA-256</th>
                      <td>{data.virustotal.hashes.sha256}</td>
                    </tr>
                    <tr>
                      <th>Vhash</th>
                      <td>{data.virustotal.hashes.vhash ?? '—'}</td>
                    </tr>
                    <tr>
                      <th>File type</th>
                      <td>{data.virustotal.file_type}</td>
                    </tr>
                    <tr>
                      <th>Magic</th>
                      <td>{data.virustotal.magic}</td>
                    </tr>
                    <tr>
                      <th>File size</th>
                      <td>
                        {data.virustotal.file_size.toLocaleString()} bytes
                      </td>
                    </tr>
                    {data.virustotal.trid && (
                      <tr>
                        <th>TrID 상위 3개</th>
                        <td>
                          {data.virustotal.trid
                            .slice(0, 3)
                            .map(
                              (t: any) => `${t.file_type} (${t.probability}%)`
                            )
                            .join(', ')}
                        </td>
                      </tr>
                    )}
                    <tr>
                      <th>DetectItEasy</th>
                      <td>
                        {data.virustotal.analysis.detectiteasy?.result ?? '—'}
                      </td>
                    </tr>
                    <tr>
                      <th>Magika</th>
                      <td>{data.virustotal.analysis.magika?.result ?? '—'}</td>
                    </tr>
                    <tr>
                      <th>Packer</th>
                      <td>{data.virustotal.packer ?? '—'}</td>
                    </tr>
                  </tbody>
                </table>
                {/* 2) GPT 요약 */}
                <pre
                  className="whitespace-pre-wrap"
                  style={{
                    fontFamily: 'semibold', // 다른 섹션과 동일
                    fontWeight: 350,
                    lineHeight: '1.6',
                  }}
                >
                  {allTexts[0].split('<VirusTotal')[0].trim()}
                </pre>
              </>
            ) : currentSection === 1 ? (
              <>
                {/* ② 정적 분석의 본문 */}
                <pre
                  className="
                    whitespace-pre-wrap
                    "
                  style={{
                    fontFamily: 'semibold',
                    fontWeight: 350,
                    lineHeight: '1.6',
                  }}
                >
                  {allTexts[1]}
                </pre>

                {/* ↘ 여기, 본문 바로 아래에 토글 버튼 */}
                <div className="mt-4">
                  <button
                    onClick={() => setShowPeDetails((v) => !v)}
                    className="text-sm bg-gray-100 hover:bg-gray-200 px-3 py-1 rounded"
                  >
                    {showPeDetails ? 'PE 세부정보 숨기기' : 'PE 세부정보 보기'}
                  </button>
                </div>
                {showPeDetails && (
                  <div className="mt-2 mb-6 p-4 bg-gray-50 border rounded space-y-2 text-sm">
                    <div>
                      <strong>Import DLL:</strong>{' '}
                      {Array.isArray(data.pe_headers.imports)
                        ? data.pe_headers.imports.map((s) => s.dll).join(', ')
                        : 'N/A'}
                    </div>
                    <div>
                      <strong>섹션 개수:</strong>{' '}
                      {data.pe_headers.number_of_sections ?? 'N/A'}
                    </div>
                    <div>
                      <strong>섹션 정보:</strong>{' '}
                      {Array.isArray(data.pe_headers.sections)
                        ? data.pe_headers.sections.map((s) => s.name).join(', ')
                        : 'N/A'}
                    </div>
                  </div>
                )}
              </>
            ) : (
              <pre
                className="
                  whitespace-pre-wrap
                  "
                style={{
                  fontFamily: 'semibold',
                  fontWeight: 350,
                  lineHeight: '1.6',
                }}
              >
                {allTexts[currentSection]}
              </pre>
            )}
          </main>
          <div
            className="
                absolute 
                bottom-0         /* 컨테이너(=nav 높이) 바로 아래에 붙음 */
                left-[300px]     /* nav 너비만큼 들어옴 */
                right-0          /* 오른쪽 끝까지 */
                border-t-2 
                border-gray-300
              "
          />
        </div>
      </div>
    </>
  )
}
