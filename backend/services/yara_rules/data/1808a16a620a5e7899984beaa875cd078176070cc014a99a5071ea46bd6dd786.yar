rule auto_rule_20250726215535_8125 {
  strings:
    $o0 = "UnwindUp3_0" wide ascii nocase
    $o1 = "strncnt" wide ascii nocase
    $o2 = "dword_45D54C" wide ascii nocase
  condition:
    3 of ($o*)
}