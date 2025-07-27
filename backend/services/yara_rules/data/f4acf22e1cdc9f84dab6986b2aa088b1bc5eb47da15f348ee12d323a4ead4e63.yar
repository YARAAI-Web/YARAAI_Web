rule auto_rule_20250726081509_8561 {
  strings:
    $o0 = "CPtoLCID" wide ascii nocase
    $o1 = "dword_45D530" wide ascii nocase
    $o2 = "old_esp" wide ascii nocase
  condition:
    3 of ($o*)
}