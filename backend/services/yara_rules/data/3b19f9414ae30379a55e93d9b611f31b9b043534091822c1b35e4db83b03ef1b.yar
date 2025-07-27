rule auto_rule_20250727030300_8460 {
  strings:
    $o0 = "hdcDst" wide ascii nocase
    $o1 = "WaitCommEvent" wide ascii nocase
    $o2 = "fModal" wide ascii nocase
    $o3 = "lpClassName" wide ascii nocase
  condition:
    4 of ($o*)
}