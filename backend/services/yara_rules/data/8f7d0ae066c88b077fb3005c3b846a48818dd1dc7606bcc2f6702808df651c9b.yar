rule auto_rule_20250726130931_5050 {
  strings:
    $o0 = "hDrop" wide ascii nocase
    $o1 = "CharUpperBuffW" wide ascii nocase
    $o2 = "dwItem2" wide ascii nocase
  condition:
    3 of ($o*)
}