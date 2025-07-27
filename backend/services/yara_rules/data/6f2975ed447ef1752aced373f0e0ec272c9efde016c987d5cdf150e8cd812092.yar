rule auto_rule_20250726131828_8105 {
  strings:
    $o0 = "dword_44A028" wide ascii nocase
    $o1 = "dword_449A34" wide ascii nocase
    $o2 = "dword_449FF8" wide ascii nocase
    $o3 = "dword_44A048" wide ascii nocase
  condition:
    4 of ($o*)
}