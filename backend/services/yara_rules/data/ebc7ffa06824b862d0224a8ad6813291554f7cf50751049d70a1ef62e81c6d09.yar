rule auto_rule_20250727000435_6432 {
  strings:
    $o0 = "x2993" wide ascii nocase
    $o1 = "x4617" wide ascii nocase
    $o2 = "x5435400000000LL" wide ascii nocase
  condition:
    3 of ($o*)
}