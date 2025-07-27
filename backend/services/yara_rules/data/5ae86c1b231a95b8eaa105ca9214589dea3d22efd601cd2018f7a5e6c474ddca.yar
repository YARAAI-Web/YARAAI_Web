rule auto_rule_20250726101522_4193 {
  strings:
    $o0 = "off_4B19B0" wide ascii nocase
  condition:
    all of them
}