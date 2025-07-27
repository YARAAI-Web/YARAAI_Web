rule auto_rule_20250726185749_4155 {
  strings:
    $o0 = "x76ABC1" wide ascii nocase
    $o1 = "x713F48" wide ascii nocase
    $o2 = "x73D4EC" wide ascii nocase
  condition:
    3 of ($o*)
}