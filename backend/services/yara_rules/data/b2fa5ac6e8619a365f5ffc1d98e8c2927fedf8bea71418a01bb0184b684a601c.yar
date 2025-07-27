rule auto_rule_20250726093958_1118 {
  strings:
    $o0 = "KSPdfCloudSvrProxy" wide ascii nocase
    $o1 = "xmmword_11B09F50" wide ascii nocase
    $o2 = "rdata" wide ascii nocase
  condition:
    3 of ($o*)
}