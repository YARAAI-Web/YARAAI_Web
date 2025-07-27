rule auto_rule_20250727043957_6706 {
  strings:
    $o0 = "dwBufferCoord" wide ascii nocase
    $o1 = "nTypeFlag" wide ascii nocase
    $o2 = "fInherit" wide ascii nocase
  condition:
    3 of ($o*)
}