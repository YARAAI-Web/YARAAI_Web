rule auto_rule_20250726062218_1545 {
  strings:
    $o0 = "dword_4C1680" wide ascii nocase
    $o1 = "dword_4C1270" wide ascii nocase
    $o2 = "dword_4C12F0" wide ascii nocase
  condition:
    3 of ($o*)
}