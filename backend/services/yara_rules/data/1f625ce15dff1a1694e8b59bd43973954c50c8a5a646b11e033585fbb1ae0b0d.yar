rule auto_rule_20250726230819_0203 {
  strings:
    $o0 = "wsprintfA" wide ascii nocase
    $o1 = "pclsidHandler" wide ascii nocase
  condition:
    all of them
}