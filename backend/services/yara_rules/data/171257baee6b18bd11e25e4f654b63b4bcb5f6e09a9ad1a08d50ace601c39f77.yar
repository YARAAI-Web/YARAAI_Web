rule auto_rule_20250727041810_7675 {
  strings:
    $o0 = "dword_458984" wide ascii nocase
    $o1 = "_cropzeros" wide ascii nocase
    $o2 = "off_4587EC" wide ascii nocase
  condition:
    3 of ($o*)
}