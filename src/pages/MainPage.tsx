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
      {/*
        헤더 바로 아래에서 80px 아래로 떨어뜨리려면
        pt-20 에서 내려온 자식 컨테이너에 mt-12 (48px) 혹은 mt-16 (64px)을 주시면 되고
        드롭존–버튼 사이 간격은 space-y-8 (32px)
      */}
      <div className="flex flex-col items-center mt-16 space-y-8">
        {/* Drop zone (640×240px) */}
        <div
          onDrop={handleDrop}
          onDragOver={(e) => e.preventDefault()}
          onClick={() => document.getElementById('fileInput')?.click()}
          className="w-[640px] h-[240px] bg-white border-2 border-blue-600 rounded-lg flex items-center justify-center cursor-pointer"
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

        {/* Analysis 버튼 (264×50px) */}
        <button
          onClick={handleAnalysis}
          disabled={!file || loading}
          className={`w-[264px] h-[50px] text-[1.5rem] font-medium rounded-lg ${
            file && !loading
              ? 'bg-yaraai-light text-black hover:bg-opacity-90'
              : 'bg-gray-200 text-gray-400 cursor-not-allowed'
          }`}
        >
          {loading ? 'Analyzing...' : 'Analysis'}
        </button>
      </div>
    </Layout>
  )
}
