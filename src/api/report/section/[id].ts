// src/pages/api/report/section/[id].ts
import type { NextApiRequest, NextApiResponse } from 'next'
import { Configuration, OpenAIApi } from 'openai'

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
})
const openai = new OpenAIApi(configuration)

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const { id } = req.query
  const { prompt } = req.body as { prompt?: string }

  // Validate
  if (req.method !== 'POST' || typeof prompt !== 'string') {
    return res.status(400).json({ error: 'Invalid request' })
  }

  try {
    const completion = await openai.createChatCompletion({
      model: 'gpt-4o-mini', // 사용하고 싶은 모델
      messages: [{ role: 'user', content: prompt }],
      max_tokens: 1024,
      temperature: 0.7,
    })

    const text = completion.data.choices[0].message?.content?.trim() || ''
    return res.status(200).json({ text })
  } catch (err) {
    console.error('OpenAI API Error:', err)
    return res.status(500).json({ error: 'OpenAI API error' })
  }
}
