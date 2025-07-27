rule auto_rule_20250727040055_0993 {
  strings:
    $o0 = "llseek" wide ascii nocase
    $o1 = "lphe" wide ascii nocase
  condition:
    all of them
}