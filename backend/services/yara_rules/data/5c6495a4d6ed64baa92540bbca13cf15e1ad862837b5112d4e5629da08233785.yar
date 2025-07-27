rule auto_rule_20250726111921_4470 {
  strings:
    $o0 = "UnwindUp4_0" wide ascii nocase
    $o1 = "dword_427680" wide ascii nocase
    $o2 = "strncnt" wide ascii nocase
  condition:
    3 of ($o*)
}