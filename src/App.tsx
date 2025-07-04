// src/App.tsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Header from './components/Header'
import Layout from './components/Layout'
import MainPage from './pages/MainPage'
import AnalysisPage from './pages/AnalysisPage'
import HistoryPage from './pages/HistoryPage'
import HistoryDetailPage from './pages/HistoryDetailPage'
import ReportPage from './pages/ReportPage'

export default function App() {
  return (
    <BrowserRouter>
      <Header />

      <Layout>
        <Routes>
          {/* 1) 홈 */}
          <Route path="/" element={<MainPage />} />

          {/* 2) 분석 페이지 
              - /analysis 로 접근 시 홈으로 리다이렉트 
              - /analysis/:filename 으로만 AnalysisPage */}
          <Route path="/analysis" element={<Navigate to="/" replace />} />
          <Route path="/analysis/:filename" element={<AnalysisPage />} />

          {/* 3) 히스토리 */}
          <Route path="/history" element={<HistoryPage />} />
          <Route path="/history/:filename" element={<HistoryDetailPage />} />

          {/* 4) 보고서 페이지 
              - /report 로 접근 시 홈으로 리다이렉트 
              - /report/:filename 으로만 ReportPage */}
          <Route path="/report" element={<Navigate to="/" replace />} />
          <Route path="/report/:filename" element={<ReportPage />} />

          {/* 5) 그 외 모든 경로는 홈으로 */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  )
}
