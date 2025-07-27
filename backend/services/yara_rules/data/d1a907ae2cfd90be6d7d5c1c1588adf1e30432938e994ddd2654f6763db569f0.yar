rule auto_rule_20250727033655_5849 {
  strings:
    $o0 = "x4EE8" wide ascii nocase
    $o1 = "DeleteConfig" wide ascii nocase
    $o2 = "x4AF7u" wide ascii nocase
    $o3 = "xEE46EAFC" wide ascii nocase
  condition:
    4 of ($o*)
}