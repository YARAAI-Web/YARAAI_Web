rule auto_rule_20250726190151_9160 {
  strings:
    $o0 = "dword_472264" wide ascii nocase
    $o1 = "_cpinfo" wide ascii nocase
    $o2 = "TrailUp3" wide ascii nocase
    $o3 = "dword_471924" wide ascii nocase
    $o4 = "old_esp" wide ascii nocase
  condition:
    4 of ($o*)
}