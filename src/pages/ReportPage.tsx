// src/pages/ReportPage.tsx
import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { fetchSection } from '../api/report'

export default function ReportPage() {
  const { filename } = useParams<{ filename: string }>()
  const [text, setText] = useState<string>('로딩 중…')

  useEffect(() => {
    if (!filename) return
    fetchSection(1, filename)
      .then(r => setText(r.text))
      .catch(() => setText('섹션 로드 실패'))
  }, [filename])

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">보고서: {filename}</h1>
      <pre className="whitespace-pre-wrap bg-gray-50 p-4 rounded">{text}</pre>
    </div>
  )
}
