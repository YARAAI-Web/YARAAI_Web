rule auto_rule_20250727032730_4388 {
  strings:
    $o0 = "dword_467EF4" wide ascii nocase
    $o1 = "dword_468074" wide ascii nocase
    $o2 = "_pFirstBlock" wide ascii nocase
  condition:
    3 of ($o*)
}