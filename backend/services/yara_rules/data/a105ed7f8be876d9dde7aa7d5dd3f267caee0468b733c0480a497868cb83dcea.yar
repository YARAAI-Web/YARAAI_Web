rule auto_rule_20250726230706_9675 {
  strings:
    $o0 = "EnumServicesStatusW" wide ascii nocase
    $o1 = "j_j__free" wide ascii nocase
  condition:
    all of them
}