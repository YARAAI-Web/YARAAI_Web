rule auto_rule_20250727030743_8763 {
  strings:
    $o0 = "dword_459004" wide ascii nocase
    $o1 = "CalType" wide ascii nocase
    $o2 = "dwExceptionFlags" wide ascii nocase
  condition:
    3 of ($o*)
}