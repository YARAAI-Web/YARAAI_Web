rule auto_rule_20250726073245_4681 {
  strings:
    $o0 = "TrailDown1" wide ascii nocase
    $o1 = "off_44BF78" wide ascii nocase
    $o2 = "TargetIp" wide ascii nocase
  condition:
    3 of ($o*)
}