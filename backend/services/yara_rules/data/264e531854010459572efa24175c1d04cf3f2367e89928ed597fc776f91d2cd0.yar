rule auto_rule_20250727014901_1766 {
  strings:
    $o0 = "dword_43440E" wide ascii nocase
    $o1 = "x618F" wide ascii nocase
    $o2 = "IsWindowEnabled" wide ascii nocase
  condition:
    3 of ($o*)
}