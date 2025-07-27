rule auto_rule_20250726123610_2756 {
  strings:
    $o0 = "dword_7C9A9C" wide ascii nocase
    $o1 = "xBE0F407F" wide ascii nocase
    $o2 = "dword_7C9040" wide ascii nocase
  condition:
    3 of ($o*)
}