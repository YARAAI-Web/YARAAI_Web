rule auto_rule_20250727033004_8461 {
  strings:
    $o0 = "x6E2Bu" wide ascii nocase
    $o1 = "xDF2EF25" wide ascii nocase
    $o2 = "x5D89u" wide ascii nocase
    $o3 = "dword_407842" wide ascii nocase
  condition:
    4 of ($o*)
}