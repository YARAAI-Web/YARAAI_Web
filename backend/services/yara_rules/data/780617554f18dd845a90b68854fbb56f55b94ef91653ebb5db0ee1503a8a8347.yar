rule auto_rule_20250726075549_7613 {
  strings:
    $o0 = "byte_427688" wide ascii nocase
    $o1 = "x3FFFu" wide ascii nocase
    $o2 = "byte_427EA0" wide ascii nocase
    $o3 = "dword_4275C8" wide ascii nocase
  condition:
    4 of ($o*)
}