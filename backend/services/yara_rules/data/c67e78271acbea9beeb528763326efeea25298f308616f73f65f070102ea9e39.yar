rule auto_rule_20250726172844_7220 {
  strings:
    $o0 = "hcur" wide ascii nocase
    $o1 = "lpFatDate" wide ascii nocase
    $o2 = "VkKeyScanExW" wide ascii nocase
    $o3 = "lpDisplayDevice" wide ascii nocase
  condition:
    4 of ($o*)
}