rule auto_rule_20250726123805_1514 {
  strings:
    $o0 = "copy_start" wide ascii nocase
    $o1 = "dword_46EBC4" wide ascii nocase
    $o2 = "dword_456028" wide ascii nocase
  condition:
    3 of ($o*)
}