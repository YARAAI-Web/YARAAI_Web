import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Layout from './components/Layout'
import MainPage from './pages/MainPage'
import AnalysisPage from './pages/AnalysisPage'
import HistoryPage from './pages/HistoryPage'
import HistoryDetailPage from './pages/HistoryDetailPage'
import ReportPage from './pages/ReportPage'
import ReportDetailPage from './pages/ReportDetailPage'

export default function App() {
  return (
    <BrowserRouter>
      {/* 최상단 Header */}
      <Header />

      {/* 페이지 컨텐츠 */}
      <Layout>
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/analysis" element={<AnalysisPage />} />

          {/* History 목록 & 상세 */}
          <Route path="/history" element={<HistoryPage />} />
          <Route path="/history/:filename" element={<HistoryDetailPage />} />

          {/* Report (테스트용) */}
          <Route path="/report" element={<ReportPage />} />
          <Route path="/report/:filename" element={<ReportDetailPage />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  )
}
