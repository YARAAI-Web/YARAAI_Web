rule auto_rule_20250726070629_9324 {
  strings:
    $o0 = "dword_64031420" wide ascii nocase
    $o1 = "dword_64031464" wide ascii nocase
    $o2 = "byte_64028B80" wide ascii nocase
  condition:
    3 of ($o*)
}