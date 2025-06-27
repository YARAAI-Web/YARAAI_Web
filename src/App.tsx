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
      {/* 헤더는 한 번만 */}
      <Header />

      {/* 페이지들은 Layout 안에서 렌더링 */}
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
