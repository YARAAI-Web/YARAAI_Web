rule auto_rule_20250726181019_8222 {
  strings:
    $o0 = "WritePrivateProfileSectionA" wide ascii nocase
    $o1 = "uPosition" wide ascii nocase
    $o2 = "chCount" wide ascii nocase
    $o3 = "dwFileOffsetHigh" wide ascii nocase
  condition:
    4 of ($o*)
}