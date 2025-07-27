rule auto_rule_20250726234511_7802 {
  strings:
    $o0 = "dword_42A01C" wide ascii nocase
    $o1 = "x79AB00000000LL" wide ascii nocase
    $o2 = "x7467" wide ascii nocase
  condition:
    3 of ($o*)
}