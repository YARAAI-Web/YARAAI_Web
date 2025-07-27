rule auto_rule_20250727033317_0297 {
  strings:
    $o0 = "dword_4C130C" wide ascii nocase
    $o1 = "dword_4C1168" wide ascii nocase
  condition:
    all of them
}