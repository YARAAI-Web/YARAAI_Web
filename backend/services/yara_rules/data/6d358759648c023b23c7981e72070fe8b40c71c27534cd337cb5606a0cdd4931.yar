rule auto_rule_20250726133239_9728 {
  strings:
    $o0 = "dword_448F4C" wide ascii nocase
    $o1 = "ungetc" wide ascii nocase
    $o2 = "UnwindUp0_0" wide ascii nocase
  condition:
    3 of ($o*)
}