rule auto_rule_20250726210638_2489 {
  strings:
    $o0 = "objects" wide ascii nocase
    $o1 = "Press" wide ascii nocase
    $o2 = "stdargv" wide ascii nocase
    $o3 = "fields" wide ascii nocase
  condition:
    4 of ($o*)
}