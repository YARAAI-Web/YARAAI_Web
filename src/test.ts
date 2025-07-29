// src/types.ts
export interface AnalysisResult {
  get_metadata: {
    module: string
    md5: string
    sha256: string
    sha1?: string
    format?: string
    filesize?: string
  }
  file_entropy: number
  string_stats: Record<string, any>
  pe_headers: Record<string, any>
  c_code: string[]
  h_code: string[]
  virustotal: {
    hashes: {
      md5: string
      sha1?: string
      sha256: string
      vhash?: string
    }
    file_type: string
    magic: string
    file_size: number
  }
  yara_rule: string
  suricata_rule: string
}
