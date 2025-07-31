// src/pages/MainPage.tsx
import React, { useState, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import Layout from '../components/Layout'

export default function MainPage() {
  const [file, setFile] = useState<File | null>(null)
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  // ✅ 동적 분석 결과가 준비됐는지 확인하는 함수
  const waitForDynamicReport = async (uuid: string) => {
    const maxRetries = 60
    for (let i = 0; i < maxRetries; i++) {
      const res = await fetch(`/api/check-report/${uuid}`)
      const data = await res.json()
      if (data.exists) return true
      await new Promise((r) => setTimeout(r, 1000))
    }
    throw new Error('❌ 동적 분석 report.json 생성 실패')
  }

  const handleDrop = useCallback((e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    if (e.dataTransfer.files.length > 0) setFile(e.dataTransfer.files[0])
  }, [])

  const handleFileChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) =>
      setFile(e.target.files?.[0] ?? null),
    []
  )

  const handleAnalysis = useCallback(async () => {
    if (!file) return
    setLoading(true)

    const form = new FormData()
    form.append('file', file)

    try {
      const res = await axios.post<{ filename: string }>(
        'http://localhost:8000/upload',
        form,
        { headers: { 'Content-Type': 'multipart/form-data' } }
      )

      const filename = res.data.filename // 예: abc123.exe
      const baseName = filename.replace(/\.[^.]+$/, '') // abc123

      // 💡 기존 캐시 제거 (섞이는 문제 방지)
      sessionStorage.removeItem(`yaraai_sections_${baseName}`)
      sessionStorage.removeItem(`yaraai_date_${baseName}`)

      // ✅ 동적 분석 결과가 올 때까지 기다림
      await waitForDynamicReport(baseName)

      // ✅ 그제서야 페이지 이동
      navigate(`/analysis/${baseName}`)
    } catch (err: any) {
      console.error(err)
      alert(err.response?.data?.detail || '파일 업로드 중 오류가 발생했습니다.')
    } finally {
      setLoading(false)
    }
  }, [file, navigate])

  return (
    <Layout>
      <div className="flex flex-col items-center mt-20 space-y-12">
        <div
          className="w-[980px] h-[344px] rounded-xl p-4 flex flex-col items-start space-y-2 relative"
          style={{
            border: '1.2px solid rgba(0,0,0,0.15)',
            borderRadius: '10px',
            marginTop: '80px',
          }}
        >
          <p className="w-full text-center font-bold text-[16px] relative top-[10px]">
            Input Your <span style={{ color: '#1b65fe' }}>File</span>
          </p>

          <div
            onDrop={handleDrop}
            onDragOver={(e) => e.preventDefault()}
            onClick={() => document.getElementById('fileInput')?.click()}
            className="w-[908px] h-[250px] bg-[#f2f2f7] rounded-xl border border-gray-300 flex flex-col items-center justify-center mx-auto cursor-pointer mt-[20px] relative"
          >
            {file && (
              <span className="text-lg font-medium truncate max-w-[90%]">
                {file.name}
              </span>
            )}
            <input
              id="fileInput"
              type="file"
              accept=".exe,.dll"
              className="hidden"
              onChange={handleFileChange}
            />
          </div>
        </div>

        <button
          type="button"
          onClick={handleAnalysis}
          disabled={!file || loading}
          className={`
              w-[300px] h-[50px] rounded-full text-[16px] font-extrabold border transition-colors duration-200
              ${
                file && !loading
                  ? 'bg-[#1b65fe] border-[#1b65fe] text-[#FFFFFF] hover:bg-[#1550cc]'
                  : 'bg-gray-200 border-gray-300 text-gray-500'
              }
            `}
          style={{ marginTop: '50px' }}
        >
          {loading ? 'Analyzing...' : 'Analysis'}
        </button>
      </div>
    </Layout>
  )
}
