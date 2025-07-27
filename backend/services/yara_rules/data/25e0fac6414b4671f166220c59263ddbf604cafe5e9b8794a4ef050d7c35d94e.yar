rule auto_rule_20250726095037_8149 {
  strings:
    $o0 = "CodePagea" wide ascii nocase
    $o1 = "dword_40E020" wide ascii nocase
    $o2 = "dword_4119B0" wide ascii nocase
  condition:
    3 of ($o*)
}