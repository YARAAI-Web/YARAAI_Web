rule auto_rule_20250726145543_8773 {
  strings:
    $o0 = "systemroot" wide ascii nocase
    $o1 = "off_77604" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}