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
      alert(err.response?.data?.detail ?? '파일 업로드 중 오류가 발생했습니다.')
    } finally {
      setLoading(false)
    }
  }, [file, navigate])

  return (
    <Layout>
      <div className="w-full max-w-3xl px-6">
        {/* 드롭존 */}
        <div
          onDrop={handleDrop}
          onDragOver={(e) => e.preventDefault()}
          onClick={() => document.getElementById('fileInput')?.click()}
          className={`w-full h-64 mt-16 border-2 border-blue-600 bg-white rounded-lg
                      flex items-center justify-center cursor-pointer`}
        >
          {file ? (
            <span className="truncate px-4 text-gray-700">{file.name}</span>
          ) : (
            <span className="text-gray-500 text-xl">input the file</span>
          )}
          <input
            id="fileInput"
            type="file"
            accept=".exe,.dll"
            className="hidden"
            onChange={handleFileChange}
          />
        </div>

        {/* Analysis 버튼 */}
        <button
          onClick={handleAnalysis}
          disabled={!file || loading}
          className={`
            mt-8 block mx-auto w-48 h-12 text-lg font-medium text-white rounded
            ${
              file && !loading
                ? 'bg-blue-600 hover:bg-blue-700'
                : 'bg-gray-400 cursor-not-allowed'
            }
          `}
        >
          {loading ? 'Analyzing...' : 'Analysis'}
        </button>
      </div>
    </Layout>
  )
}
