rule auto_rule_20250726184624_2166 {
  strings:
    $o0 = "TimeAdjustmentDisabled" wide ascii nocase
    $o1 = "off_42E41F" wide ascii nocase
  condition:
    all of them
}