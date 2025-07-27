rule auto_rule_20250727015054_1119 {
  strings:
    $o0 = "x14000A616LL" wide ascii nocase
    $o1 = "v532" wide ascii nocase
    $o2 = "v550" wide ascii nocase
  condition:
    3 of ($o*)
}