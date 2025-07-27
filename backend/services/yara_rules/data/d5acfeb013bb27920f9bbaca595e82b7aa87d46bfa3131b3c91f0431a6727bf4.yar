rule auto_rule_20250726203547_1850 {
  strings:
    $o0 = "TrailUp3" wide ascii nocase
    $o1 = "_NLG_Notify" wide ascii nocase
    $o2 = "byte_44E2DC" wide ascii nocase
  condition:
    3 of ($o*)
}