rule auto_rule_20250726230314_7987 {
  strings:
    $o0 = "dword_45D558" wide ascii nocase
    $o1 = "off_45CF40" wide ascii nocase
  condition:
    all of them
}