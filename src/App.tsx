//web\src\App.tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Layout from './components/Layout'
import MainPage from './pages/MainPage'
import AnalysisPage from './pages/AnalysisPage'
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
          <Route path="/reports" element={<ReportPage />} />
          <Route path="/reports/:filename" element={<ReportDetailPage />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  )
}
