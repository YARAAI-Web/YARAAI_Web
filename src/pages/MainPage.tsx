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
    if (e.dataTransfer.files.length > 0) setFile(e.dataTransfer.files[0])
  }, [])

  const handleFileChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setFile(e.target.files?.[0] ?? null)
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
        { headers: { 'Content-Type': 'multipart/form-data' } }
      )
      navigate('/analysis', { state: { filename: res.data.filename } })
    } catch (err: any) {
      console.error(err)
      alert(err.response?.data?.detail || '파일 업로드 중 오류가 발생했습니다.')
    } finally {
      setLoading(false)
    }
  }, [file, navigate])

  return (
    <Layout>
      <div className="flex flex-col items-center mt-20">
        {/* Drop zone (800×400px) */}
        <div
          onDrop={handleDrop}
          onDragOver={(e) => e.preventDefault()}
          onClick={() => document.getElementById('fileInput')?.click()}
          className="w-[800px] h-[400px] bg-white rounded-lg flex items-center justify-center cursor-pointer"
          style={{ border: '2px solid #A3E635' }} // 연두색 border
        >
          {file ? (
            <span className="text-black text-[1.5rem] truncate">
              {file.name}
            </span>
          ) : (
            <span className="text-gray-500 text-[1.5rem]">input the file</span>
          )}
          <input
            id="fileInput"
            type="file"
            accept=".exe,.dll"
            className="hidden"
            onChange={handleFileChange}
          />
        </div>

        {/* Analysis 버튼 (300×75px) */}
        <button
          onClick={handleAnalysis}
          disabled={!file || loading}
          style={{
            marginTop: '50px',
            backgroundColor: file && !loading ? '#A3E635' : undefined,
            cursor: !file || loading ? 'not-allowed' : 'pointer',
          }}
          className="w-[300px] h-[75px] text-[1.5rem] font-medium rounded-lg"
        >
          {loading ? 'Analyzing...' : 'Analysis'}
        </button>
      </div>
    </Layout>
  )
}
