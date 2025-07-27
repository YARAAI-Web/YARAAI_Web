rule auto_rule_20250726191330_7429 {
  strings:
    $o0 = "FindWindowA" wide ascii nocase
    $o1 = "DlgDirSelectExA" wide ascii nocase
    $o2 = "GetWindowWord" wide ascii nocase
  condition:
    3 of ($o*)
}