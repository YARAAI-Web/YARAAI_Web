import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import MainPage from './pages/MainPage'
import AnalysisPage from './pages/AnalysisPage'
import ReportPage from './pages/ReportPage'
import ReportDetailPage from './pages/ReportDetailPage'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/analysis" element={<AnalysisPage />} />
        <Route path="/reports" element={<ReportPage />} />
        <Route path="/reports/:filename" element={<ReportDetailPage />} />
      </Routes>
    </BrowserRouter>
  )
}
