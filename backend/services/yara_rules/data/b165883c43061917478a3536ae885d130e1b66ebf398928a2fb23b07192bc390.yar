rule auto_rule_20250726143609_5759 {
  strings:
    $o0 = "_seh_longjmp_unwind" wide ascii nocase
    $o1 = "program" wide ascii nocase
    $o2 = "dword_46ED5C" wide ascii nocase
  condition:
    3 of ($o*)
}