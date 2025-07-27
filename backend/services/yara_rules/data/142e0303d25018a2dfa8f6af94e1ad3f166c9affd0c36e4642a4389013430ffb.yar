rule auto_rule_20250726121930_3943 {
  strings:
    $o0 = "EnumServicesStatusW" wide ascii nocase
    $o1 = "F2Ch" wide ascii nocase
  condition:
    all of them
}