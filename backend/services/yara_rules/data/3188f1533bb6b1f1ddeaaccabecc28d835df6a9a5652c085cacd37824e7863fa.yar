rule auto_rule_20250726185616_0887 {
  strings:
    $o0 = "bTimeAdjustmentDisabled" wide ascii nocase
  condition:
    all of them
}