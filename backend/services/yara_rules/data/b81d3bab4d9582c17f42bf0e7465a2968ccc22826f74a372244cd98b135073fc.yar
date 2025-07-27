rule auto_rule_20250727023651_9861 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "TrailDown2" wide ascii nocase
    $o2 = "TrailDown1" wide ascii nocase
    $o3 = "x402811" wide ascii nocase
  condition:
    4 of ($o*)
}