rule auto_rule_20250726083939_8318 {
  strings:
    $o0 = "should" wide ascii nocase
    $o1 = "old_esp" wide ascii nocase
    $o2 = "dword_469A00" wide ascii nocase
  condition:
    3 of ($o*)
}