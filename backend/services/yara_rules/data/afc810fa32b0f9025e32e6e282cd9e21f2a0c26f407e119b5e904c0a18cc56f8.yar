rule auto_rule_20250726144124_6878 {
  strings:
    $o0 = "fuLoad" wide ascii nocase
    $o1 = "VkKeyScanW" wide ascii nocase
    $o2 = "uIDCheckItem" wide ascii nocase
    $o3 = "DdeGetData" wide ascii nocase
  condition:
    4 of ($o*)
}