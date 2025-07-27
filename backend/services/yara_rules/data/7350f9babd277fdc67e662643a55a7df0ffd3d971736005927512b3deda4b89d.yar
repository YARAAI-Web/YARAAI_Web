rule auto_rule_20250726060043_3582 {
  strings:
    $o0 = "_tmpfname" wide ascii nocase
    $o1 = "old_esp" wide ascii nocase
    $o2 = "dword_4643E0" wide ascii nocase
  condition:
    3 of ($o*)
}