//web\src\components\Layout.tsx
import React, { type ReactNode } from 'react'

interface Props {
  children: ReactNode
}

export default function Layout({ children }: Props) {
  return (
    <div className="flex flex-col min-h-screen bg-gray-300">
      <main className="flex-1 relative pt-[30px]">{children}</main>
    </div>
  )
}
