rule auto_rule_20250727020541_1347 {
  strings:
    $o0 = "UnwindUp6_0" wide ascii nocase
    $o1 = "dword_411170" wide ascii nocase
    $o2 = "x4043F1" wide ascii nocase
  condition:
    3 of ($o*)
}