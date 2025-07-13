// src/pages/MainPage.tsx
import React, { useState, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import Layout from '../components/Layout'

export default function MainPage() {
  const [file, setFile] = useState<File | null>(null)
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  /* ------------------------------ handlers ------------------------------ */
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
      navigate(`/analysis/${res.data.filename}`)
    } catch (err: any) {
      console.error(err)
      alert(err.response?.data?.detail || '파일 업로드 중 오류가 발생했습니다.')
    } finally {
      setLoading(false)
    }
  }, [file, navigate])

  /* ------------------------------ UI ------------------------------ */
  return (
    <Layout>
      <div className="flex flex-col items-center mt-20 space-y-12">
        {/* ────────────── 바깥 네모 ────────────── */}
        <div
          className="
            w-[766px] h-[290px] 
            rounded-xl 
            p-4
            flex flex-col items-start
            space-y-2
            relative"
          style={{
            border: '1.2px solid rgba(0,0,0,0.15)',
            borderRadius: '10px',
            marginTop: '80px',
          }}
        >
          {/* 왼쪽 상단 텍스트 */}
          <p className="w-full text-center font-bold text-[16px] relative top-[10px]">
            Input Your <span style={{ color: '#1b65fe' }}>File</span>
          </p>

          {/* ────────── 안쪽 네모 (가로·세로·색·테두리) ────────── */}
          <div
            onDrop={handleDrop}
            onDragOver={(e) => e.preventDefault()}
            onClick={() => document.getElementById('fileInput')?.click()}
            className="w-[720px] h-[200px] 
            bg-[#f2f2f7] 
            rounded-xl 
            border border-gray-300 
            flex flex-col items-center justify-center
            mx-auto
            cursor-pointer
            mt-[20px]
            relative"
            style={{
              border: '1.2px solid rgba(0,0,0,0.15)',
              borderRadius: '10px',
            }}
          >
            {/* 파일이 있으면 파일명 표시 */}
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

        {/* ────────────── Analysis 버튼 ────────────── */}
        <button
          type="button"
          onClick={handleAnalysis}
          disabled={!file || loading}
          className={`
            w-[250px] h-[50px] rounded-full text-[16px] font-extrabold border transition-colors duration-200
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
