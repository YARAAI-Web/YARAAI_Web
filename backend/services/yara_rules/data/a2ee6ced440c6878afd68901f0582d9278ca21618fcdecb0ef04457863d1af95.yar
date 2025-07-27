rule auto_rule_20250726084523_4689 {
  strings:
    $o0 = "lpCharType" wide ascii nocase
    $o1 = "x41C4u" wide ascii nocase
    $o2 = "x426870" wide ascii nocase
    $o3 = "UnwindUp5_0" wide ascii nocase
  condition:
    4 of ($o*)
}