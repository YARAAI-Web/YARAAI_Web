rule auto_rule_20250726172939_8515 {
  strings:
    $o0 = "dword_7817C" wide ascii nocase
    $o1 = "dword_1E9EC" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}