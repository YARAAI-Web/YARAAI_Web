rule auto_rule_20250727034530_5575 {
  strings:
    $o0 = "x49E1u" wide ascii nocase
    $o1 = "dword_4337E3" wide ascii nocase
    $o2 = "xF89F2DA9" wide ascii nocase
  condition:
    3 of ($o*)
}