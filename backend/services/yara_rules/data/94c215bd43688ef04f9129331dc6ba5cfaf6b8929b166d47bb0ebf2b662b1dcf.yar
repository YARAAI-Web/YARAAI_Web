rule auto_rule_20250726165509_7406 {
  strings:
    $o0 = "gu_return" wide ascii nocase
    $o1 = "main_loop_0" wide ascii nocase
    $o2 = "dword_449A48" wide ascii nocase
    $o3 = "ReturnValue" wide ascii nocase
  condition:
    4 of ($o*)
}