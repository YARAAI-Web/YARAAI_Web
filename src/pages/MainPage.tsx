// src/pages/MainPage.tsx
import React, { useState, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import Layout from '../components/Layout'

export default function MainPage() {
  const [file, setFile] = useState<File | null>(null)
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const handleDrop = useCallback((e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    if (e.dataTransfer.files.length > 0) {
      setFile(e.dataTransfer.files[0])
    }
  }, [])

  const handleFileChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const picked = e.target.files?.[0] ?? null
      setFile(picked)
    },
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
        {
          headers: { 'Content-Type': 'multipart/form-data' },
        }
      )
      navigate('/analysis', { state: { filename: res.data.filename } })
    } catch (err: any) {
      console.error('Upload error:', err)
      const detail = err.response?.data?.detail
      alert(detail ?? '파일 업로드 중 오류가 발생했습니다.\n다시 시도해주세요.')
    } finally {
      setLoading(false)
    }
  }, [file, navigate])

  return (
    <Layout>
      <div
        className="w-[300px] h-[180px] border border-blue-400 bg-gray-100 
                   flex items-center justify-center my-10 text-gray-500 
                   cursor-pointer select-none"
        onDrop={handleDrop}
        onDragOver={(e) => e.preventDefault()}
        onClick={() => document.getElementById('fileInput')?.click()}
      >
        {file ? (
          <span className="truncate w-full px-2">{file.name}</span>
        ) : (
          'input the file'
        )}
        <input
          id="fileInput"
          type="file"
          accept=".exe,.dll"
          className="hidden"
          onChange={handleFileChange}
        />
      </div>

      <button
        onClick={handleAnalysis}
        disabled={!file || loading}
        title={!file ? '먼저 파일을 선택해 주세요' : undefined}
        className={`px-6 py-2 rounded transition-colors flex items-center justify-center ${
          loading
            ? 'bg-gray-300 text-gray-700 cursor-not-allowed'
            : 'bg-blue-500 text-white hover:bg-blue-600'
        }`}
      >
        {loading && (
          <svg
            className="animate-spin -ml-1 mr-2 h-5 w-5 text-white"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
            />
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
            />
          </svg>
        )}
        {loading ? 'Analyzing...' : 'Analysis'}
      </button>

      <div className="fixed bottom-4 right-4">
        <button
          onClick={() => alert('챗봇 기능은 추후 구현 예정입니다')}
          className="bg-blue-800 text-white w-12 h-12 rounded-full shadow-lg 
                     flex items-center justify-center text-2xl hover:bg-blue-900"
          title="챗봇 열기"
        >
          💬
        </button>
      </div>
    </Layout>
  )
}
