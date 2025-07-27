rule auto_rule_20250726165808_1852 {
  strings:
    $o0 = "OnProcessingStart" wide ascii nocase
    $o1 = "GetHandle" wide ascii nocase
  condition:
    all of them
}