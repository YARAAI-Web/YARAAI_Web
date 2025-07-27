// src/hooks/useCapaReport.ts
import { useState, useEffect } from 'react'
import { fetchCapaReport } from '../api/fetchCapaResult'

export function useCapaReport(sha256: string) {
  const [report, setReport] = useState<string>('')
  const [loading, setLoading] = useState<boolean>(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (!sha256) return
    setLoading(true)
    setError(null)

    fetchCapaReport(sha256)
      .then((res) => {
        setReport(res.report)
      })
      .catch((e: Error) => {
        setError(e.message)
      })
      .finally(() => {
        setLoading(false)
      })
  }, [sha256])

  return { report, loading, error }
}
