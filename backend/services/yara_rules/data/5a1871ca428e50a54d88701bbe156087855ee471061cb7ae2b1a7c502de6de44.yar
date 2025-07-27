rule auto_rule_20250726083712_8702 {
  strings:
    $o0 = "Client" wide ascii nocase
    $o1 = "_pFirstBlock" wide ascii nocase
    $o2 = "_snprintf" wide ascii nocase
    $o3 = "off_4640F0" wide ascii nocase
  condition:
    4 of ($o*)
}