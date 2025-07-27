rule auto_rule_20250726075019_1330 {
  strings:
    $o0 = "off_46C6E8" wide ascii nocase
    $o1 = "_startTwoArgErrorHandling" wide ascii nocase
  condition:
    all of them
}