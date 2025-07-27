rule auto_rule_20250726131239_1133 {
  strings:
    $o0 = "x7C38" wide ascii nocase
    $o1 = "dword_4364CE" wide ascii nocase
    $o2 = "PerformanceCounter" wide ascii nocase
  condition:
    3 of ($o*)
}