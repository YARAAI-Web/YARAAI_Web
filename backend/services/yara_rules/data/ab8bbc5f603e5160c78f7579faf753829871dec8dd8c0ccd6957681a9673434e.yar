rule auto_rule_20250727015108_9718 {
  strings:
    $o0 = "x580D4822" wide ascii nocase
  condition:
    all of them
}