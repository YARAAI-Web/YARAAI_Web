rule auto_rule_20250726161453_3086 {
  strings:
    $o0 = "ExecutingAffine" wide ascii nocase
    $o1 = "crt_debugger_hook" wide ascii nocase
    $o2 = "InitInstance" wide ascii nocase
  condition:
    3 of ($o*)
}