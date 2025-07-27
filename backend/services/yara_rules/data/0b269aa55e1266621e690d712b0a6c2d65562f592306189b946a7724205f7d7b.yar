rule auto_rule_20250726141459_6270 {
  strings:
    $o0 = "StringTypeA" wide ascii nocase
    $o1 = "dodwords" wide ascii nocase
    $o2 = "dword_44C13C" wide ascii nocase
  condition:
    3 of ($o*)
}